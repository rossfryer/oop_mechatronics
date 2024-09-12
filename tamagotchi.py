from microbit import *
import random

# Tamagotchi class for the Microbit
class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50    # Scale of 0-100
        self.happiness = 50 # Scale of 0-100
        self.energy = 50    # Scale of 0-100

    def feed(self):
        display.show(Image.HAPPY)
        if self.hunger > 10:
            self.hunger -= 10
        else:
            self.hunger = 0
        self.happiness += 5
        self.energy += 2
        sleep(1000)

    def play(self):
        #Add code
        return

    def sleep(self):
        #Add code
        return

    def display_stats(self):
        # Display stats on the LEDs (hunger, happiness, energy as brightness levels)
        return

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
        else:
            # Let the Tamagotchi sleep if no buttons are pressed for a while
            pet.sleep()
        
        # Simulate energy, hunger decreasing over time
        # Add code

tamagotchi_game()
