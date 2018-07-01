from tkinter import *
import tkinter.ttk as ttk
from Tagcounter.misc import TagMethod
from tkinter.scrolledtext import ScrolledText


class GUI:
    def __init__(self):
        self.window = Tk()
        self.load_button = Button(self.window, text='Load from url', command=self.get_tags_from_url, width=11)
        self.view_button = Button(self.window, text='View from DB', command=self.view_tags_from_url, width=11)
        self.urls_combobox = ttk.Combobox(self.window, values=[u"www.yandex.ru"], height=3)
        self.predef_sel_button = Button(self.window, text='Select URL', command=self.select_predef_url, width=11)
        self.entry_url = Entry(self.window, width=23)
        self.out_tags_field = ScrolledText(self.window, height=10, width=13, font='Arial 14', wrap=WORD)
        self.status_bar = Label(self.window, text="ready...", bd=1, relief=SUNKEN, anchor=W)
        self.urls_combobox.pack()
        self.predef_sel_button.pack()
        self.entry_url.pack()
        self.load_button.pack()
        self.view_button.pack()
        self.out_tags_field.pack()
        self.status_bar.pack(side=BOTTOM, fill=X)
        self.window.resizable(width=False, height=False)
        self.controller = None

    def run(self):
        self.window.mainloop()

    def set_controller(self, controller):
        self.controller = controller
        self.fill_urls_from_file()

    def select_predef_url(self):
        self.entry_url.delete(0, END)
        self.entry_url.insert(0, self.urls_combobox.get())

    def get_tags_from_url(self):
        url = self.entry_url.get()
        self.controller.process_url(url, TagMethod.GET)

    def view_tags_from_url(self):
        url = self.entry_url.get()
        self.controller.process_url(url, TagMethod.VIEW)

    def print_msg(self, string):
        self.status_bar.configure(text=string)

    def clear_statusbar(self):
        self.print_msg('')

    def print_tags(self, string):
        self.clear_statusbar()
        """Clear text field and print new text"""
        self.out_tags_field.configure(state=NORMAL)
        self.out_tags_field.delete(1.0, END)
        self.out_tags_field.insert(INSERT, string)
        self.out_tags_field.configure(state=DISABLED)

    def fill_urls_from_file(self):
        """Get set of urls from prompt file"""
        self.urls_combobox.configure(values=self.controller.get_urls_from_file())

