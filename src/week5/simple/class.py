from abc import ABC, abstractmethod
from playsound import playsound

# 1. Abstraction


class AudioDevice(ABC):
    def __init__(self, sound_file):
        self.__sound_file = sound_file   # 4. Encapsulation (private attribute)

    # Getter (controlled access)
    def get_sound_file(self):
        return self.__sound_file

    # Setter (controlled modification)
    def set_sound_file(self, new_file):
        if isinstance(new_file, str) and new_file.endswith((".mp3", ".wav")):
            self.__sound_file = new_file
        else:
            raise ValueError("Invalid sound file format. Must be .mp3 or .wav")

    # 1. Abstraction: force subclasses to implement play_sound
    @abstractmethod
    def play_sound(self):
        pass


# 2. Inheritance + 3. Polymorphism
class Car(AudioDevice):
    def __init__(self):
        super().__init__("car.mp3")

    def play_sound(self):
        print("Car is driving... 🚗")
        playsound(self.get_sound_file())


class Smartphone(AudioDevice):
    def __init__(self):
        super().__init__("phone.mp3")

    def play_sound(self):
        print("Smartphone is calling... 📱")
        playsound(self.get_sound_file())


class Dog(AudioDevice):
    def __init__(self):
        super().__init__("dog.mp3")

    def play_sound(self):
        print("Dog is barking... 🐶")
        playsound(self.get_sound_file())


class Birds(AudioDevice):
    def __init__(self):
        super().__init__("birds.mp3")

    def play_sound(self):
        print("Birds singing... 🐶")
        playsound(self.get_sound_file())


# ---- Usage ----
devices = [Birds(), Car(), Smartphone(), Dog()]

for device in devices:   # 3. Polymorphism: same method, different behavior
    device.play_sound()


# Encapsulation in action
dog = Dog()
print("Original dog sound:", dog.get_sound_file())
dog.set_sound_file("angry_dog.mp3")  # safely update sound file
print("Updated dog sound:", dog.get_sound_file())
