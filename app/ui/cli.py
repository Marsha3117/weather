def get_city() -> str:
    """
    Solicita al usuario una ciudad válida.
    """

    while True:
        city = input("🌍 Ingresa el nombre de una ciudad: ").strip()

        if city:
            return city

        print("⚠️ La ciudad no puede estar vacía. Intenta de nuevo.")


def get_cities() -> list[str]:
    """
    Solicita múltiples ciudades válidas separadas por coma.
    """

    while True:
        raw = input("🌍 Ingresa ciudades separadas por coma: ").strip()

        if not raw:
            print("⚠️ Debes ingresar al menos una ciudad.")
            continue

        cities = [city.strip() for city in raw.split(",") if city.strip()]

        if cities:
            return cities

        print("⚠️ No se ingresaron ciudades válidas. Intenta de nuevo.")