import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from calculatebmr import calculate_bmr
from calculate_daily_calories import calculate_daily_calories

def open_calorie_window(username):
    def on_calculate():
        try:
            weight_str = weight_var.get().strip()
            height_str = height_var.get().strip()
            age_str = age_var.get().strip()
            sex = sex_var.get()
            activity = activity_var.get()

            print(f"Weight entered: {weight_str}")
            print(f"Height entered: {height_str}")
            print(f"Age entered: {age_str}")
            print(f"Sex selected: {sex}")
            print(f"Activity level selected: {activity}")

            if not weight_str or not height_str or not age_str:
                result_label.config(text="Please fill in all numeric fields.")
                return

            weight = float(weight_str)
            height = float(height_str)
            age = int(age_str)

            bmr = calculate_bmr(weight, height, age, sex)
            if bmr is None:
                result_label.config(text="Please select 'male' or 'female' for sex.")
                return

            result = f"BMR: {bmr:.2f} calories/day"
            daily_claorie_intake = calculate_daily_calories(bmr, activity)
            result2 = f"The threshold amount is: {daily_claorie_intake:.2f} calories/day"

            combined_result = f"{result}\n{result2}"
            result_label.config(text=combined_result)

                        

        except ValueError as e:
            print(f"ValueError: {e}")
            result_label.config(text="Please enter valid numeric values.")

    # Use Toplevel instead of a new root window
    win = tk.Toplevel()
    win.title(f"Welcome {username} - Calories Calculator")
    win.state('zoomed')
    win.bind("<Escape>", lambda e: win.attributes("-fullscreen", False))

    # Apply ttkbootstrap theme
    style = ttk.Style("flatly")

    ttk.Label(win, text=f"Hello {username}!", font=("Helvetica", 20)).pack(pady=20)
    ttk.Label(win, text="Enter your details below to calculate BMR", font=("Helvetica", 14)).pack(pady=10)

    frame = ttk.Frame(win, padding=20)
    frame.pack()

    weight_var = tk.StringVar()
    height_var = tk.StringVar()
    age_var = tk.StringVar()
    sex_var = tk.StringVar(value="male")
    activity_var = tk.StringVar(value="sedentary")

    fields = [
        ("Weight (kg)", weight_var),
        ("Height (cm)", height_var),
        ("Age", age_var),
    ]

    for label, var in fields:
        ttk.Label(frame, text=label).pack(anchor='w', padx=10, pady=(10, 0))
        ttk.Entry(frame, textvariable=var).pack(fill='x', padx=10)

    ttk.Label(frame, text="Sex").pack(anchor='w', padx=10, pady=(10, 0))
    sex_frame = ttk.Frame(frame)
    sex_frame.pack(anchor='w', padx=10)
    ttk.Radiobutton(sex_frame, text="Male", variable=sex_var, value="male").pack(side='left', padx=5)
    ttk.Radiobutton(sex_frame, text="Female", variable=sex_var, value="female").pack(side='left', padx=5)

    ttk.Label(frame, text="Activity Level").pack(anchor='w', padx=10, pady=(10, 0))
    activity_frame = ttk.Frame(frame)
    activity_frame.pack(anchor='w', padx=10)

    activity_levels = [
        ("Sedentary", "sedentary"),
        ("Lightly active", "lightly active"),
        ("Moderately active", "moderately active"),
        ("Very active", "very active"),
    ]

    for text, value in activity_levels:
        ttk.Radiobutton(activity_frame, text=text, variable=activity_var, value=value).pack(side='left', padx=5)

    ttk.Button(frame, text="Calculate BMR", command=on_calculate, bootstyle=SUCCESS).pack(pady=20)

    result_label = ttk.Label(frame, text="", font=("Helvetica", 12))
    result_label.pack(pady=10)

    win.mainloop()
