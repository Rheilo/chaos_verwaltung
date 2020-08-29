import tkinter as tk
import tkinter.ttk as ttk



class DynamischeLagerverwaltungGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.menu = None
        self.__init_menubar()
        #self.__erstelle_gui()


    def __erstelle_gui(self):
        raise NotImplementedError


    def __init_menubar(self):
        self.menu = tk.Menu(self)
        self.configure(menu=self.menu)

        self.menu_lager = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label = 'Lager', menu=self.menu_lager)
        self.menu_lager.add_command(label = 'Übersicht', command = None)
        self.menu_lager.add_command(label = 'Einlagern ...', command = None)
        self.menu_lager.add_command(label = 'Auslagern ...', command = None)
        self.menu_lager.add_separator()
        self.menu_lager.add_command(label = 'Auswertung', command = None)

        self.menu_artikel = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label = 'Artikel', menu = self.menu_artikel)
        self.menu_artikel.add_command(label = 'Neu ...', command = None)
        self.menu_artikel.add_command(label = 'Löschen', command = None)

        self.menu_einstellungen = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label = 'Einstellungen', command=None)

        self.menu_hilfe = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label = 'Hilfe', menu = self.menu_hilfe)
        self.menu_hilfe.add_command(label = 'Programm Hilfe', command=None)
        self.menu_hilfe.add_command(label = 'Update ...', command=None)
        self.menu_hilfe.add_command(label = 'Über ...', command=None)