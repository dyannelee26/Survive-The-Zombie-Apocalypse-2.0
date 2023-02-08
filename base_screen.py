from tkinter import * 
from tkinter import ttk
from tkinter.ttk import Progressbar
import time
  
class BaseScreen(Frame):
    def __init__(self, master):
        super(BaseScreen, self).__init__(master)
        self.grid()
        self.create_widgets()

    
    def create_widgets(self):
        health = ttk.Style()
        health.theme_use('default')
        health.configure("health.Horizontal.TProgressbar", background='#00FF2B')
        
        supplies = ttk.Style()
        supplies.theme_use('default')
        supplies.configure("supplies.Horizontal.TProgressbar", background='#00FF2B')


        bar = Progressbar(self, length=300, style='health.Horizontal.TProgressbar')
        bar['value'] = 95
        Label(self, text="Health", font="Ariel 10").grid(row=1, column=0, padx=6.5, sticky=W)
        bar.grid(column=0, row=0, padx = 10, pady=(10, 0), sticky=S)

        bar2 = Progressbar(self, length=300, style='supplies.Horizontal.TProgressbar')
        bar2['value'] = 100
        Label(self, text="Supplies", font="Ariel 10").grid(row=3, column=0, padx=6.5, sticky=W)
        bar2.grid(column=0, row=2, padx = 10, sticky=W)

        bar2.start(5000)

    def quit_game(self):
        self.destroy()

root = Tk()
root.title("Base")
root.geometry("1250x750")
app = BaseScreen(root)
root.mainloop()