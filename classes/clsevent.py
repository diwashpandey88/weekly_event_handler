from classes.connection import DataBase


class Event:
    def __init__(self):
        self.db = DataBase()

    def add_item(self, days, events):
        if days == '' or events == '':
            return False
        else:
            qry = "INSERT INTO events (days,events) VALUES (%s,%s)"
            values = (days, events)
            self.db.iud(qry, values)
            return True

    def show_item(self):
        all_items = []
        try:
            qry = "SELECT * FROM events"
            all_items = self.db.show_data(qry)
            return all_items
        except Exception as abc:
            print(abc)
            return all_items

    def search_item(self, key):
        qry = "SELECT * FROM events WHERE days LIKE '" + key + "%'"
        all_items = self.db.show_data(qry)
        return all_items

    def update_item(self, row, days, events):
        try:
            qry = "UPDATE events SET days = %s, events = %s WHERE id = %s"
            values = (days, events, row)
            self.db.iud(qry, values)
            return True
        except Exception as error:
            print(error)
            return False

    def deleter(self, row):
        try:
            qry = "DELETE FROM events WHERE id=%s "
            values = (row,)
            self.db.iud(qry, values)
            return True
        except Exception as error:
            print(error)
            return False

def binary_search(list, key):
    start =0
    end=len(list) - 1

    while start <= end:
        mid = (start + end) // 2
        if list[mid] == key:
            return mid
        elif list[mid] > key:
            end = mid -1
        else:
            start = mid + 1
    return -1

def search_day():

    db = DataBase()
    qry = "SELECT days from events ORDER BY days"
    data = db.show_data(qry)
    my_data = []
    for i in data:
        my_data.append(i[0])
    print(my_data)
    print(binary_search(my_data,'Saturday'))
    print(binary_search(my_data, 'Monday'))



search_day()