import psycopg2

connection = psycopg2.connect("dbname=test user=postgres password=theceo@16")

cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS table1')
cursor.execute('''
               CREATE TABLE table1(
                   id INTEGER PRIMARY KEY,
                   completed BOOLEAN NOT NULL DEFAULT FALSE
               );
''')
data = {
    'id': 1,
    'completed': True
}

SQL = '''
    INSERT INTO table1 VALUES(%(id)s,%(completed)s);               
'''

cursor.execute(SQL, data)
cursor.execute('INSERT INTO table1 VALUES(3,true);')
cursor.execute("SELECT * FROM table1")
result = cursor.fetchall()
print(result)
cursor.close()
connection.commit()
connection.close()
