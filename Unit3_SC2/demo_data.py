import sqlite3


connection = sqlite3.connect('/Users/yinmialas/Desktop/Unit3_SC2/demo_data.sqlite3')

cursor = connection.cursor()
#create_taable = cursor.execute('CREATE TABLE demo ( id SERIAL PRIMARY KEY, S text,x integer,y integer);').fetchall()

values = [(1, 'g', 3, 9), (2, 'v', 5, 7), (3, 'f', 8, 7)]
insert_data = cursor.executemany('INSERT INTO demo VALUES(?,?,?,?)',values).fetchall()

#connection.commit()

many_rows = cursor.execute('SELECT COUNT(id) FROM demo;').fetchall()
#print(many_rows) # ansewr [(3,)]

x_y = cursor.execute('SELECT COUNT(x),COUNT(y)FROM demo;').fetchall()
# print(x_y) # answer [(3, 3)]

unique = cursor.execute('SELECT COUNT(DISTINCT s), COUNT(DISTINCT x), COUNT(DISTINCT y)FROM demo;').fetchall()
print(unique) # answer [(3, 3, 2)]
