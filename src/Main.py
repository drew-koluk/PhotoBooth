import tkinter as tk


print(tk.TkVersion)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        # Add your widgets here
        self.hello_label = tk.Label(self, text="Hello, Tkinter!")
        self.hello_label.pack()

        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("My Tkinter App")
    app = Application(master=root)
    app.mainloop()