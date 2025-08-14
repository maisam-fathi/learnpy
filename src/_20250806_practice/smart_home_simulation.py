# Exercise:
# Design a basic simulation of a smart home with various smart devices.
# You will implement a base class `SmartDevice` with common attributes
# and behavior, and create two subclasses `SmartLight` and `SmartSpeaker`.
# The goal is to use class inheritance, instance tracking, conditional logic,
# and method implementation.

# Step 1:
# Define a class called SmartDevice with the following:
# - class variable `device_count` to track the total number of devices created.
# - instance variables: `ip_address`, `device_name`, `status` (either "online" or "offline")
# - `__init__` method to initialize the values. You may simulate connection:
#   if the last digit of the IP address is even, set the status to "online", else "offline".
# - a method `get_status()` to return the device name and current status.

class SmartDevice:
    device_count = 0

    def __init__(self, ip_address, device_name):
        self.ip_address = ip_address
        self.device_name = device_name
        SmartDevice.device_count += 1

        # Define device status offline or online
        last_digit = int(self.ip_address.split('.')[-1])
        if last_digit % 2 == 0:
            self.status = 'online'
        else:
            self.status = 'offline'

    def get_status(self):
        return f"{self.device_name} is {self.status}"

    @classmethod
    def get_device_count(cls):
        return cls.device_count


# Step 2:
# Create a subclass called SmartLight that inherits from SmartDevice.
# Add a method `toggle_light()` that prints "Light turned ON" if offline, and "Light toggled" if online.
class SmartLight(SmartDevice):
    def toggle_light(self):
        if self.status == 'online':
            print('Light toggled.')
        elif self.status == 'offline':
            self.status = 'online'
            print('Light turned ON.')
        else:
            print('Unknown status.')


# Step 3:
# Create another subclass called SmartSpeaker.
# Add a method `play_music()` that prints "Playing music on [device_name]" only if the status is "online".
# Otherwise, print "Device is offline. Cannot play music."
class SmartSpeaker(SmartDevice):
    def play_music(self):
        if self.status == 'online':
            print(f'Playing music on {self.device_name}.')
        else:
            print('Device is offline. Cannot play music.')


# Step 4:
# In your main block, create several instances of both device types.
# Print their statuses and simulate using their specific methods.
# Also, print the total number of smart devices created using `SmartDevice.device_count`.
LivingRoomSpeaker = SmartSpeaker('192.168.0.0', 'Living room speaker')
LivingRoomLight = SmartLight('192.168.0.1', 'Living room light')
BedroomSpeaker = SmartSpeaker('192.168.0.3', 'Bedroom speaker')
BedroomLight = SmartLight('192.168.0.4', 'Bedroom light')

print(f'There are {SmartDevice.device_count} smart devices in home.')

print(f'{LivingRoomSpeaker.device_name} is {LivingRoomSpeaker.get_status()}.')
print(f'{LivingRoomLight.device_name} is {LivingRoomLight.get_status()}.')

LivingRoomSpeaker.play_music()
LivingRoomLight.toggle_light()
BedroomSpeaker.play_music()
BedroomLight.toggle_light()
