from tkinter import *

from tkinter import ttk, messagebox
from classes.todo import *
import datetime

x = datetime.datetime.now()
z = x.strftime("%A")


class Todoui:

    def __init__(self):
        self.window = Tk()
        self.window.geometry('400x400')
        self.window.title('task')

        self.text1 = Label(self.window, text="To-do", width='28', font=('Arieal', 20))
        self.text1.grid(columnspan=4)

        self.text2 = Label(self.window, text='Today is {}'.format(z))
        self.text2.grid(row =1,column=1)
        self.update_index = ""
        self.a = Tododbsunday()
        self.b = Tododbmonday()
        self.c = Tododbtuesday()
        self.d = Tododbwednesday()
        self.e = Tododbthursday()
        self.f = Tododbfriday()
        self.g = Tododbsaturday()
        self.event_tree = ttk.Treeview(self.window, columns=('time', 'task'))
        self.event_tree.grid(row=2, column=0, columnspan=3)
        self.event_tree['show'] = 'headings'
        self.event_tree.column('time', width=200)
        self.event_tree.column('task', width=200)
        self.event_tree.heading('time', text='Time')
        self.event_tree.heading('task', text='Task')

        self.add = Button(self.window, text='+', command=self.add_item)
        self.add.grid(row=3, column=2)

        self.update = Button(self.window, text='Update', command=self.update_item)
        self.update.grid(row=3, column=1)

        self.delete = Button(self.window, text='Delete', command=self.deleter)
        self.delete.grid(row=3, column=0)

        self.a1 = Label(self.window, text='Time')
        self.a1.grid(row=4, column=0)

        self.a1 = Entry(self.window)
        self.a1.grid(row=4, column=1)

        self.a2 = Label(self.window, text='Task')
        self.a2.grid(row=5, column=0)

        self.a2 = Entry(self.window)
        self.a2.grid(row=5, column=1)
        if z == 'Sunday':
            self.show_todo_tree_sunday()
        if z == 'Monday':
            self.show_todo_tree_monday()
        if z == 'Tuesday':
            self.show_todo_tree_tuesday()
        if z == 'Wednesday':
            self.show_todo_tree_wednesday()
        if z == 'Thursday':
            self.show_todo_tree_thursday()
        if z == 'Friday':
            self.show_todo_tree_friday()
        if z == 'Saturday':
            self.show_todo_tree_saturday()
        self.window.mainloop()

    def show_todo_tree_sunday(self):

        self.event_tree.delete(*self.event_tree.get_children())
        data = self.a.show_item()
        for i in data:
            self.event_tree.insert("", "end", text=i[0], value=(i[1], i[2]))
        self.event_tree.bind("<Double-1>", self.on_item_select)

    def show_todo_tree_monday(self):

        self.event_tree.delete(*self.event_tree.get_children())
        data = self.b.show_item()
        for i in data:
            self.event_tree.insert("", "end", text=i[0], value=(i[1], i[2]))
        self.event_tree.bind("<Double-1>", self.on_item_select)

    def show_todo_tree_tuesday(self):

        self.event_tree.delete(*self.event_tree.get_children())
        data = self.c.show_item()
        for i in data:
            self.event_tree.insert("", "end", text=i[0], value=(i[1], i[2]))
        self.event_tree.bind("<Double-1>", self.on_item_select)

    def show_todo_tree_wednesday(self):

        self.event_tree.delete(*self.event_tree.get_children())
        data = self.d.show_item()
        for i in data:
            self.event_tree.insert("", "end", text=i[0], value=(i[1], i[2]))
        self.event_tree.bind("<Double-1>", self.on_item_select)

    def show_todo_tree_thursday(self):

        self.event_tree.delete(*self.event_tree.get_children())
        data = self.e.show_item()
        for i in data:
            self.event_tree.insert("", "end", text=i[0], value=(i[1], i[2]))
        self.event_tree.bind("<Double-1>", self.on_item_select)

    def show_todo_tree_friday(self):

        self.event_tree.delete(*self.event_tree.get_children())
        data = self.f.show_item()
        for i in data:
            self.event_tree.insert("", "end", text=i[0], value=(i[1], i[2]))
        self.event_tree.bind("<Double-1>", self.on_item_select)

    def show_todo_tree_saturday(self):

        self.event_tree.delete(*self.event_tree.get_children())
        data = self.g.show_item()
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
        if self.update_index != "":
            messagebox.showerror("Error", "Please update the selected row first")
        else:
            time = self.a1.get()
            task = self.a2.get()
            if z == "Sunday":
                if self.a.add_item(time, task):
                    messagebox.showinfo('Item', "Item Added")

                else:
                    messagebox.showerror("Error", 'Cannot be added')
            if z == "Monday":
                if self.b.add_item(time, task):
                    messagebox.showinfo('Item', "Item Added")

                else:
                    messagebox.showerror("Error", 'Cannot be added')
            if z == "Tuesday":
                if self.c.add_item(time, task):
                    messagebox.showinfo('Item', "Item Added")

                else:
                    messagebox.showerror("Error", 'Cannot be added')
            if z == "Wednesday":
                if self.d.add_item(time, task):
                    messagebox.showinfo('Item', "Item Added")

                else:
                    messagebox.showerror("Error", 'Cannot be added')
            if z == "Thursday":
                if self.e.add_item(time, task):
                    messagebox.showinfo('Item', "Item Added")

                else:
                    messagebox.showerror("Error", 'Cannot be added')
            if z == "Friday":
                if self.f.add_item(time, task):
                    messagebox.showinfo('Item', "Item Added")

                else:
                    messagebox.showerror("Error", 'Cannot be added')
            if z == "Saturday":
                if self.g.add_item(time, task):
                    messagebox.showinfo('Item', "Item Added")

                else:
                    messagebox.showerror("Error", 'Cannot be added')

    def update_item(self):



        if z == 'Sunday':
            if self.update_index == "":
                messagebox.showerror("Error", "Please select a row first")
            else:
                time = self.a1.get()
                task = self.a2.get()

                if self.a.update_item(self.update_index, time, task):
                    messagebox.showinfo('Item', "Item Updated")
                    self.show_todo_tree_sunday()
                    self.update_index = ""
                else:
                    messagebox.showerror("Error", 'Can not be updated !!!')
        if z == 'Monday':
            if self.update_index == "":
                messagebox.showerror("Error", "Please select a row first")
            else:
                time = self.a1.get()
                task = self.a2.get()

                if self.b.update_item(self.update_index, time, task):
                    messagebox.showinfo('Item', "Item Updated")
                    self.show_todo_tree_monday()
                    self.update_index = ""
                else:
                    messagebox.showerror("Error", 'Can not be updated !!!')

        if z == 'Tuesday':
            if self.update_index == "":
                messagebox.showerror("Error", "Please select a row first")
            else:
                time = self.a1.get()
                task = self.a2.get()

                if self.c.update_item(self.update_index, time, task):
                    messagebox.showinfo('Item', "Item Updated")
                    self.show_todo_tree_tuesday()
                    self.update_index = ""
                else:
                    messagebox.showerror("Error", 'Can not be updated !!!')
        if z == 'Wednesday':
            if self.update_index == "":
                messagebox.showerror("Error", "Please select a row first")
            else:
                time = self.a1.get()
                task = self.a2.get()

                if self.d.update_item(self.update_index, time, task):
                    messagebox.showinfo('Item', "Item Updated")
                    self.show_todo_tree_wednesday()
                    self.update_index = ""
                else:
                    messagebox.showerror("Error", 'Can not be updated !!!')
        if z == 'Thursday':
            if self.update_index == "":
                messagebox.showerror("Error", "Please select a row first")
            else:
                time = self.a1.get()
                task = self.a2.get()

                if self.e.update_item(self.update_index, time, task):
                    messagebox.showinfo('Item', "Item Updated")
                    self.show_todo_tree_thursday()
                    self.update_index = ""
                else:
                    messagebox.showerror("Error", 'Can not be updated !!!')
        if z == 'Friday':
            if self.update_index == "":
                messagebox.showerror("Error", "Please select a row first")
            else:
                time = self.a1.get()
                task = self.a2.get()

                if self.f.update_item(self.update_index, time, task):
                    messagebox.showinfo('Item', "Item Updated")
                    self.show_todo_tree_friday()
                    self.update_index = ""
                else:
                    messagebox.showerror("Error", 'Can not be updated !!!')
        if z == 'Saturday':
            if self.update_index == "":
                messagebox.showerror("Error", "Please select a row first")
            else:
                time = self.a1.get()
                task = self.a2.get()

                if self.g.update_item(self.update_index, time, task):
                    messagebox.showinfo('Item', "Item Updated")
                    self.show_todo_tree_saturday()
                    self.update_index = ""
                else:
                    messagebox.showerror("Error", 'Can not be updated !!!')
    def deleter(self):
        if z == 'Sunday':
            self.a.deleter(self.update_index)
            messagebox.showinfo('Item', "Item deleted")
        if z == 'Monday':
            self.b.deleter(self.update_index)
            messagebox.showinfo('Item', "Item deleted")

        if z == 'Tuesday':
            self.c.deleter(self.update_index)
            messagebox.showinfo('Item', "Item deleted")
        if z == 'Wednesday':
            self.d.deleter(self.update_index)
            messagebox.showinfo('Item', "Item deleted")
        if z == 'Thursday':
            self.e.deleter(self.update_index)
            messagebox.showinfo('Item', "Item deleted")
        if z == 'Friday':
            self.f.deleter(self.update_index)
            messagebox.showinfo('Item', "Item deleted")
        if z == 'Saturday':
            self.g.deleter(self.update_index)
            messagebox.showinfo('Item', "Item deleted")