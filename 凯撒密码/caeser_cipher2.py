import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            result += new_char
        else:
            result += char
    return result

def on_encrypt():
    input_text = input_textbox.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(input_text, shift)
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, encrypted_text)

def copy_to_clipboard():
    output_textbox.clipboard_clear()
    output_textbox.clipboard_append(output_textbox.get("1.0", "end-1c"))

def on_decrypt():
    encrypted_text = output_textbox.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    decrypted_text = caesar_cipher(encrypted_text, -shift)
    input_textbox.delete("1.0", tk.END)
    input_textbox.insert(tk.END, decrypted_text)

def copy_decrypted_to_clipboard():
    input_textbox.clipboard_clear()
    input_textbox.clipboard_append(input_textbox.get("1.0", "end-1c"))

root = tk.Tk()
root.title("Caesar Cipher")

style = ttk.Style()
style.configure("TFrame", background="white")
style.configure("TLabel", background="white", foreground="black")
style.configure("TButton", background="white", foreground="black")
style.configure("TEntry", background="white", foreground="black")
style.configure("TText", background="white", foreground="black")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

input_label = ttk.Label(frame, text="Input Text:")
input_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
input_textbox = tk.Text(frame, wrap=tk.WORD, width=40, height=10)
input_textbox.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 5))

shift_label = ttk.Label(frame, text="Shift:")
shift_label.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
shift_entry = ttk.Entry(frame)
shift_entry.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 5))

encrypt_button = ttk.Button(frame, text="Encrypt", command=on_encrypt)
encrypt_button.grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
encrypt_button.bind("<Enter>", lambda event: encrypt_button.config(background="#f0f0f0"))
encrypt_button.bind("<Leave>", lambda event: encrypt_button.config(background="white"))
encrypt_button.bind("<Button-1>", lambda event: encrypt_button.config(background="#d0d0d0"))
encrypt_button.bind("<ButtonRelease-1>", lambda event: encrypt_button.config(background="white"))

decrypt_button = ttk.Button(frame, text="Decrypt", command=on_decrypt)
decrypt_button.grid(row=8, column=0, sticky=tk.W, pady=(0, 5))
decrypt_button.bind("<Enter>", lambda event: decrypt_button.config(background="#f0f0f0"))
decrypt_button.bind("<Leave>", lambda event: decrypt_button.config(background="white"))
decrypt_button.bind("<Button-1>", lambda event: decrypt_button.config(background="#d0d0d0"))
decrypt_button.bind("<ButtonRelease-1>", lambda event: decrypt_button.config(background="white"))

copy_button = ttk.Button(frame, text="Copy Encrypted Text", command=copy_to_clipboard)
copy_button.grid(row=5, column=0, sticky=tk.W, pady=(0, 5))
copy_button.bind("<Enter>", lambda event: copy_button.config(background="#f0f0f0"))
copy_button.bind("<Leave>", lambda event: copy_button.config(background="white"))
copy_button.bind("<Button-1>", lambda event: copy_button.config(background="#d0d0d0"))
copy_button.bind("<ButtonRelease-1>", lambda event: copy_button.config(background="white"))

copy_decrypted_button = ttk.Button(frame, text="Copy Decrypted Text", command=copy_decrypted_to_clipboard)
copy_decrypted_button.grid(row=9, column=0, sticky=tk.W, pady=(0, 5))
copy_decrypted_button.bind("<Enter>", lambda event: copy_decrypted_button.config(background="#f0f0f0"))
copy_decrypted_button.bind("<Leave>", lambda event: copy_decrypted_button.config(background="white"))
copy_decrypted_button.bind("<Button-1>", lambda event: copy_decrypted_button.config(background="#d0d0d0"))
copy_decrypted_button.bind("<ButtonRelease-1>", lambda event: copy_decrypted_button.config(background="white"))

output_label = ttk.Label(frame, text="Encrypted Text:")
output_label.grid(row=6, column=0, sticky=tk.W, pady=(0, 5))
output_textbox = tk.Text(frame, wrap=tk.WORD, width=40, height=10)
output_textbox.grid(row=7, column=0, sticky=(tk.W, tk.E), pady=(0, 5))

scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=output_textbox.yview)
scrollbar.grid(row=7, column=1, sticky=(tk.N, tk.S))
output_textbox['yscrollcommand'] = scrollbar.set

root.mainloop()