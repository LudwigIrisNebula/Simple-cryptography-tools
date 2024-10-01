import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            result += new_char
        else:
            result += char
    return result

def on_encrypt():
    input_text = input_entry.get()
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(input_text, shift)
    result_label.delete("1.0", tk.END)
    result_label.insert(tk.END, "Encrypted Text: " + encrypted_text)
    shifted_alphabets = ' '.join(chr(i) for i in range(ord('A'), ord('Z')+1))
    shifted_alphabet_label.config(text="Shifted Alphabets: " + shifted_alphabets)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.get("1.0", tk.END))

root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("800x600")

# Create a label to display the alphabets
alphabet_label = tk.Label(root, text="Alphabets: " + ' '.join(chr(i) for i in range(ord('a'), ord('z')+1)))
alphabet_label.pack(side=tk.TOP, anchor=tk.W)

# Create a label to display the shifted alphabets
shifted_alphabet_label = tk.Label(root, text="Shifted Alphabets: " + ' '.join(chr(i) for i in range(ord('A'), ord('Z')+1)))
shifted_alphabet_label.pack(side=tk.TOP, anchor=tk.W)

input_label = tk.Label(root, text="Input Text:")
input_label.pack()
input_entry = tk.Entry(root)
input_entry.pack()

shift_label = tk.Label(root, text="Shift:")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.pack()

scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_label = tk.Text(root, wrap=tk.WORD, yscrollcommand=scrollbar.set)
result_label.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=result_label.yview)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()
