from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def show_device(self):
        print(f"Device: {self.__class__.__name__}")

    @abstractmethod
    def turn_on(self):
        pass


class SmartLight(SmartDevice):
    def turn_on(self):
        print("The smart light is turned on.")


class SmartFan(SmartDevice):
    def turn_on(self):
        print("The smart fan is turned on.")


class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("The smart speaker is turned on.")


light = SmartLight()
fan = SmartFan()
speaker = SmartSpeaker()

light.show_device()
light.turn_on()

fan.show_device()
fan.turn_on()

speaker.show_device()
speaker.turn_on()


class SecurityCamera:
    def check_status(self):
        print("Security camera is monitoring.")


class DoorLock:
    def check_status(self):
        print("Door lock is secured.")


devices = [SecurityCamera(), DoorLock()]

for device in devices:
    device.check_status()