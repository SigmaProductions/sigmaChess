from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
        )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        self.photo = PhotoImage(file="stulejka.gif")

        w=Canvas(master,width=self.photo.width(),height=self.photo.height())
        w.pack()


        w.create_image(100,100,image=self.photo)

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below