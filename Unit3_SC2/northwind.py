import sqlite3


########################## part 2 connect a given database ###################


connection1 = sqlite3.connect('/Users/yinmialas/Desktop/Unit3_SC2/northwind_small.sqlite3')

cursor1 = connection1.cursor()

check = cursor1.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()
#print(check)

check2 = cursor1.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()
#print(check2)

# What are the ten most expensive items (per unit price) in the database?
most_expensive = cursor1.execute('SELECT UnitPrice, MAX(UnitPrice) AS most_expensives FROM Product GROUP by UnitPrice ORDER BY most_expensives DESC LIMIT 10;').fetchall()
#print(most_expensive)

# What is the average age of an employee at the time of their hiring? (Hint: alot of arithmetic works with dates.)
age = cursor1.execute('''SELECT FirstName, BirthDate, HireDate, strftime('%Y', DATE(HireDate)) - strftime('%Y', DATE(BirthDate)) AS age FROM Employee;''').fetchall()
#print(age)

######################## part3 ####################

#- What are the ten most expensive items (per unit price) in the database *and* their suppliers

price_supplyier = cursor1.execute('SELECT MAX(UnitPrice) AS most_expensives, MAX(CompanyName) FROM Product LEFT JOIN Supplier ON Supplier.companyname = Supplier.CompanyName GROUP BY UnitPrice ORDER BY UnitPrice DESC LIMIT 10;').fetchall()
#print(price_supplyier)

