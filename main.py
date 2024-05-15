from utils.dice_game import DiceGame
from utils.user_manager import UserManager
from utils.user import User
from utils.score import Score

UserManager_instance = UserManager()
User_instance = User()

def main():
    while True:
        print(f"Welcome to Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            UserManager_instance.register()
        elif choice == "2":
            UserManager_instance.login()
        elif choice == "3":
            break
        else:
            print("\nInvalid choice. Please try again.\n")
    
main()  