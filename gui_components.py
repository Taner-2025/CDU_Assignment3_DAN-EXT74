# gui_components.py

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from model_handlers import ModelFactory
from model_info import get_model_info
from oop_explanations import get_oop_explanations
class BaseGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter AI GUI")
        self.geometry("900x600")
        self.configure(bg="#f0f0f0")

class AIApp(BaseGUI):
    def __init__(self):
        super().__init__()
        self.model_type = tk.StringVar()
        self.input_type = tk.StringVar()
        self.input_data = None
        self.create_widgets()

    def create_widgets(self):
        # Model Selection
        ttk.Label(self, text="Model Selection:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        model_dropdown = ttk.Combobox(self, textvariable=self.model_type, values=["Text-to-Image", "Image Classification"])
        model_dropdown.grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(self, text="Load Model", command=self.load_model).grid(row=0, column=2, padx=10)

        # Input Type
        ttk.Label(self, text="Input Type:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        ttk.Radiobutton(self, text="Text", variable=self.input_type, value="text").grid(row=1, column=1)
        ttk.Radiobutton(self, text="Image", variable=self.input_type, value="image").grid(row=1, column=2)

        # Input Area
        self.input_text = tk.Text(self, height=5, width=60)
        self.input_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        ttk.Button(self, text="Browse", command=self.browse_file).grid(row=2, column=3, padx=10)

        # Run Buttons
        ttk.Button(self, text="Run Model 1", command=lambda: self.run_model("model1")).grid(row=3, column=0, padx=10)
        ttk.Button(self, text="Run Model 2", command=lambda: self.run_model("model2")).grid(row=3, column=1, padx=10)

        # Output Display
        ttk.Label(self, text="Output Display:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.output_display = tk.Text(self, height=10, width=80)
        self.output_display.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

        # Model Info
        ttk.Label(self, text="Selected Model Info:").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.model_info_display = tk.Text(self, height=5, width=80)
        self.model_info_display.grid(row=7, column=0, columnspan=4, padx=10, pady=10)

        # OOP Explanation
        ttk.Label(self, text="OOP Concepts Explanation:").grid(row=8, column=0, padx=10, pady=10, sticky="w")
        self.oop_display = tk.Text(self, height=5, width=80)
        self.oop_display.grid(row=9, column=0, columnspan=4, padx=10, pady=10)
        self.oop_display.insert(tk.END, get_oop_explanations())

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.input_data = file_path
        self.input_text.delete("1.0", tk.END)
        self.input_text.insert(tk.END, file_path)

    def load_model(self):
        model_info = get_model_info(self.model_type.get())
        self.model_info_display.delete("1.0", tk.END)
        self.model_info_display.insert(tk.END, model_info)

    def run_model(self, model_key):
        input_value = self.input_text.get("1.0", tk.END).strip()
        handler = ModelFactory.get_model_handler(self.model_type.get())
        if handler:
            result = handler.run(input_value, model_key, self.input_type.get())
            self.output_display.delete("1.0", tk.END)
            self.output_display.insert(tk.END, result)
        else:
            messagebox.showerror("Error", "Model handler not found.")

