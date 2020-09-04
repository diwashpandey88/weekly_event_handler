from classes.connection import DataBase

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



