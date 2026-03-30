import random

class DummySensor:
    def __init__(self):
        self.env_values={}
        self.set_env()
    
    def set_env(self):
        self.env_values = {
            "mars_base_internal_temperature": round(random.uniform(15.0, 25.0), 2),
            "mars_base_external_temperature": round(random.uniform(-100.0, -10.0), 2),
            "mars_base_internal_humidity": random.randint(30, 60),
            "mars_base_external_illuminance": random.randint(0, 5000),
            "mars_base_internal_co2": round(random.uniform(0.03, 0.06), 3),
            "mars_base_internal_oxygen": round(random.uniform(19.0, 21.0), 1)
        }
sensor = DummySensor()
print(sensor.env_values)
    