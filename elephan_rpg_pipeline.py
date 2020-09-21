import psycopg2

DB_NAME = 'unflvzfw'
DB_USER = 'unflvzfw'
DB_pass = 'f5sc5MwHR7KWP8lSrHdvVrcGnfS3RP-X'
DB_HOST = 'lallah.db.elephantsql.com'

# connect to ElephantSQL-hosted PostgresSQL DB
connection = psycopg2.connect(dbname=DB_NAME,
                              user=DB_USER,
                              password=DB_pass,
                              host=DB_HOST)

cursor = connection.cursor()
cursor.execute('SELECT * FROM test_table;')
result = cursor.fetchall()
#print(result)


################## connect sqlite3 db for rpg data ##############

import sqlite3

sl_conn = sqlite3.connect('/Users/yinmialas/Desktop/lambda_unit3/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3')
sl_cursor = sl_conn.cursor()
characters = sl_cursor.execute('SELECT * FROM charactercreator_character;').fetchall()
#print(characters)


##################### create character table in postgress and insert data ##################

create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT, 
    intelligence INT,
    dexterity INT,
    wisdom INT
)
'''
cursor.execute(create_character_table_query)
connection.commit()

for character in characters[0:10]:
    insert_query = f'''INSERT INTO rpg_characters
    (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES {character}
    '''
    cursor.execute(insert_query)
connection.commit()


######################## QUERY EXAMPLES ########################
''' big_query = insert into rpg_characters
(character_id

####### for delete #####
DELETE FROM RPG_cgaracter
Where character_id < 9 ;

###### update a table ######
 update rpg_character set intelligence = 1 where character_id = 9'''