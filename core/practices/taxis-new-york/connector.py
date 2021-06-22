import sqlite3
import pandas as pd
import os
import openpyxl



# Database connection
class SQLiteConnection:
    def __init__(self, database):
        self.database = database
        self.cnx = None
        self.cursor = None

    def connect(self):
        try:
            # Connect to the database
            self.cnx = sqlite3.connect(self.database)
            print("Connection OK")
            self.cursor = self.cnx.cursor()
        except sqlite3.DatabaseError:
            print(f'Error found while connecting to {self.database}')
            raise

    def disconnect(self):
        self.cursor.close()
        self.cnx.close()
        print("Connection closed")

    def query_data(self, query):
        try:
            print("Executing query...\n")
            self.cursor.execute(query)
            print(" | ".join([i[0] for i in self.cursor.description]))
            for row in self.cursor.fetchall():
                print(row)
            print("Query executed successfully\n")
        except sqlite3.DatabaseError as e:
            print(e)

    # Get dataframe from query
    def getDataframe(self, query):
        try:
            self.cursor.execute(query)
            column_names = list(map(lambda x: x[0], self.cursor.description))
            df = pd.DataFrame(column_names, columns=self.cursor.fetchall())
            return df
        except sqlite3.DatabaseError as e:
            print(e)

    # Save query result to excel
    def data_to_excel(self, query, path):
        df = self.getDataframe(query)
        filename = os.path.basename(path)
        try:
            wb = openpyxl.Workbook()
            wb.save(filename=path)
            df.to_excel(path, sheet_name='Results', index=False)
            wb.close()
        except FileExistsError as e:
            print(f"Error found creating file {filename}")
            print(e)
