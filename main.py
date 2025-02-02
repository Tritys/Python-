import tkinter as tk
from app import PythonAdventuresApp

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = PythonAdventuresApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Произошла ошибка: {e}")