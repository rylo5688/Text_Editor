import Tkinter

class Message(object):
    def __init__(self, string):
        self.page = Tkinter.Tk()
        self.page.title('Message')

        #setting the page geometry
        self.page.geometry('200x400')

        #displaying the message
        self.text = Tkinter.Text(self.page, background='white', foreground='black', font=('Arial', 12))
        self.text.insert(0.0, string)
        self.text.pack()

    def displayMsg(self):
        self.page.mainloop()
