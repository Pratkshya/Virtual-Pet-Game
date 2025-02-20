import time, random

class Pet:
    def __init__(self,name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.health = 50
        self.alive = True

    def feed_pet(self):
        if self.alive:
            print(f"{self.name} is eating...")
            self.food_animation()
            print()
            self.hunger = max(0, self.hunger - 20)
            self.happiness = min(100, self.happiness +10)
            print(f"{self.name}'s hunger is now {self.hunger} and happiness is now {self.happiness}")
        else:
            print(f"{self.name} is no longer with us. Please restart to play again.")    

    def play_with_pet(self):
        if self.alive:
            print(f"{self.name} is playing!")
            self.health = min(100, self.health + 20)
            self.happiness = min(100, self.happiness +10)
            print(f"{self.name}'s health is now {self.health} and happiness is now {self.happiness}")
        else:
            print(f"{self.name} is no longer with us. Please restart to play again.") 

    def check_pet(self):
        if self.hunger >= 80:
            self.health = max(0, self.health - 10)
            print(f"{self.name}'s health is getting worse due to hunger. Feed your pet!")
        if self.happiness <=20:
            self.health = max(0, self.health - 10)    
            print(f"{self.name} is getting sick and sad. Play with your pet to make it happy!")
        if self.health <= 0:
            self.alive = False
            print(f"{self.name} has died. GAME OVER!")    


    def status(self):
        if self.alive:
            print(f"\n{self.name}'s Status: ")
            print(f"Hunger: {self.hunger}")
            print(f"Happiness: {self.happiness}")
            print(f"Health: {self.health}")
        else:
            print(f"{self.name} is no longer alive.")

    def is_alive(self):
        return self.alive
    
    def food_animation(self):
        pet_food = ["🍗", "🥩", "🍖", "🍰","🍓"]
        for food in pet_food:
            print(food, end=" ", flush=True)
            time.sleep(0.5)
    
def main():    
    print("🐾 Welcome to the Real-Time Virtual Pet Game!")
    pet_name = input("Enter a name for your pet: ")
    pet = Pet(pet_name)

    while pet.is_alive():
        print("\nChoose an option: ")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Check your pet's status")
        print("4. Exit the game")

        choice = input("\nEnter your choice: ")   

        if choice == "1":
            pet.feed_pet()
        elif choice == "2":
            pet.play_with_pet()
        elif choice == "3":
            pet.check_pet()
            pet.status()
        elif choice == "4":
            print(f"Goodbye! {pet.name} will miss you!")
            break
        else:
            print("Invalid choice. Please try again.")

        time.sleep(1)
        pet.hunger = min(100, pet.hunger + random.randint(8,20))
        pet.happiness = max(0, pet.happiness - random.randint(0,10))
        time.sleep(1)

if __name__ == "__main__":      
    main()        
