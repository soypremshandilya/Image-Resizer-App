from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from PIL import Image

def resize_image():
    width = width_entry.get()
    height = height_entry.get()

    try:
        width = int(width)
        height = int(height)
    except ValueError:
        messagebox.showerror("Invalid Input", "Width and height must be integers.")
        return

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff")]
    )
    if not file_path:
        return

    try:
        with Image.open(file_path) as img:
            img_resized = img.resize((width, height))

            save_path = filedialog.asksaveasfilename(
                title="Save Resized Image",
                defaultextension=".png",
                filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg;*.jpeg"), ("All Files", "*.*")]
            )
            if save_path:
                img_resized.save(save_path)
                messagebox.showinfo("Success", f"Image resized and saved at: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to resize image: {e}")

root = Tk()
root.title("Prem's Image Resizer")

Label(root, text="Width:").grid(row=0, column=0, padx=20, pady=20)
width_entry = Entry(root)
width_entry.grid(row=0, column=1, padx=20, pady=20)

Label(root, text="Height:").grid(row=1, column=0, padx=20, pady=20)
height_entry = Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

resize_button = Button(root, text="Resize Image", command=resize_image)
resize_button.grid(row=2, column=0, columnspan=2, pady=40)

root.mainloop()
