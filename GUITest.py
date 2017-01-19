import Tkinter

def onKeyPress(event):
    text.insert('insert', '%s' % (event.char, ))
    content.append(event.char)

class createPage(object):
    def save(object): #runs when the save button is clicked
        newContents = object.text.get(0.0, 'end') #gets all the contents from the text widget
        uFile = open(object.file + ".txt", "w+") #opens the file in writing mode
        #add functionality where user saves as a new file
        #if they didn't open one to begin with
        uFile.write(newContents) #writing out the contents from the text widget to the file
        uFile.close()

    def saveExit(object): #runs when the save and exit button is clicked
        newContents = object.text.get(0.0, 'end') #gets all the contents from the text widget
        uFile = open(object.file + ".txt", "w+") #opens the file in writing mode
        #add functionality where user saves as a new file
        #if they didn't open one to begin with
        uFile.write(newContents) #writing out the contents from the text widget to the file
        uFile.close()
        object.page.destroy() #closes the text widget

    def __init__(self, fileName):
        self.page = Tkinter.Tk()
        self.page.title(fileName)
        self.page.geometry('450x450')
        #containter for the button
        self.page.buttonframe = Tkinter.Frame(self.page)
        self.page.buttonframe.grid(row=0, column=1)

        #save button
        self.bSave = Tkinter.Button(self.page.buttonframe, text="Save", command=self.save).grid(row=0, column=0)

        #save and exit button
        self.bSaveAndExit = Tkinter.Button(self.page.buttonframe, text="Save and Exit", command=self.saveExit).grid(row=0,column=1)

        self.page.buttonframe.pack(fill='x')

        self.text = Tkinter.Text(self.page, background='white', foreground='black', font=('Comic Sans MS', 12))

        #later add functionality for only opening
        #when there's a specified file to open
        uFileContents = "" #contents already in the file
        self.uFile = open(fileName + ".txt", "r+")#opening a known file
        for line in self.uFile: #getting the contents from the file
            uFileContents += line
        self.file = fileName
        self.uFile.close()

        self.text.insert(0.0, uFileContents) #opens text widget with the text from the file
        self.text.pack()

        self.page.mainloop()
        self.page.bind('<KeyPress>', onKeyPress)

#try to create a text class
if __name__ == '__main__':
    testPage = createPage("openFile")
