from neo4j import GraphDatabase

uri = "bolt://127.0.0.1:7474"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

queries = """
// Retrieve All Nodes
MATCH (n)
RETURN n;

// Retrieve All Relationships
MATCH ()-[r]->()
RETURN r;

// Count Nodes
MATCH (n)
RETURN count(n) AS nodeCount;

// Count Relationships
MATCH ()-[r]->()
RETURN count(r) AS relationshipCount;

// Get Node Labels
MATCH (n)
RETURN DISTINCT labels(n) AS labels
LIMIT 100;


// Get Relationship Types
MATCH ()-[r]->()
RETURN DISTINCT type(r) AS relationshipTypes
LIMIT 100;

// Example: Limit results to 25 nodes
MATCH (n)
RETURN n
LIMIT 100;
"""

def run_queries(tx, queries):
    for query in queries.strip().split(";"):
        if query.strip():
            result = tx.run(query)
            for record in result:
                print(record)

with driver.session() as session:
    session.write_transaction(run_queries, queries)

driver.close()