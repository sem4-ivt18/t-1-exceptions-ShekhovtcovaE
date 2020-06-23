import sqlite3
def main():
  conn = sqlite3.connect('example.db')
  c = conn.cursor()
  flag = True
  if(conn):
    while(flag):
      print("1 - Ввод строки\n2 - Обновление по одному параметру\n3 - Удаление по одному параметру\n4 - Ввод нескольких строк\n5 - Обновление по нескольким параметрам\n6 - Удаление по нескольким параметрам\n7 - Вывод таблицы на экран")
      menu_choice = int(input())
      if menu_choice == 1:
        ins_row(c)
        conn.commit()
      elif menu_choice == 2:
        smbl = input("Введите значение символа, строку которого необходимо изменить \n")
        prc = float(input("Введите новую цену \n"))
        upd_row(c, smbl, prc)
        conn.commit()
      elif menu_choice == 3:
        d_smbl = input("Введите значение символа, строку которого хотите удалить \n")
        del_row(c, d_smbl)
        conn.commit()
      elif menu_choice == 4:
        lst = [('2006-03-28', 'BUY', 'IBM', 1000, 410),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 725.2),
             ('2006-04-06', 'SELL', 'IBM', 500, 317.00),
            ]
        ins_many(c, lst)
        conn.commit()
      elif menu_choice == 5:
        upd_lst = [(100, 'RHAT'),
               (122, 'IBM')]
        upd_many(c, upd_lst)
        conn.commit()
      elif menu_choice == 6:
        del_lst = [("MSFT"), ("RHAT")]
        del_many(c, del_lst)
        conn.commit()
      elif menu_choice == 7:
        param = input("Введите параметр, по которому хотите отсортировать")
        file_read(c, param)
      else: 
        flag = False
    
    conn.close()
  else:
    create_table(c)
    


def create_table(c):
  try:
    c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
  except sqlite3.OperationalError:
    print('Ошибка')
  
def ins_row(c):
  c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',198,35.14)")

def upd_row(c, smbl, prc) :
    try:
        c.execute("UPDATE stocks set price = ? WHERE symbol = ?", (prc, smbl,))
    except OperationalError:
        print("Нет такой строки")

def del_row(c, smbl):
    try:
      c.execute("DELETE FROM stocks WHERE symbol = ?", (smbl,))
    except OperationalError:
        print("Нет такой строки")


def file_read(c, param):
    for row in c.execute('SELECT * FROM stocks ORDER BY ?', (param, )):
        print(row)


def ins_many(c, lst):
    c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', lst)


def upd_many(c, lst):
  try:
    c.executemany("UPDATE stocks set price = ? WHERE symbol = ?", lst)
  except sqlite3.OperationalError:
    print("Нет такой строки")
     
 
def del_many(c, lst):
  try:
    c.executemany("DELETE FROM stocks WHERE symbol = ?", lst)
  except sqlite3.OperationalError:
    print("Нет такой строки")
    

main()