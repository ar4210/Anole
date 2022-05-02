class Cage():
    def __init__(self, name, temperature = -1, humidity = -1):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity

    # INSERT RASBERRY PI CODE HERE
    def get_temp(self):
        # Retrieve temperature from RPi4
        pass

    def get_humidity(self):
        # Retrieve Humidity from RPi4
        pass

    def set_temp(self):
        self.temperature = self.get_temp()
        return self.temperature

    def set_humidity(self):
        self.humidity = self.get_humidity()
        return self.humidity
