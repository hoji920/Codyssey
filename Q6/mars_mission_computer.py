import random

class DummySensor:
    def __init__(self):
        self.env_values={}
        self.set_env()
        self.get_env()
    
    def set_env(self):
        self.env_values = {
            "mars_base_internal_temperature": round(random.uniform(18.0, 30.0), 2),
            "mars_base_external_temperature": round(random.uniform(0.0, 21.0), 2),
            "mars_base_internal_humidity": random.randint(50, 60),
            "mars_base_external_illuminance": random.randint(500, 715),
            "mars_base_internal_co2": round(random.uniform(0.02, 0.1), 3),
            "mars_base_internal_oxygen": round(random.uniform(4.0, 7.0), 1)
        }
    
    def get_env(self):
        return self.env_values
    

if __name__ == "__main__":
    # 인스턴스화
    ds = DummySensor()

    # 데이터 설정 (set_env 호출)
    ds.set_env()

    # 데이터 확인 (get_env 호출 및 출력)
    env_data = ds.get_env()
    print("\n=== 현재 화성 기지 환경 정보 ===")
    for key, value in env_data.items():
        print(f"{key}: {value}")



    