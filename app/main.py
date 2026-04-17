from app.ui.cli import get_city, get_cities
from app.services.weather_api import (
    get_coordinates,
    get_weather,
    get_weather_multiple,
    get_forecast
)
from app.utils.formatter import (
    format_weather,
    format_forecast
)


def main():
    # Selección de modo
    while True:
        mode = input("¿Consultar una ciudad o varias? (1/m): ").strip().lower()
        if mode in ("1", "m"):
            break
        print("⚠️ Opción inválida. Usa '1' o 'm'.")

    # 🌍 MÚLTIPLES CIUDADES
    if mode == "m":
        cities = get_cities()
        results = get_weather_multiple(cities)

        for city, weather in results.items():
            print(f"\n🌍 {city}")

            if not weather:
                print("❌ No disponible")
                continue

            print(format_weather(weather))

        return

    # 🌍 UNA CIUDAD
    city = get_city()

    lat, lon = get_coordinates(city)

    if None in (lat, lon):
        print("❌ No se pudo encontrar la ciudad.")
        return

    print(f"\n🌍 {city}")

    weather = get_weather(lat, lon)

    if not weather:
        print("❌ No se pudo obtener el clima.")
        return

    print(format_weather(weather))

    forecast = get_forecast(lat, lon)

    if forecast:
        print(format_forecast(forecast))