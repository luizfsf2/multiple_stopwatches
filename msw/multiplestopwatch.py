import json
import tkinter as tk
from msw.stopwatch import Stopwatch

class MultiStopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Multi-Stopwatch Application')        
        self.stopwatches = []
        self.load_state()
        self.init_ui()
        self.autosave_interval = 60000  # 60 seconds
        self.autosave()

    def init_ui(self):
        self.control_frame = tk.Frame(self.master, padx=5, pady=5)
        self.add_button = tk.Button(self.control_frame, text='Add Stopwatch', command=self.add_stopwatch)
        self.save_button = tk.Button(self.control_frame, text='Save All', command=self.save_state)
        self.add_button.pack(side=tk.LEFT)
        self.save_button.pack(side=tk.LEFT)
        self.control_frame.pack(side=tk.TOP, fill=tk.X)

    def add_stopwatch(self):
        label = f"Stopwatch {len(self.stopwatches) + 1}"
        stopwatch = Stopwatch(self.master, label)
        self.stopwatches.append(stopwatch)

    def save_state(self):
        try:
            data = [{'label': sw.label_entry.get(), 'elapsed_time': sw.elapsed_time, 'running': sw.running} for sw in self.stopwatches]
            with open('stopwatches_state.json', 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Failed to save state: {e}")

    def load_state(self):
        try:
            with open('stopwatches_state.json', 'r') as f:
                data = f.read()
                if data:
                    data = json.loads(data)
                    for item in data:
                        stopwatch = Stopwatch(self.master, item['label'], item['elapsed_time'], item['running'])
                        self.stopwatches.append(stopwatch)
                        if item['running']:
                            stopwatch.resume()
        except FileNotFoundError:
            pass

    def autosave(self):
        self.save_state()
        self.master.after(self.autosave_interval, self.autosave)