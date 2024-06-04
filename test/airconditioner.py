class AirConditioner:
    def _init_(self):
        self.is_on = False
        self.temperature = 0

    @property
    def is_on(self):
        return self.is_on

    @property
    def temperature(self):
        return self.temperature

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_temperature(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def increase_temperature(self):
        if self.is_on:
            if self.temperature < 30:
                self.temperature += 1
                return True
            else:
                return False
            return False

    def decrease_temperature(self):
        if self.is_on:
            if self.temperature > 16:
                self.temperature -= 1
                return True
            else:
                return False
            return False