from abc import ABC, abstractmethod

class DatabaseQueries(ABC):
    """A Database."""
    @abstractmethod
    def create(self):
        """Create Query."""
    
    @abstractmethod
    def update(self):
        """Update Query."""

    @abstractmethod
    def delete(self):
        """Delete Query."""

class MySQLQueries(DatabaseQueries):
    def create(self):
        print("Create a MySQL Query.")
    def update(self):
        print("Update a MySQL Query.")
    def delete(self):
        print("Delete a MySQL Query.")

class MongoDBQueries(DatabaseQueries):
    def create(self):
        print("Create a MongoDB Query.")
    def update(self):
        print("Update a MongoDB Query.")
    def delete(self):
        print("Delete a MongoDB Query.")

class Neo4JQueries(DatabaseQueries):
    def create(self):
        print("Create a Neo4J Query.")
    def update(self):
        print("Update a Neo4J Query.")
    def delete(self):
        print("Delete a Neo4J Query.")

def main():
    database: str = input("Enter desired database (mysql, mongodb, neo4j): ")

    if database not in ["mysql", "mongodb", "neo4j"]:
        print("Selected Database Not Available")
        return

    if database == "mysql":
        queries = MySQLQueries()
    elif database == "mongodb":
        queries = MongoDBQueries()
    elif database == "neo4j":
        queries = Neo4JQueries()

    queries.create()
    queries.update()
    queries.delete()

if __name__ == "__main__":
    main()