from tkinter import *
from classes.clsevent import *
from tkinter import ttk, messagebox



class EventA:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('400x400')
        self.window.title('Events')

        self.text1 = Label(self.window, text="Events", width='28', font=('Arieal', 20))
        self.text1.grid(columnspan=4)

        self.event = Event()
        self.update_index = ""

        self.event_tree = ttk.Treeview(self.window, columns=('days', 'events'))
        self.event_tree.grid(row=2, column=0, columnspan=3)
        self.event_tree['show'] = 'headings'
        self.event_tree.column('days', width=200)
        self.event_tree.column('events', width=200)
        self.event_tree.heading('days', text='Days')
        self.event_tree.heading('events', text='Events')

        self.add = Button(self.window, text='+', command=self.add_item)
        self.add.grid(row=3, column=2)

        self.update = Button(self.window, text='Update', command=self.update_item)
        self.update.grid(row=3, column=1)

        self.delete = Button(self.window, text='Delete', command=self.delete)
        self.delete.grid(row=3, column=0)

        self.a1 = Label(self.window, text='Day')
        self.a1.grid(row=4, column=0)

        self.a1 = Entry(self.window, text='day')
        self.a1.grid(row=4, column=1)

        self.a2 = Label(self.window, text='Events')
        self.a2.grid(row=5, column=0)

        self.a2 = Entry(self.window, text='events')
        self.a2.grid(row=5, column=1)
        self.show_event_tree()
        self.window.mainloop()

    def add(self):
        Addevent()

    def hello(self):
        Upevent()

    def show_event_tree(self):
        self.event_tree.delete(*self.event_tree.get_children())
        data = self.event.show_item()
        for i in data:
            self.event_tree.insert("", "end", text=i[0], value=(i[1], i[2]))
        self.event_tree.bind("<Double-1>", self.on_item_select)

    def on_item_select(self, event):

        selected_row = self.event_tree.selection()[0]
        selected_item = self.event_tree.item(selected_row, 'values')
        self.update_index = self.event_tree.item(selected_row, 'text')
        self.a1.delete(0, END)
        self.a1.insert(0, selected_item[0])
        self.a2.delete(0, END)
        self.a2.insert(0, selected_item[1])

    def add_item(self):

        Days = self.a1.get()
        Events = self.a2.get()

        if self.event.add_item(Days, Events):
            messagebox.showinfo('Item', "Item Added")
            self.show_event_tree()
        else:
            messagebox.showerror("Error", 'Cannot be addedd')

    def update_item(self):

        if self.update_index == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            Days = self.a1.get()
            Events = self.a2.get()

            if self.event.update_item(self.update_index, Days, Events):
                messagebox.showinfo('Item', "Item Updated")
                self.show_event_tree()
                self.update_index = ""

            else:
                messagebox.showerror("Error", 'Can not be updated !!!')

    def delete(self):
        self.event.deleter(self.update_index)
        messagebox.showinfo('Item', "Item deleted")
        self.show_event_tree()
