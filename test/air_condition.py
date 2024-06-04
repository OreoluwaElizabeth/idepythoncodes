from test import AirConditioner

def test_AirConditonerIsOn():
    ac = AirConditioner()
    ac.turn_on()
    assert ac.is_on == True

def test_AirConditionerIsOff():
    ac = AirConditioner()
    ac.turn_on()
    ac.turn_off()
    assert ac.is_on == False

def test_AirConditionerTemperatureIncreases():
    ac = AirConditioner()
    ac.turn_on()
    initialTemperature = ac.get_temperature()
    ac.inrease_temperature
    newTemperature = ac.get_temperature()
    assert newTemperature == initialTemperature - 1
    assert newTemperature >= 16