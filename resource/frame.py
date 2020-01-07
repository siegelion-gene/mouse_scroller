import time
import tkinter as tk
from pynput.mouse import Button, Controller
from resource.myThread import MyThread

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.m = Controller()
        # self.t = threading.Thread(target=self.scroll, name='LoopThread')
        self.t = MyThread(target=self.scroll)

    def create_widgets(self):
        start_button = tk.Button(self, text="start", command=self.start)
        start_button.pack(side="top")
        pause_button = tk.Button(self, text="pause", command=self.pause)
        pause_button.pack(side="top")
        quit_button = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        quit_button.pack(side="bottom")

    def scroll(self):
        time.sleep(1)
        self.m.scroll(0, -100)

    def start(self):
        if self.t.is_alive():
            self.t.resume()
        else:
            self.t.start()

    def pause(self):
        self.t.pause()
        print("paused")


