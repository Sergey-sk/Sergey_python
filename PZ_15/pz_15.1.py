# Приложение КОММАНДИРОВОЧНЫЕ РАСХОДЫ для автоматизированного
# финансового контроля на предприятии. БД должна содержать таблицу Статьи расходов,
# имеющую следующую структуру записи: № приказа, Фамилия, Место командировки,
# Оплата, Аванс, Вид расходов, Сумма расходов.

import sqlite3 as sq

con = sq.connect('pz_15.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS expense_items (
    order_number INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name TEXT NOT NULL,
    trip_location TEXT NOT NULL,
    payment TEXT NOT NULL,
    advance REAL NOT NULL,
    expense_type TEXT NOT NULL,
    expense_amount REAL NOT NULL)''')

con.commit()

def insert(last_name, trip_location, payment, advance, expense_type, expense_amount):
    cur.execute('''INSERT INTO expense_items (last_name, trip_location, payment, advance, expense_type, expense_amount)
    VALUES (?, ?, ?, ?, ?, ?)''', (last_name, trip_location, payment, advance, expense_type, expense_amount))
    con.commit()

def search(data):
    cur.execute(f'SELECT * FROM expense_items WHERE {data}')
    return cur.fetchall()

def delete(data):
    cur.execute(f'DELETE FROM expense_items WHERE {data}')
    con.commit()

def edit(update_data, data):
    cur.execute(f'UPDATE expense_items SET {update_data} WHERE {data}')
    con.commit()

insert('Иванов И.И.', 'Москва', '1000', 500, 'Транспорт', 1500)
insert('Петров П.П.', 'Санкт-Петербург', '1200', 600, 'Проживание', 1800)
insert('Сидоров А.А.', 'Ростов-на-Дону', '1500', 800, 'Еда', 2000)

delete("order_number = '002'")

results = search("last_name = 'Иванов И.И.'")
results2 = search("trip_location = 'Санкт-Петербург'")
results3 = search("payment = '1500'")
print("Результаты поиска:", results)
print("Результаты поиска:", results2)
print("Результаты поиска:", results3)

edit("payment = 1100.0", "order_number = '001'")
edit("advance = 400", "order_number = '002'")
edit("expense_amount = 1000 ", "order_number = '003'")


con.close()