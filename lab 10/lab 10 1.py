import psycopg2
import sys
import csv
try:
    connect = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="332468afk", port="5432")
except:
    print("can't establish connection")
    
cursor=connect.cursor()

def enter_data():
    name=input("ENTER YOUR NAME: ")
    number=input("ENTER YOUR NUMBER: ")

    user=(name, number)

    sql='''INSERT INTO phonebook (name, number) VALUES (%s, %s);'''
    cursor.execute(sql, user)

    connect.commit() 

def update_data():
    oldname=input("ENTER YOUR OLD NAME: ")
    oldnumber=input("ENTER YOUR OLD NUMBER: ")
    
    olduser=(oldname, oldnumber)
    
    sql='''DELETE FROM phonebook WHERE name=%s AND number=%s;'''
    cursor.execute(sql, olduser)
    
    connect.commit()
    
    newname=input("ENTER YOUR NEW NAME: ")
    newnumber=input("ENTER YOUR NEW NUMBER: ")
    
    newuser=(newname, newnumber)

    sql='''INSERT INTO phonebook (name, number) VALUES (%s, %s);'''
    cursor.execute(sql, newuser)

    connect.commit()

def delete():
    name=input("ENTER YOUR NAME: ")
    number=input("ENTER YOUR NUMBER: ")
    
    user=(name, number)
    
    sql='''DELETE FROM phonebook WHERE name=%s AND number=%s;'''
    
    cursor.execute(sql, user)
    
    connect.commit()
    
def csv_add():
    csv_path=input('Your csv file(path): ')
    
    file=open(csv_path, 'r')
    
    reader=csv.reader(file)
    
    next(reader)
    for row in reader:
        sql='''INSERT INTO phonebook (name, number) VALUES (%s, %s);'''
        
        data=(row[0], row[1])
        
        cursor.execute(sql, data)
        connect.commit()
        
def search():
    print("How would you like to search: NAME, NUMBER")
    method=input()
    if method=='NAME':
        name=input("Enter the name: ")
        sql='''SELECT * FROM phonebook WHERE name=%s'''
        cursor.execute(sql, (name,))
        rows=cursor.fetchall()
        for row in rows:
            print(row)
        
    if method=='NUMBER':
        number=input("Enter the number: ")
        sql='''SELECT * FROM phonebook WHERE number=%s;'''
        cursor.execute(sql, (number,))
        rows=cursor.fetchall()
        for row in rows:
            print(row)

def choose_command():
    print("Choose a command: ENTER, UPDATE, DELETE, CSV, SEARCH, DONE")

    command=input()

    if command=='ENTER':
        enter_data()
        choose_command()
    if command=='UPDATE':
        update_data()
        choose_command()
    if command=='DELETE':
        delete()
        choose_command()
    if command=='CSV':
        csv_add()
        choose_command()
    if command=='SEARCH':
        search()
        choose_command()
    if command=='DONE':
        connect.commit()
        cursor.close()
        connect.close()
        sys.exit()

choose_command()