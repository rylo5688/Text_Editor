import Tkinter
import ttk

class Index(object):
    def __init__(self):
        self.page = Tkinter.Tk()
        self.page.title('Text_Editor')

        #setting the page geometry
        screen_width = str(self.page.winfo_screenwidth())
        screen_height = str(self.page.winfo_screenheight())
        self.page.geometry(screen_width+'x'+screen_height)

        #container

        #tabs
        tabContainer = ttk.Notebook(self.page)
        tab1 = ttk.Frame(tabContainer)
        print 'test'
        tabContainer.add(tab1, text='Tab One')

        self.page.mainloop()
