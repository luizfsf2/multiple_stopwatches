import tkinter as tk
from msw.multiplestopwatch import MultiStopwatchApp

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiStopwatchApp(root)
    root.mainloop()