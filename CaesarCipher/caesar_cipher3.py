import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if mode == "encrypt":
                if char.islower():
                    new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
                else:
                    new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            elif mode == "decrypt":
                if char.islower():
                    new_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
                else:
                    new_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
            result += new_char
        else:
            result += char
    return result

def on_encrypt():
    input_text = input_textbox.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, caesar_cipher(input_text, shift, "encrypt"))

def on_decrypt():
    input_text = input_textbox.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, caesar_cipher(input_text, shift, "decrypt"))

def remove_punctuation():
    input_text = input_textbox.get("1.0", "end-1c")
    input_textbox.delete("1.0", tk.END)
    input_textbox.insert(tk.END, ''.join(e for e in input_text if e.isalnum() or e.isspace()))

def remove_spaces():
    input_text = input_textbox.get("1.0", "end-1c")
    input_textbox.delete("1.0", tk.END)
    input_textbox.insert(tk.END, input_text.replace(" ", ""))

root = tk.Tk()
root.title("Caesar Cipher Tool")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# ttk.Label(frame, text="Caesar Cipher").grid(row=0, column=0, sticky=tk.W)
# ttk.Label(frame, text="shift cipher").grid(row=1, column=0, sticky=tk.W)
ttk.Label(frame, text="<III III III III III III III III I \n \I III III III III III III III III").grid(row=0, column=1, sticky=tk.E)
ttk.Label(frame, text="(^_^)Ludwig NGC7023").grid(row=0, column=1, sticky=tk.E)
ttk.Label(frame, text="Pa pz dypaalu pu jvkl~").grid(row=10, column=1, sticky=tk.N)

style = ttk.Style()
style.configure("Rounded.TEntry", borderwidth=10, relief="groove", background="white")

input_label = ttk.Label(frame, text="----Input Text:")
input_label.grid(row=0, column=0, sticky=tk.W)
input_textbox = tk.Text(frame, width=40, height=5)
input_textbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

shift_label = ttk.Label(frame, text="1~25-Shift:")
shift_label.grid(row=2, column=0, sticky=tk.W)
shift_entry = ttk.Entry(frame, width=10, style="Rounded.TEntry")
shift_entry.grid(row=2, column=0, sticky=tk.E)

output_label = ttk.Label(frame, text="----Output Text:")
output_label.grid(row=3, column=0, sticky=tk.W)
output_textbox = tk.Text(frame, width=40, height=5)
output_textbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

encrypt_button = ttk.Button(frame, text="Encrypt", command=on_encrypt)
encrypt_button.grid(row=5, column=0, pady=5)
decrypt_button = ttk.Button(frame, text="Decrypt", command=on_decrypt)
decrypt_button.grid(row=5, column=1, pady=5)
remove_punctuation_button = ttk.Button(frame, text="Remove Punctuation", command=remove_punctuation)
remove_punctuation_button.grid(row=6, column=0, pady=5)
remove_spaces_button = ttk.Button(frame, text="Remove Spaces", command=remove_spaces)
remove_spaces_button.grid(row=6, column=1, pady=5)

style = ttk.Style()
style.configure('TEntry', borderwidth=10, relief='groove')
style.configure('TText', borderwidth=10, relief='groove')

def open_encryption_window():
    def copy_to_clipboard(text):
        root.clipboard_clear()
        root.clipboard_append(text)

    def display_encryptions():
        for i in range(1, 26):
            encrypted_text = caesar_cipher(entry_text.get(), i, "encrypt")
            labels[i-1].config(text=f"Shift {i}")
            entry_boxes[i-1].delete(0, tk.END)
            entry_boxes[i-1].insert(0, encrypted_text)

    root = tk.Toplevel()
    root.title("Super Encryption Windows")
    root.attributes('-alpha', 0.9)  # 设置窗口透明度为90%

    None_label = ttk.Label(root, text="III III III \n III III III")
    None_label.grid(row=4, column=12, padx=10, pady=0)
    None_label = ttk.Label(root, text="(^_^)")
    None_label.grid(row=4, column=12, padx=10, pady=0)
    None_label2 = ttk.Label(root, text="III III III \n III III III")
    None_label2.grid(row=5, column=12, padx=10, pady=0)
    None_label2 = ttk.Label(root, text="Use all shift")
    None_label2.grid(row=5, column=12, padx=10, pady=0)

    entry_label = ttk.Label(root, text="Enter text to encrypt:")
    entry_label.grid(row=0, column=12, padx=10, pady=10)

    entry_text = tk.StringVar()
    entry = ttk.Entry(root, textvariable=entry_text)
    entry.grid(row=1, column=12, padx=10, pady=10)

    encrypt_button = ttk.Button(root, text="Encrypt", command=display_encryptions)
    encrypt_button.grid(row=2, column=12, columnspan=2, pady=10)

    labels = []
    entry_boxes = []
    for i in range(25):
        label = ttk.Label(root, text="")
        label.grid(row=(i//5)*2 + 2, column=(i % 5)*2+3, padx=10, pady=5)
        labels.append(label)

        entry_box = ttk.Entry(root)
        entry_box.grid(row=(i//5)*2 + 3, column=(i % 5)*2 + 3, padx=10, pady=5)
        entry_boxes.append(entry_box)

    root.mainloop()

# Add this line after the definition of `remove_spaces_button`
open_encryption_window_button = ttk.Button(frame, text="Open Super Encryption Windows", command=open_encryption_window)
open_encryption_window_button.grid(row=9, column=0, columnspan=2, pady=5)

root.mainloop()