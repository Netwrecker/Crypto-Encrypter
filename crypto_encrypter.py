import os
from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
      
def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def browse_files():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("All files", "*.*"),))
    label_file_explorer.configure(text="File Opened: " + filename)

def encrypt_button():
    key = load_key()
    encrypt_file(entry_file_path.get(), key)
    messagebox.showinfo("Encryption", "File encrypted successfully.")

def decrypt_button():
    key = load_key()
    decrypt_file(entry_file_path.get(), key)
    messagebox.showinfo("Decryption", "File decrypted successfully.")

window = Tk()
window.title("Encryption/Decryption App")
window.geometry("700x350")

label_file_explorer = Label(window, text="File Explorer using Tkinter", width=100, height=4, fg="blue")
label_file_explorer.grid(column=1, row=1)

button_explore = Button(window, text="Browse Files", command=browse_files)
button_explore.grid(column=1, row=2)

button_encrypt = Button(window, text="Encrypt", command=encrypt_button)
button_encrypt.grid(column=1, row=3)

button_decrypt = Button(window, text="Decrypt", command=decrypt_button)
button_decrypt.grid(column=1, row=4)

entry_file_path = Entry(window, width=100)
entry_file_path.grid(column=1, row=5)

window.mainloop()

if __name__ == "__main__":
    generate_key()
    window.mainloop()
