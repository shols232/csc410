# sql_parser.py
from sql_metadata import Parser

def extract_table_names(query):
    """
    Uses the sql-metadata library to extract table names from a SQL query.
    Returns a list of table names found in the query.
    """
    tables = Parser(query).tables
    print(f"DEBUG: extract_table_names - Extracted tables: {tables}")
    return tables

def determine_target_table(query, node_mapping):
    """
    Determines the target table for the query by:
      1. Extracting table names from the query using sql-metadata.
      2. Filtering the extracted names against the keys in node_mapping.
    Returns:
      - A single table name (string) if exactly one match is found.
      - None if no known table is found.
      - A list of table names if multiple matches are found.
    """
    extracted_tables = extract_table_names(query)
    
    known_tables = []
    for table in extracted_tables:
        for key in node_mapping:
            if table.lower() == key.lower():
                known_tables.append(key)
    # Remove duplicates.
    known_tables = list(set(known_tables))
    
    if len(known_tables) == 1:
        return known_tables[0]
    elif len(known_tables) == 0:
        print("DEBUG: determine_target_table - No matching table found.")
        return None
    else:
        print("DEBUG: determine_target_table - Multiple matching tables found.")
        return known_tables
