import tkinter as tk
from tkinter import simpledialog

def encrypt(text, key):
    if not isinstance(text, str) or not text:
        print("Invalid input: 'text' must be a non-empty string")
        raise ValueError("Invalid input: 'text' must be a non-empty string")
    if not isinstance(key, int) or key <= 0:
        print("Invalid input: 'key' must be a positive integer")
        raise ValueError("Invalid input: 'key' must be a positive integer")
    if key > len(text):
        print("Invalid input: 'key' must be less than or equal to the length of 'text'")
        raise ValueError("Invalid input: 'key' must be less than or equal to the length of 'text'")
    
    columns = [[] for _ in range(key)]

    for i, char in enumerate(text): 
        row = i % key
        columns[row].append(char)

    return ''.join(''.join(column) for column in columns)

def decrypt(cipher, key):
    if key == 0:
        raise ValueError("Key cannot be zero")
    
    num_rows = len(cipher) // key
    num_cols = num_rows + (1 if len(cipher) % key else 0)

    result = [''] * num_cols
    idx = 0

    for row in range(key):
        for col in range(num_cols):
            if idx < len(cipher):
                result[col] += cipher[idx]
                idx += 1
    return ''.join(result)

def handle_action(action):
    try:
        user_text = text_input.get("1.0", "end-1c").strip()
        encryption_key = int(key_input.get().strip())
        print(f"User Text: {user_text}, Key: {encryption_key}")#可省略

        if action == "encrypt":
            result_text.config(state=tk.NORMAL)
            result_text.delete("1.0", tk.END)
            encrypted_text = encrypt(user_text, encryption_key)
            result_text.insert(tk.END, encrypted_text)
            result_text.config(state=tk.DISABLED)

        elif action == "decrypt":
            result_text.config(state=tk.NORMAL)
            result_text.delete("1.0", tk.END)
            decrypted_text = decrypt(user_text, encryption_key)
            result_text.insert(tk.END, decrypted_text)
            result_text.config(state=tk.DISABLED)

    except ValueError as e:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, str(e))
        result_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Fence Cipher Tool")

tk.Label(root, text="Enter Text:").grid(row=0, column=0, sticky=tk.W)
text_input = tk.Text(root, height=5, width=40)
text_input.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

tk.Label(root, text="Enter Key:").grid(row=2, column=0, sticky=tk.W)
key_input = tk.Entry(root)
key_input.grid(row=2, column=1, padx=10, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=lambda: handle_action("encrypt"))
encrypt_button.grid(row=3, column=0, padx=10, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=lambda: handle_action("decrypt"))
decrypt_button.grid(row=3, column=1, padx=10, pady=5)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, sticky=tk.W)

result_text = tk.Text(root, height=5, width=40, state=tk.DISABLED)
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()