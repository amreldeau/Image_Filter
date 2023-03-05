import tkinter as tk
from tkinter import filedialog
import cv2

class ImageFilterApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Filter App")

        self.input_image = None
        self.output_images = {}

        # Create UI elements
        self.input_button = tk.Button(master, text="Select Input Image", command=self.load_input_image)
        self.input_button.pack(pady=10)

        self.filter_buttons = [
            tk.Button(master, text = "Grayscale", command=self.apply_filter("grayscale")),
            tk.Button(master, text="Blur", command=self.apply_filter("blur")),
            tk.Button(master, text="Canny Edges", command=self.apply_filter("canny")),
        ]
        for button in self.filter_buttons:
            button.pack(padx=10, pady=5)

        self.save_button = tk.Button(master, text="Save Output Images", command=self.save_output_images)
        self.save_button.pack(pady=10)

    def load_input_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.input_image = cv2.imread(file_path)
            self.show_image(self.input_image)

    def apply_filter(self, filter_name):
        def callback():
            if self.input_image is not None:
                if filter_name == "grayscale":
                    output_image = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
                elif filter_name == "blur":
                    output_image = cv2.GaussianBlur(self.input_image, (11, 11), 0)
                elif filter_name == "canny":
                    output_image = cv2.Canny(self.input_image, 30, 150)
                self.output_images[filter_name] = output_image
                self.show_image(output_image)
        return callback

    def save_output_images(self):
        for filter_name, image in self.output_images.items():
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
            if file_path:
                cv2.imwrite(file_path, image)

    def show_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels = image.shape
        ratio = height / width
        if height > 500 or width > 500:
            if ratio > 1:
                height = 500
                width = int(height / ratio)
            else:
                width = 500
                height = int(width * ratio)
        image = cv2.resize(image, (width, height))
        image = tk.PhotoImage(data=cv2.imencode('.png', image)[1].tobytes())
        if hasattr(self, 'image_label'):
            self.image_label.configure(image=image)
            self.image_label.image = image
        else:
            self.image_label = tk.Label(self.master, image=image)
            self.image_label.pack(padx=10, pady=10)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("500x500")
    app = ImageFilterApp(root)
    root.mainloop()
