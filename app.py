from db import init_db
import ttkbootstrap as ttk
from auth_ui import AuthApp

def main():
    init_db()
    root = ttk.Window(themename="flatly")
    AuthApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
