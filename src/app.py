from menu import display_menu
from image_loader import ImageLoader


class VisionLab:
    def __init__(self):
        self.name = "VisionLab"
        self.version = "1.0.0"
        self.loader = ImageLoader()

    def start(self):
        print("=" * 50)
        print(f"Welcome to {self.name}")
        print(f"Version: {self.version}")
        print("=" * 50)

        while True:

            display_menu()

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.loader.open_image()

            elif choice == "2":
                print("Saving Image... Coming Soon!")

            elif choice == "3":
                print("Image Information... Coming Soon!")

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")