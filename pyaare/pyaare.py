import requests

class PyAare:

    def __init__(self, city: str):
        self._checkCity(city)
        self._city = city
        self.refresh()

    def refresh(self):
        """
        Get the newest data
        """

        try:
            aareNode = self._getData()["aare"]
            self._tempC = float(aareNode['temperature'])
            self._tempText = aareNode["temperature_text"]
            self._flow = aareNode["flow"]
            self._flowText = aareNode["flow_text"]
        except Exception as e:
            raise RuntimeError(f"Error while getting Aare data: {e}")

    def _checkCity(self, city: str):
        cities = requests.get(
            f'https://aareguru.existenz.ch/v2018/cities', timeout=5).json()
        supportedCities = set([entry["city"].lower() for entry in cities])
        if city.lower() not in supportedCities:
            raise RuntimeError(f"City {city} is not supported")


    def _getData(self):
        return requests.get(
            f'http://aareguru.existenz.ch/currentV2.php?app=homeAnwendung?city={self._city}', timeout=5).json()


    def _assertHttpOk(self, statusCode: int):
        statusCodeOk = 200
        if statusCode != statusCodeOk:
            raise Exception(f'HTTP status code is {statusCode}, expected {statusCodeOk}')

    def __repr__(self) -> str:
        return f"Aare Temperature: {self.tempC}°C, Text: {self.tempText}, Flow: {self.flow}, Text: {self.flowText}"

    @property
    def tempC(self) -> float:
        """ Returns the Aare temperature
        Returns:
        float: temperature in degree celcius
        """
        return self._tempC

    @property
    def tempText(self) -> str:
        """ Returns the description text of the Aare temperature
        Returns:
        str: description text
        """
        return self._tempText

    @property
    def flow(self) -> int:
        """ Returns the Aare flow in m^3
        Returns:
        float: temperature in degree celcius
        """
        return self._flow

    @property
    def flowText(self) -> str:
        """ Returns the description text of the Aare flow
        Returns:
        str: description text
        """
        return self._flowText