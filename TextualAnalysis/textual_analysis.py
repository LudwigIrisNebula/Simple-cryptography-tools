import tkinter as tk
from tkinter import Toplevel, Text, Button
import matplotlib.pyplot as plt
from collections import Counter
import string
from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

class FrequencyAnalyzer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Frequency Analyzer")
        self.window.geometry("400x220")
        self.window.attributes('-alpha', 0.9)

        label = tk.Label(self.window, text="input")
        label.pack()

        self.entry = tk.Entry(self.window,width=50)
        self.entry.pack()

        label2 = tk.Label(self.window, text="Consecutive character analysis")
        label2.pack()

        self.entry2 = tk.Entry(self.window,width=7)
        self.entry2.pack()

        analyze_button = tk.Button(self.window, text="Letter frequency analysis", command=self.show_analysis)
        analyze_button.pack()
        analyze2_button = tk.Button(self.window, text="Word frequency analysis", command=self.show_analysis2)
        analyze2_button.pack()
        world_freq_button = tk.Button(self.window, text="World Letter frequency analysis", command=self.show_world_frequency)
        world_freq_button.pack()
        consecutive_button = tk.Button(self.window, text="Consecutive character analysis", command=self.show_consecutive_analysis)
        consecutive_button.pack()

        self.window.mainloop()

    def show_analysis(self):
        input_value = self.entry.get()
        letter_freq = Counter(input_value.replace(" ", "").lower())
        all_letters = {letter: 0 for letter in string.ascii_lowercase}
        all_letters.update(letter_freq)
        letters, counts = zip(*all_letters.items())
        plt.figure(figsize=(10,2),dpi=75)
        plt.bar(letters, counts, color='silver',linestyle="--",alpha=0.5)
        plt.title("Letter frequency analysis")
        plt.xlabel("letter")
        plt.ylabel("frequency")
        plt.grid(True,linestyle='--',alpha=0.5)
        plt.show()

    def show_analysis2(self):
        input_value = self.entry.get()
        word_freq = Counter(input_value.split())
        words, counts = zip(*word_freq.items())
        plt.figure(figsize=(10,2),dpi=75)
        plt.bar(words, counts,color="silver",linestyle="--",alpha=0.5,label="Ludwig NGC7023")
        plt.title("Word frequency analysis")
        plt.xlabel("word")
        plt.ylabel("frequency")
        plt.grid(True,linestyle='--',alpha=0.5)
        plt.show()

    def show_world_frequency(self):
        world_freq = {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074}
        letters, counts = zip(*world_freq.items())
        plt.figure(figsize=(10,2),dpi=75)
        plt.bar(letters, counts,color='silver',linestyle="--",alpha=0.5)
        plt.title("World Letter frequency analysis")
        plt.xlabel("letter")
        plt.ylabel("frequency")
        plt.grid(True,linestyle='--',alpha=0.5)
        plt.show()

    def show_consecutive_analysis(self):
        n = int(self.entry2.get())
        input_value = self.entry.get()
        consecutive_chars = [input_value[i:i+n] for i in range(len(input_value) - n + 1)]
        consecutive_freq = Counter(consecutive_chars)
        pairs, counts = zip(*consecutive_freq.items())
        plt.figure(figsize=(10,2),dpi=75)
        plt.bar(pairs, counts, color='silver',linestyle="--",alpha=0.5)
        plt.title("Consecutive character analysis")
        plt.xlabel("character pair")
        plt.ylabel("frequency")
        plt.grid(True,linestyle='--',alpha=0.5)
        plt.show()

if __name__ == "__main__":
    FrequencyAnalyzer()
