from menu import display_menu

class VisionLab:
    def __init__(self):
        self.name = "VisionLab"
        self.version = "1.0.0"

    def start(self):
        print("=" *50)
        print(f"Welcome to {self.name}")
        print(f"Version: {self.version}")
        print("=" *50)


    while True:
        display_menu

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            print("Opening image... Coming soon!")
        elif choice == "2":
            print("Saving Image ... Coming Soon!")
        elif choice == "3":
            print("Image information ... Coming Soon!")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
