import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import threading
from Camera import openCamera
from Camera import takephoto

#tCAM is a random name, feel free to change it to whatever. its just the threading for the opencamera code
def tCAM():
    threading.Thread(target=openCamera,daemon=True).start()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Photobooth")
        self.geometry('500x500')
        self.create_widgets()


    def create_widgets(self):
        self.hello_label = tk.Label(self,text="Welcome To the Photo Booth")
        self.hello_label.pack()

        self.open_camera = tk.Button(self, text="Open Camera Frame", command=tCAM)
        self.open_camera.pack()

        self.Take_Picture = tk.Button(self, text="Take A Photo!", command=takephoto)
        self.Take_Picture.pack()

        self.button = tk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()


    def button_clicked(self):
        showinfo(title='Information', message='Hello, Tkinter!')


if __name__ == "__main__":
    app = App()
    app.mainloop()


 