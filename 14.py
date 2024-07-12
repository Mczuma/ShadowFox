class MobilePhone:
    def_init_(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
    self.screen_type = screen_type
    self.network_type = network_type
    self.dual_sim = dual_sim
    self.front_camera = front_camera
    self.rear_camera = rear_camera
    self.ram = ram
    self.storage = storage

class Apple(MobilePhone):
    def_init_(self, front_camera, rear_camera, ram, storage):
    super()._init_('Touch Screen', '5G', True, front_camera, rear_camera, ram, storage)
class Samsung(MobilePhone):
    def_init_('Touch Screen', '5G', True, front_camera, rear_camera, ram, storage)

    apple_phone =Apple(12MP, 48MP, 4GB, 64GB)
    samsung_phone = Samsung(16MP, 32MP, 3GB, 32GB)

print("Apple Phone:")
print(apple_phone.get_info())
print()
print("Samsung Phone:")
print(samsung_phone.get_info())
