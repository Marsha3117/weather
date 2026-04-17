from app.models.weather import Weather


def format_weather(weather: Weather) -> str:
    """
    Genera una representación en texto del clima actual.
    """

    if not weather:
        return "❌ No hay datos del clima disponibles."

    return f"""
╔══════════════════════╗
   🌤 Clima actual
╠══════════════════════╣
   Estado: {weather.description}
   🌡 Temperatura: {weather.temperature}°C
   💨 Viento: {weather.windspeed} km/h
╚══════════════════════╝
"""


def format_forecast(forecast: list[dict]) -> str:
    """
    Formatea el pronóstico de 5 días.
    """

    if not forecast:
        return "❌ No hay datos de pronóstico disponibles."

    output = "\n📅 Pronóstico 5 días:\n"

    for day in forecast:
        output += (
            f"{day['date']} | "
            f"{day['description']} "
            f"{day['temp_min']}°C - {day['temp_max']}°C\n"
        )

    return output