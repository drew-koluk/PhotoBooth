import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def openCamera():
    print("this worked")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Photobooth")
        self.geometry('500x500')
        self.create_widgets()


    def create_widgets(self):
        self.hello_label = tk.Label(self,text="Welcome To the Photo Booth")
        self.hello_label.pack()

        self.open_camera = tk.Button(self, text="Open Camera Frame", command=openCamera)
        self.open_camera.pack()

        self.button = tk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        showinfo(title='Information', message='Hello, Tkinter!')


if __name__ == "__main__":
    app = App()
    app.mainloop()
 
    