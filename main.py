from pypika import Query
import duckdb
from lark import Lark

# Use PyPika to generate a simple SQL query
query = Query.select(1)
sql = query.get_sql()
print("Generated SQL:", sql)

# Use DuckDB to execute the query
result = duckdb.query(sql).fetchall()
print("Query result:", result)

# Use Lark to parse a simple string
grammar = """
start: DIGIT
DIGIT: "0".."9"
"""

parser = Lark(grammar)
tree = parser.parse("5")
print("Parse tree:", tree)