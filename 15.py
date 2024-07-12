class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
    self.screen_type = screen_type
    self.network_type = network_type
    self.dual_sim = dual_sim
    self.front_camera = rear_camera
    self.ram = ram 
    self.storage = storage
    self.call_log = []

    def make_call(self, number):
        self.call_log.append(f"Made call to {number}")
        print(f"Calling {number}...")
        
    def receive_call(self, number):
        self.call_log.append(f"Received call from {number}")
        print("Taking picture...")
    def take_picture(self):
        print("Taking picyure...")

    def get_info(self):
        return f"Screen Type: {self.screen_type},Network Type:
{self.network_type}, Dual SIM: {self.dual_sim}, Front Camera:
{self.front_camera}, Rear Camera: {self.rear_camera}, RAM: {self.ram},Storage: {self.storage}"

class Apple(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        super().__init__('Touch Screen', '5G', True, front_camera, rear_camera, ram, storage)

    def take_picture(self):
        super().take_picture()
        print("Using advanced camera software...")

class Samsung(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        super().__init__('Touch Screen', '5G', True, front_camera, rear_camera, ram, storage)

    def take_picture(self):
        super().take_picture()
        print("Using advanced camera software with AI features...")

apple_phone1 = Apple(12MP, 48MP, 4GB, 64GB)
apple_phone2 = Apple(16MP, 32MP, 6GB, 128GB)

samsung_phone1 =Samsung(16MP, 32MP, 3GB, 32GB)
samsung_phone = Samsung(12MP, 48MP, 4GB, 64GB)

apple_phone1.make_call("0540878907")
apple_phone1.receive_call("0540878907")
apple_phone1.take_picture()

samsung_phone1.make_call("0500823307")
samsung_phone1.receive_call("0500823307")
samsung_phone1.take_picture()

      