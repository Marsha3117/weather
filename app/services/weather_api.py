import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.config.settings import BASE_URL, GEOCODING_URL, TIMEOUT, CACHE_EXPIRATION
from app.utils.cache import get_from_cache, save_to_cache
from app.models.weather import Weather


# -------------------------
# Utils
# -------------------------

def normalize_city(city: str) -> str:
    return city.strip().title()


def map_weather_code(code: int) -> str:
    mapping = {
        0: "Despejado",
        1: "Parcialmente nublado",
        2: "Nublado",
        3: "Muy nublado",
        45: "Niebla",
        48: "Niebla con escarcha",
        51: "Llovizna ligera",
        53: "Llovizna moderada",
        55: "Llovizna intensa",
        61: "Lluvia ligera",
        63: "Lluvia moderada",
        65: "Lluvia fuerte",
        71: "Nieve ligera",
        73: "Nieve moderada",
        75: "Nieve fuerte",
        95: "Tormenta eléctrica"
    }
    return mapping.get(code, "Desconocido")


# -------------------------
# API Calls
# -------------------------

def get_coordinates(city: str) -> tuple[float | None, float | None]:
    if not city or not city.strip():
        return None, None

    city = normalize_city(city)

    params = {
        "name": city,
        "count": 1
    }

    try:
        response = requests.get(GEOCODING_URL, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()

        results = data.get("results")
        if not results:
            return None, None

        result = results[0]
        lat = result.get("latitude")
        lon = result.get("longitude")

        return lat, lon

    except requests.exceptions.RequestException:
        return None, None


def get_weather(lat: float, lon: float) -> Weather | None:
    if lat is None or lon is None:
        return None

    cache_key = f"{lat},{lon}"

    cached = get_from_cache(cache_key, CACHE_EXPIRATION)
    if cached:
        return Weather(**cached)  # 🔥 FIX CLAVE

    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,windspeed_10m,weathercode"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()

        current = data.get("current")
        if not current:
            return None

        weather = Weather(
            temperature=current.get("temperature_2m"),
            windspeed=current.get("windspeed_10m"),
            description=map_weather_code(current.get("weathercode"))
        )

        save_to_cache(cache_key, weather.__dict__)

        return weather

    except requests.exceptions.RequestException:
        return None


def get_weather_multiple(cities: list[str]) -> dict[str, Weather | None]:
    results = {}

    def fetch(city: str):
        normalized = normalize_city(city)

        lat, lon = get_coordinates(normalized)
        if lat is None or lon is None:
            return normalized, None

        weather = get_weather(lat, lon)
        return normalized, weather

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch, city): city for city in cities}

        for future in as_completed(futures):
            city = futures[future]

            try:
                normalized, weather = future.result()
                results[normalized] = weather
            except Exception:
                results[normalize_city(city)] = None

    return results


def get_forecast(lat: float, lon: float) -> list[dict] | None:
    if lat is None or lon is None:
        return None

    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,weathercode",
        "forecast_days": 5,
        "timezone": "auto"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()

        daily = data.get("daily")
        if not daily:
            return None

        forecast = []

        for date, tmax, tmin, code in zip(
            daily["time"],
            daily["temperature_2m_max"],
            daily["temperature_2m_min"],
            daily["weathercode"]
        ):
            forecast.append({
                "date": date,
                "temp_max": tmax,
                "temp_min": tmin,
                "description": map_weather_code(code)
            })

        return forecast

    except requests.exceptions.RequestException:
        return None