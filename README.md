# Terms of reference for the position of Python Developer Junior.
# Test task: "ElectronicsTrading"
# Technologies:

● Python 3.8+

● Django 2.1+

● DRF 3.10+

● Celery 4.4 +

● PostgreSQL 10+

# Task Part #1 (mandatory):

1. Create a web application with an API interface and an admin panel.
2. Create a database using Django migrations.

# Implementation requirements:
1. **It is necessary to implement a network model for the sale of electronics. The network should
be a hierarchical structure of 5 levels:**
   - Factory;
   - Distributor;
   - Dealership;
   - Large retail chain;
   - Individual entrepreneur.

    Each link in the network refers to only one equipment supplier (not necessarily
    the previous one in the hierarchy). It is important to note that the hierarchy level is determined not by the name
    of the link, but by the relationship to the rest of the network elements, i.e. the factory is always at level 0, and if
    the retail network refers directly to the factory, bypassing the other links, its level is 1.


2. **Each link of the network has the following elements:**
   - Name;
   - Contacts:
     - Email;
     - Address:
       - Country;
       - City;
       - Street;
       - House number;
   - Products:
     - Name;
     - Model;
     - The date of the product's release to the market;
   - Employees;
   - Supplier (the previous network object in the hierarchy);
   - Debt to the supplier in monetary terms, up to kopecks;
   - Creation time (filled in automatically when created)


3. **Make a conclusion in the admin panel of the created objects.On the network object page, add:**
   - link to the "Supplier";
   - filter by city name;
   - "admin action", clearing debts to the supplier of selected
   objects


4. **Using DRF, create a set of views:**
- 4.1 Information about all network objects;
- 4.2 Information about objects of a certain country (filter by name);
- 4.3 Statistics on objects whose debt exceeds the average debt
of all objects;
- 4.4 All network objects where a certain product can be found (filter by product id);
- 4.5 The ability to create and delete a network object and a product;
- 4.6 The ability to update the data of the network object and product (prohibit updating via 
 API of the "Debt to the supplier" field);

5. **Configure API access rights so that only active employees have access to
the API.**

# Task Part #2 (optional):
- Fill in the database.
- Automate processes in the application using Celery.
- Configure separate API access.

# Implementation requirements:
1. **Fill the database with test data. You can choose the method yourself.**
2. **Write several celery tasks:**
    - The task should be started automatically every 3 hours and increase the debt
to the supplier by a random number from 5 to 500;
    - The task should start automatically at 6:30 every day and reduce
the debt owed to the supplier by a random number from 100 to 10,000;


# Run the project locally
1. **Fill in .env file, edit .env example**

2. **Build the containers**
```shell
docker-compose build
```
3. **Run the containers**
```shell
docker-compose up -d
```
4. **Track the logs**
```shell
docker-compose logs -f 
```