from microbit import *
import random
import music


# Tamagotchi class for the Microbit
class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50    # Scale of 0-100
        self.happiness = 50 # Scale of 0-100
        self.energy = 50    # Scale of 0-100

    def feed(self):
        display.show(Image.HAPPY)
        music.play(['c', 'd', 'e', 'c'])
        if self.hunger > 10:
            self.hunger -= 10
        else:
            self.hunger = 0
        self.happiness += 5
        self.energy += 2
        sleep(1000)

    def play(self):
        display.show(Image.BUTTERFLY)
        music.play(['c', 'a', 'a', 'a'])
        if self.happiness < 100:
            self.happiness += 10
        if self.energy > 5:
            self.energy -= 5
        else:
            self.energy = 0
        sleep(1000)

    def sleep(self):
        display.scroll("z")
        if self.energy < 90:
            self.energy += 10
        self.hunger += 5
        sleep(2000)

    def display_stats(self):
        # Display hunger, happiness, and energy as bar levels on the LED grid
        for i in range(5):
            display.set_pixel(0, i, int(self.hunger / 10))  # Hunger
            display.set_pixel(1, i, 0)
            display.set_pixel(2, i, int(self.happiness / 10))  # Happiness
            display.set_pixel(3, i, 0)
            display.set_pixel(4, i, int(self.energy / 10))  # Energy
        sleep(1000)
        display.clear()

    def is_alive(self):
        if self.hunger >= 100 or self.energy <= 0:
            display.show(Image.SKULL)
            sleep(2000)
            return False
        return True

# Main game loop
def tamagotchi_game():
    pet = Tamagotchi("Tammy")
    
    while pet.is_alive():
        display.show(Image.HEART)  # Display a heart while the pet is alive
        
        if button_a.is_pressed() and button_b.is_pressed():
            # Show stats if both buttons are pressed
            pet.display_stats()
        elif button_a.is_pressed():
            # Feed the Tamagotchi if button A is pressed
            pet.feed()
        elif button_b.is_pressed():
            # Play with the Tamagotchi if button B is pressed
            pet.play()
        elif accelerometer.was_gesture('shake'):
            display.show(Image.CONFUSED)
            sleep(1000)

        elif temperature()<26:
            display.scroll("brrrrrr")
            sleep(1000)
        else:
            # Let the Tamagotchi sleep if no buttons are pressed for a while
            pet.sleep()
        
        # Simulate hunger and energy decreasing over time
        pet.hunger += 1
        pet.energy -= 1
        
    
        
        sleep(1000)

tamagotchi_game()
