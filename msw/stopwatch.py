import tkinter as tk
from datetime import datetime
class Stopwatch:
    def __init__(self, master, label="", elapsed_time=0, running=False):
        self.master = master        
        self.label = label
        self.running = False
        self.elapsed_time = elapsed_time
        self.last_time = datetime.now().timestamp() if running else 0
        self.create_widgets()
        if running:
            self.resume()    
            self.update_timer()


    def create_widgets(self):
        self.frame = tk.Frame(self.master, padx=5, pady=5, bg='lightgray')
        self.label_entry = tk.Entry(self.frame, bg='white')
        self.label_entry.insert(0, self.label)
        self.time_display = tk.Label(self.frame, text="00:00:00", font=('Helvetica', 16), fg='black', bg='lightgray')
        self.start_button = tk.Button(self.frame, text='Start', command=self.start)
        self.pause_button = tk.Button(self.frame, text='Pause', command=self.pause)
        self.resume_button = tk.Button(self.frame, text='Resume', command=self.resume)
        self.reset_button = tk.Button(self.frame, text='Reset', command=self.reset)
        self.label_entry.pack(side=tk.TOP, fill=tk.X)
        self.time_display.pack(side=tk.TOP)
        self.start_button.pack(side=tk.LEFT)
        self.pause_button.pack(side=tk.LEFT)
        self.resume_button.pack(side=tk.LEFT)
        self.reset_button.pack(side=tk.LEFT)
        self.frame.pack(side=tk.TOP, fill=tk.X)

    def update_timer(self):
        if self.running:
            delta = datetime.now().timestamp() - self.last_time
            self.elapsed_time += delta
            self.last_time = datetime.now().timestamp()
            self.display_time()
            self.master.after(50, self.update_timer)

    def display_time(self):
        t = int(self.elapsed_time)
        hours, remainder = divmod(t, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.time_display.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

    def start(self):
        if not self.running:
            self.running = True
            self.last_time = datetime.now().timestamp()
            self.update_timer()

    def pause(self):
        self.running = False

    def resume(self):
        if not self.running:
            self.running = True
            self.last_time = datetime.now().timestamp()
            self.update_timer()

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.display_time()