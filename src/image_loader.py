import cv2
class ImageLoader:

    """Handles Loading and saving of Images"""
        
    def open_image(self):
        print("\nOpening Image Module ...")
        
        image_path = input("Enter Image Path:")

        image = cv2.imread(image_path)

        if image is None:
            print("\n❌ Could not load the image.")
            print("Please check the file path.")
            return

        print("\n✅ Image loaded successfully!")

        print(f"Height: {image.shape[0]} pixels")
        print(f"Width: {image.shape[1]} pixels")
        print(f"Channels: {image.shape[2]}")

        cv2.imshow("VisionLab - Loaded Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()