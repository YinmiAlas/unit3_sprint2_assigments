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
#print(most_expensive) # answer [(263.5, 263.5), (123.79, 123.79), (97, 97), (81, 81), (62.5, 62.5), (55, 55), (53, 53), (49.3, 49.3), (46, 46), (45.6, 45.6)]

# What is the average age of an employee at the time of their hiring? (Hint: alot of arithmetic works with dates.)
age = cursor1.execute('''SELECT FirstName, BirthDate, HireDate, strftime('%Y', DATE(HireDate)) - strftime('%Y', DATE(BirthDate)) AS age FROM Employee;''').fetchall()
# print(age)
# # answer [('Nancy', '1980-12-08', '2024-05-01', 44), ('Andrew', '1984-02-19', '2024-08-14', 40), ('Janet', '1995-08-30', '2024-04-01', 29), 
# ('Margaret', '1969-09-19', '2025-05-03', 56), ('Steven', '1987-03-04', '2025-10-17', 38), 
# ('Michael', '1995-07-02', '2025-10-17', 30), ('Robert', '1992-05-29', '2026-01-02', 34), ('Laura', '1990-01-09', '2026-03-05', 36), ('Anne', '1998-01-27', '2026-11-15', 28)]

# - (*Stretch*) How does the average age of employee at hire vary by city?
age_city = cursor1.execute('''SELECT City, strftime('%Y', DATE(HireDate)) - strftime('%Y', DATE(BirthDate)) AS age FROM Employee;''').fetchall()
#print(age_city) # Answer: [('Seattle', 44), ('Tacoma', 40), ('Kirkland', 29), ('Redmond', 56), ('London', 38), ('London', 30), 
#('London', 34), ('Seattle', 36), ('London', 28)]



# ######################## part3 ####################

# #- What are the ten most expensive items (per unit price) in the database *and* their suppliers

price_supplyier = cursor1.execute('SELECT MAX(Product.UnitPrice) AS most_expensives, Supplier.CompanyName FROM Product LEFT JOIN Supplier ON Product.Id = Supplier.Id GROUP BY UnitPrice ORDER BY UnitPrice DESC LIMIT 10;').fetchall()
# print(price_supplyier) # answer [(263.5, None), (123.79, "Forêts d'érables"), (97, 'PB Knäckebröd AB'), (81, 'Leka Trading'), (62.5, 'Aux joyeux ecclésiastiques'), (55, None), (53, None), (49.3, None), (46, None), (45.6, 'Gai pâturage')]


#- What is the largest category (by number of unique products in it)?

largest_category = cursor1.execute('SELECT COUNT(DISTINCT ProductName), Description FROM Product LEFT JOIN Category ON Product.Id = Category.Id GROUP BY Description ORDER BY Description;').fetchall()
#print(largest_category) # answer [(69, None), (1, 'Breads, crackers, pasta, and cereal'), (1, 'Cheeses'), (1, 'Desserts, candies, and sweet breads'), (1, 'Dried fruit and bean curd'), 
#(1, 'Prepared meats'), (1, 'Seaweed and fish'), (1, 'Soft drinks, coffees, teas, beers, and ales'), (1, 'Sweet and savory sauces, relishes, spreads, and seasonings')]

# (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`(not name, region, or other fields) as the unique identifier for territories.
most_territories = cursor1.execute('SELECT MAX(EmployeeTerritory.TerritoryId) AS most_territories, Employee.Id FROM EmployeeTerritory LEFT JOIN Employee ON EmployeeTerritory.EmployeeId = Employee.Id;').fetchall()
# print(most_territories) # answer: [('98104', 6)]


############################ part4 ###################

# 1. In the Northwind database, what is the type of relationship between the `Employee` and `Territory` tables
# Answer: The relation between this two tanles is the foreign key which is the employeeid and territoryid

# 2. What is a situation where a document store (like MongoDB) is appropriate, and
#  what is a situation where it is not appropriate.
# Answer: document store is appropriate when The amount of data in many applications cannot be served affordably by a SQL database.
# it is not appropiate If you don't have a specific usecase to which a NoSQL database might offer a solution to.

# 3.  What is "NewSQL", and what is it trying to achieve
# Answer: NewSQL is a class of relational database management systems that seek to provide the scalability of NoSQL systems 
# for online transaction processing (OLTP) workloads while maintaining the ACID guarantees of a traditional database system.