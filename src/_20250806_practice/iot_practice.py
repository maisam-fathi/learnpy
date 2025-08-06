class Device:
    count = 0

    def __init__(self, ip, mac_address, name):
        self.ip = ip
        self.mac_address = mac_address
        self.name = name
        Device.count += 1
        # result = ping the device
        result = False
        if result:
            self.status = 'active'
        else:
            self.status = 'unknown'

    def get_status(self):
        # return result based on ping results for self.ip
        return self.status


class TV(Device):
    def turn_on(self):
        # connect to self.ip and turn on
        pass

    def turn_off(self):
        # connect to self.ip and turn off
        pass


class Thermostat(Device):
    def get_temperature(self):
        # connect to self.ip and read the temperature and return the result
        result = 22  # dummy temperature value
        return result
