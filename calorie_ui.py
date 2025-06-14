import ttkbootstrap as ttk

def open_calorie_window(username):
    win = ttk.Window(themename="flatly")
    win.title(f"Welcome {username} - Calories Calculator")
    win.state('zoomed')
    win.bind("<Escape>", lambda e: win.attributes("-fullscreen", False))

    ttk.Label(win, text=f"Hello {username}!", font=("Helvetica", 20)).pack(pady=30)
    ttk.Label(win, text="This is your calorie calculator homepage.", font=("Helvetica", 14)).pack(pady=10)
    ttk.Label(win, text="(You can add API integration and search here)", font=("Helvetica", 12, "italic")).pack(pady=20)
