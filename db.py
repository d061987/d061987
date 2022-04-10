import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="root",
  password="Bappa@123456",
  database="icicidb"
  ) #use data base name

#print(mydb)

cursor = mydb.cursor()
#cursor.execute('CREATE DATABASE mynewdb') # create database
#cursor.execute('SHOW DATABASES')
# databases = cursor.fetchall()
# print(databases)
#cursor.execute('create table emp(id int, name varchar(100), sex char(21))')
cursor.execute('show tables')
tables = cursor.fetchall()
for t in tables:
  print(t)
cursor.execute('create table user(id int not null auto_increment primary key, name varchar(122))')
cursor.execute('alter table user add column city varchar(29)')
query = "insert into user(name, city) values(%s, %s)"
values = ('Virat', 'Delhi')
cursor.execute(query, values)
mydb.commit()
values = [('Rothi', 'Mumbai'),('Yubi', 'Panjab'),('Rahul','Bangaluru')]
cursor.executemany(query, values)
mydb.commit()