#!/usr/bin/env python3
import argparse
import mysql.connector
from mysql.connector import Error
from file_config import node_mapping
from sql_parser import determine_target_table

def route_query(query):
    target = determine_target_table(query, node_mapping)
    if target is None:
        print("Error: No known table found in query. Cannot route.")
        return
    elif isinstance(target, list):
        print("Error: Multiple known table references found in query:", target)
        print("Cannot reliably route to a single node.")
        return

    conn_params = node_mapping[target]
    try:
        # Use a buffered cursor to ensure that results are fully fetched.
        connection = mysql.connector.connect(**conn_params)
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        
        # For SELECT queries, fetch and display all results.
        if query.strip().upper().startswith("SELECT"):
            results = cursor.fetchall()
            if results:
                print("DEBUG: route_query - Query returned rows:")
                for row in results:
                    print(row)
            else:
                print("DEBUG: route_query - Query executed successfully, but no rows returned.")
        else:
            # For non-SELECT queries, print the number of affected rows.
            print(f"DEBUG: route_query - Query executed successfully. Rows affected: {cursor.rowcount}")
        
        connection.commit()
        print(f"Query routed to table '{target}' on node {conn_params['host']}.")
    except mysql.connector.Error as e:
        print(f"Error executing query on node {conn_params['host']}: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def main():
    parser = argparse.ArgumentParser(
        description="Route an SQL query to the appropriate MySQL node based on the target table."
    )
    parser.add_argument(
        'query',
        nargs='?',
        help="The SQL query to route. If not provided, interactive mode is used."
    )
    args = parser.parse_args()

    if args.query:
        route_query(args.query)
    else:
        print("Entering interactive mode. Type 'exit' or 'quit' to end.")
        while True:
            try:
                query = input("SQL> ")
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if query.strip().lower() in ("exit", "quit"):
                break
            if query.strip():
                route_query(query)

if __name__ == '__main__':
    main()
