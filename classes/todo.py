from classes.connection import DataBase

class Tododbsunday:
    def __init__(self):
        self.db = DataBase()

    def add_item(self, time, task):
        if time == '' or task == '':
            return False
        else:
            qry = "INSERT INTO sunday (time,task) VALUES (%s,%s)"
            values = (time, task)
            self.db.iud(qry, values)
            return True

    def show_item(self):
        qry = "SELECT * FROM sunday"
        all_items = self.db.show_data(qry)
        return all_items

    def search_item(self, key):
        qry = "SELECT * FROM sunday WHERE name LIKE '" + key + "%'"
        all_items = self.db.show_data(qry)
        return all_items

    def update_item(self,row, time, task):
        qry = "UPDATE sunday SET time = %s, task = %s WHERE id = %s"
        values = (time, task, row)
        self.db.iud(qry, values)
        return True

    def delete_item(self):
        pass

    def deleter(self,row):
        qry = "DELETE FROM sunday WHERE id=%s "
        values = (row,)
        self.db.iud(qry, values)


class Tododbmonday:
    def __init__(self):
        self.db = DataBase()

    def add_item(self, time, task):
        qry = "INSERT INTO monday (time,task) VALUES (%s,%s)"
        values = (time, task)
        self.db.iud(qry, values)
        return True

    def show_item(self):
        qry = "SELECT * FROM monday"
        all_items = self.db.show_data(qry)
        return all_items

    def search_item(self, key):
        qry = "SELECT * FROM monday WHERE name LIKE '" + key + "%'"
        all_items = self.db.show_data(qry)
        return all_items

    def update_item(self, row, time, task):
        qry = "UPDATE monday SET time = %s, task = %s WHERE id = %s"
        values = (time, task, row)
        self.db.iud(qry, values)
        return True

    def delete_item(self):
        pass

    def deleter(self, row):
        qry = "DELETE FROM monday WHERE id=%s "
        values = (row,)
        self.db.iud(qry, values)


class Tododbtuesday:
    def __init__(self):
        self.db = DataBase()

    def add_item(self, time, task):
        qry = "INSERT INTO tuesday (time,task) VALUES (%s,%s)"
        values = (time, task)
        self.db.iud(qry, values)
        return True

    def show_item(self):
        qry = "SELECT * FROM tuesday"
        all_items = self.db.show_data(qry)
        return all_items

    def search_item(self, key):
        qry = "SELECT * FROM tuesday WHERE name LIKE '" + key + "%'"
        all_items = self.db.show_data(qry)
        return all_items

    def update_item(self, row, time, task):
        qry = "UPDATE tuesday SET time = %s, task = %s WHERE id = %s"
        values = (time, task, row)
        self.db.iud(qry, values)
        return True

    def delete_item(self):
        pass

    def deleter(self, row):
        qry = "DELETE FROM tuesday WHERE id=%s "
        values = (row,)
        self.db.iud(qry, values)

class Tododbwednesday:
    def __init__(self):
        self.db = DataBase()

    def add_item(self, time, task):
        qry = "INSERT INTO wednesday (time,task) VALUES (%s,%s)"
        values = (time, task)
        self.db.iud(qry, values)
        return True

    def show_item(self):
        qry = "SELECT * FROM wednesday"
        all_items = self.db.show_data(qry)
        return all_items

    def search_item(self, key):
        qry = "SELECT * FROM wednesday WHERE name LIKE '" + key + "%'"
        all_items = self.db.show_data(qry)
        return all_items

    def update_item(self, row, time, task):
        qry = "UPDATE wednesday SET time = %s, task = %s WHERE id = %s"
        values = (time, task, row)
        self.db.iud(qry, values)
        return True

    def delete_item(self):
        pass

    def deleter(self, row):
        qry = "DELETE FROM wednesday WHERE id=%s "
        values = (row,)
        self.db.iud(qry, value)

class Tododbthursday:
    def __init__(self):
        self.db = DataBase()

    def add_item(self, time, task):
        qry = "INSERT INTO thursday (time,task) VALUES (%s,%s)"
        values = (time, task)
        self.db.iud(qry, values)
        return True

    def show_item(self):
        qry = "SELECT * FROM thursday"
        all_items = self.db.show_data(qry)
        return all_items

    def search_item(self, key):
        qry = "SELECT * FROM thursday WHERE name LIKE '" + key + "%'"
        all_items = self.db.show_data(qry)
        return all_items

    def update_item(self, row, time, task):
        qry = "UPDATE thursday SET time = %s, task = %s WHERE id = %s"
        values = (time, task, row)
        self.db.iud(qry, values)
        return True

    def delete_item(self):
        pass

    def deleter(self, row):
        qry = "DELETE FROM thursday WHERE id=%s "
        values = (row,)
        self.db.iud(qry, values)

class Tododbfriday:
    def __init__(self):
        self.db = DataBase()

    def add_item(self, time, task):
        qry = "INSERT INTO friday (time,task) VALUES (%s,%s)"
        values = (time, task)
        self.db.iud(qry, values)
        return True

    def show_item(self):
        qry = "SELECT * FROM friday"
        all_items = self.db.show_data(qry)
        return all_items

    def search_item(self, key):
        qry = "SELECT * FROM friday WHERE name LIKE '" + key + "%'"
        all_items = self.db.show_data(qry)
        return all_items

    def update_item(self, row, time, task):
        qry = "UPDATE friday SET time= %s, task = %s WHERE id = %s"
        values = (time, task, row)
        self.db.iud(qry, values)
        return True

    def delete_item(self):
        pass

    def deleter(self, row):
        qry = "DELETE FROM friday WHERE id=%s "
        values = (row,)
        self.db.iud(qry, values)

class Tododbsaturday:
    def __init__(self):
        self.db = DataBase()

    def add_item(self, time, task):
        qry = "INSERT INTO saturday (time,task) VALUES (%s,%s)"
        values = (time, task)
        self.db.iud(qry, values)
        return True

    def show_item(self):
        qry = "SELECT * FROM saturday"
        all_items = self.db.show_data(qry)
        return all_items

    def search_item(self, key):
        qry = "SELECT * FROM saturday WHERE name LIKE '" + key + "%'"
        all_items = self.db.show_data(qry)
        return all_items

    def update_item(self, row, time, task):
        qry = "UPDATE saturday SET time = %s, events = %s task id = %s"
        values = (time, task, row)
        self.db.iud(qry, values)
        return True

    def delete_item(self):
        pass

    def deleter(self, row):
        qry = "DELETE FROM saturday WHERE id=%s "
        values = (row,)
        self.db.iud(qry, values)