# assigment 1

# Base class for all devices
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def power_on(self):
        print(f"{self.brand} {self.model} Powering on...\n Please enter your password:_____")
    
    def power_off(self):
        print(f"{self.brand} {self.model} powering off...\n Shutting Down")

        
# Child class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, color, storage_space):
        super().__init__(brand, model)  # Call parent constructor
        self.color = color
        self.__storage_space = storage_space  # Private attribute for encapsulation
        
    # Getter method for private storage attribute
    def get_storage_space(self):
        return self.__storage_space
    
    # Method install apps storage management
    def install_app(self, app_name, size):
        if size <= self.__storage_space:
            self.__storage_space -= size
            print(f"Installed {app_name} successfully. Storage left: {self.__storage_space}GB.\n")
        else:
            print(f"Storage space is running out.\n{app_name} app cannot be installed.\nStorage left is {self.__storage_space}GB")
    
    # Method to delete apps and free up storage
    def delete_app(self, app_name, size):
        self.__storage_space += size
        print(f"Successfully deleted {app_name} app.\nFreed up space is {size}GB.\nStorage available: {self.__storage_space}GB")
        
    # Polymorphism - Override parent's power_on method
    def power_on(self):
        print(f"{self.brand} {self.model} is turning on.....Welcome to OS")


# Create  device instance
my_device = Device("Oppo", "A74")
my_device.power_on()
# my_device.power_off()

print("\nMy phone")
# Create a smartphone instance with specific attributes
phone = Smartphone("Oppo", "A74", "black", 128)
phone.power_on()  # Calls overridden method
print(f"\nStorage before app installation: {phone.get_storage_space()}GB")

# Install and manage apps
phone.install_app("WhatsApp", 2)
phone.install_app("Telegram", 25)
phone.delete_app("Safaricom", 20)