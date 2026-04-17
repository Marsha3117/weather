class Weather:
    """
    Representa los datos del clima de una ubicación.

    Attributes:
        temperature (float | str): Temperatura actual en grados Celsius.
        windspeed (float | str): Velocidad del viento en km/h.
        description (str): Descripción del estado del clima.

    Example:
        >>> weather = Weather(20, 10, "Nublado")
        >>> print(weather.temperature)
        20
    """

    def __init__(self, temperature, windspeed, description):
        """
        Inicializa un objeto Weather con los datos del clima.

        Args:
            temperature (float | str): Temperatura actual.
            windspeed (float | str): Velocidad del viento.
            description (str): Descripción del clima.
        """
        self.temperature = temperature
        self.windspeed = windspeed
        self.description = description

    def __repr__(self):
        """
        Representación del objeto para debugging.

        Returns:
            str: Representación legible del objeto Weather.
        """
        return (
            f"Weather(temperature={self.temperature}, "
            f"windspeed={self.windspeed}, "
            f"description='{self.description}')"
        )