import tkinter as tk
from tkinter import messagebox

class CaesarCipherApp:
    def __init__(self, master):
        self.master = master
        master.title("Caesar Cipher")
        master.geometry("400x500")
        master.configure(bg='#f0f0f0')

        self.input_label = tk.Label(master, text="Enter Text:", bg='#f0f0f0')
        self.input_label.pack(pady=(20, 5))

        self.input_text = tk.Text(master, height=5, width=50)
        self.input_text.pack(pady=5)
        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt, bg='#4CAF50', fg='white')
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt, bg='#2196F3', fg='white')
        self.decrypt_button.pack(pady=10)

        self.result_label = tk.Label(master, text="Result:", bg='#f0f0f0')
        self.result_label.pack(pady=5)
        self.result_text = tk.Text(master, height=5, width=50)
        self.result_text.pack(pady=5)

        
        self.copy_button = tk.Button(master, text="Copy", command=self.copy_to_clipboard, bg='#FFC107', fg='black')
        self.copy_button.pack(pady=10)

        self.clear_button = tk.Button(master, text="Clear", command=self.clear_fields, bg='#F44336', fg='white')
        self.clear_button.pack(pady=10)

    def caesar_cipher(self, text, shift=3, mode='encrypt'):
        """
        Perform Caesar Cipher encryption or decryption
        """
        result = ""
        if mode == 'decrypt':
            shift = -shift

        for char in text:
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += char

        return result

    def encrypt(self):
        """
        Encrypt the input text using Caesar Cipher
        """
        try:
            text = self.input_text.get("1.0", tk.END).strip()

            if not text:
                messagebox.showerror("Error", "Please enter text to encrypt")
                return

            encrypted_text = self.caesar_cipher(text)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, encrypted_text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt(self):
        """
        Decrypt the input text using Caesar Cipher
        """
        try:
            text = self.input_text.get("1.0", tk.END).strip()

            if not text:
                messagebox.showerror("Error", "Please enter text to decrypt")
                return

            decrypted_text = self.caesar_cipher(text, mode='decrypt')
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, decrypted_text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        """
        Copy the result text to the clipboard
        """
        try:
            result_text = self.result_text.get("1.0", tk.END).strip()
            if not result_text:
                messagebox.showinfo("Info", "No text to copy")
                return
            self.master.clipboard_clear()
            self.master.clipboard_append(result_text)
            self.master.update()  # Necessary to store in the clipboard
            messagebox.showinfo("Success", "Copied to clipboard")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_fields(self):
        """
        Clear the input and result text fields
        """
        self.input_text.delete("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)

def main():
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
