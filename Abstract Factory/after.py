from abc import ABC, abstractmethod

class DatabaseQueries(ABC):
    """A Database Query."""
    def create(self):
        """Create a Database Query."""
    def update(self):
        """Update a Database Query."""
    def delete(self):
        """Delete a Database Query."""

class MySQLDatabaseQueries(DatabaseQueries):
    """A MySQL Database Query."""
    def create(self):
        print("Create a MySQL Query.")
    def update(self):
        print("Update a MySQL Query.")
    def delete(self):
        print("Delete a MySQL Query.")

class MongoDBDatabaseQueries(DatabaseQueries):
    """A MongoDB Database Query."""
    def create(self):
        print("Create a MongoDB Query.")
    def update(self):
        print("Update a MongoDB Query.")
    def delete(self):
        print("Delete a MongoDB Query.")

class Neo4JDatabaseQueries(DatabaseQueries):
    """A Neo4J Database Query."""
    def create(self):
        print("Create a Neo4J Query.")
    def update(self):
        print("Update a Neo4J Query.")
    def delete(self):
        print("Delete a Neo4J Query.")

class Database(ABC):
    """A Database."""
    @abstractmethod
    def generateQueries(self) -> DatabaseQueries:
        """Database Queries."""

class MySQL(Database):
    """A MySQL Database."""
    def generateQueries(self) -> DatabaseQueries:
        return MySQLDatabaseQueries()
    
class MongoDB(Database):
    """A MongoDB Database."""
    def generateQueries(self) -> DatabaseQueries:
        return MongoDBDatabaseQueries()
    
class Neo4J(Database):
    """A Neo4J Database."""
    def generateQueries(self) -> DatabaseQueries:
        return Neo4JDatabaseQueries()

class DatabaseFactory():
    def get_database(self, database: str) -> Database:
        """Get a Database."""
        if database == "mysql":
            return MySQL()
        elif database == "mongodb":
            return MongoDB()
        elif database == "neo4j":
            return Neo4J()
        
def main():
    database: str = input("Enter desired database (mysql, mongodb, neo4j): ")

    if database not in ["mysql", "mongodb", "neo4j"]:
        print("Selected Database Not Available")
        return

    db: Database = DatabaseFactory().get_database(database)
    queries: DatabaseQueries = db.generateQueries()

    queries.create()
    queries.update()
    queries.delete()

if __name__ == "__main__":
    main()