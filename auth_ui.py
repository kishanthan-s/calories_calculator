import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from services.auth_service import authenticate, register
from calorie_ui import open_calorie_window

class AuthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calories Calculator - Login")
        self.root.state('zoomed')
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))
        self.frame = ttk.Frame(root, padding=40)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.mode = 'login'
        self.build_form()

    def build_form(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        ttk.Label(self.frame, text="Calories Calculator", font=("Helvetica", 24, "bold")).pack(pady=20)
        ttk.Label(self.frame, text="Username", font=("Helvetica", 12)).pack(anchor="w", padx=10)
        self.username_entry = ttk.Entry(self.frame, width=40)
        self.username_entry.pack(pady=5)

        ttk.Label(self.frame, text="Password", font=("Helvetica", 12)).pack(anchor="w", padx=10)
        self.password_entry = ttk.Entry(self.frame, show="*", width=40)
        self.password_entry.pack(pady=5)

        action_text = "Login" if self.mode == 'login' else "Sign Up"
        ttk.Button(self.frame, text=action_text, bootstyle=PRIMARY, command=self.login_or_signup).pack(pady=15)

        switch_text = "Don't have an account? Sign Up" if self.mode == 'login' else "Already have an account? Login"
        ttk.Button(self.frame, text=switch_text, bootstyle=LINK, command=self.switch_mode).pack()

    def switch_mode(self):
        self.mode = 'signup' if self.mode == 'login' else 'login'
        self.build_form()

    def login_or_signup(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Please enter username and password.")
            return

        if self.mode == 'login':
            if authenticate(username, password):
                messagebox.showinfo("Success", f"Welcome, {username}!")
                self.root.withdraw()
                open_calorie_window(username)
            else:
                messagebox.showerror("Login Failed", "Invalid credentials.")
        else:
            if register(username, password):
                messagebox.showinfo("Success", "Account created. You can log in now.")
                self.switch_mode()
            else:
                messagebox.showerror("Error", "Username already exists.")
