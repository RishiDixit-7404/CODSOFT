import tkinter as tk
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("650x550")

        self.label = tk.Label(root, text="Enter password length:")
        self.label.configure(font="helvetica 30 bold")
        self.label.pack(pady=10)

        self.length_entry = tk.Entry(root)
        self.length_entry.configure(font="helvetica 30 bold")
        self.length_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.configure(font="helvetica 30 bold")
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(root, text="")
        self.password_label.configure(font="helvetica 30 italic")
        self.password_label.pack()

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
            if password_length <= 0:
                self.password_label.config(text="Enter a positive password length.")
            else:
                password = self.generate_random_password(password_length)
                self.password_label.config(text="Generated Password: " + password)
        except ValueError:
            self.password_label.config(text="Enter a valid integer for password length.")

    def generate_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()