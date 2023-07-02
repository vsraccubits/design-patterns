# Database Queries Using Abstract Factory

This code demonstrates the use of the Factory Method design pattern to create instances of different database queries.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the Python script.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the following command to execute the script:

   ```bash
   python before.py
   ```
   ```bash
   python after.py
   ```

## Code Explanation


+ DatabaseQueries (Abstract Base Class): An abstract class defining the common interface for database queries.

+ MySQLDatabaseQueries, MongoDBDatabaseQueries, Neo4JDatabaseQueries: Concrete implementations of DatabaseQueries for MySQL, MongoDB, and Neo4J databases.

+ Database (Abstract Base Class): An abstract class defining the common interface for database factories.

+ MySQL, MongoDB, Neo4J: Concrete implementations of Database for MySQL, MongoDB, and Neo4J database factories.

+ DatabaseFactory: An abstract factory class responsible for creating the appropriate database queries based on the user's input.

## Extending the Code

To add a new database and queries:

1. Create a new class that extends Database, DatabaseQueries