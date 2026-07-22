# Parent Class
class TrafficDevice:
    def activate(self):
        print("Traffic device activated.")


# Child Class 1
class TrafficLight(TrafficDevice):
    def activate(self):
        print("Traffic Light: Switching from RED to GREEN.")


# Child Class 2
class SpeedCamera(TrafficDevice):
    def activate(self):
        print("Speed Camera: Capturing speed of vehicles.")


# Child Class 3
class PedestrianSignal(TrafficDevice):
    def activate(self):
        print("Pedestrian Signal: Walk signal is ON.")


# Additional Child Class
class EmergencySiren(TrafficDevice):
    def activate(self):
        print("Emergency Siren: Giving priority to emergency vehicles.")


# Creating objects
traffic_light = TrafficLight()
speed_camera = SpeedCamera()
pedestrian_signal = PedestrianSignal()
emergency_siren = EmergencySiren()

# Storing objects in a list
devices = [
    traffic_light,
    speed_camera,
    pedestrian_signal,
    emergency_siren]

# Polymorphism: activate all devices without checking their types
print(" Smart Traffic Management System ")

for device in devices:
    device.activate()