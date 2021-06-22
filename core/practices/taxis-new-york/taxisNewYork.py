"""
Download data from https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
Files: Yellow Taxi Trip Records 2020 for january, february and march
"""
from connector import SQLiteConnection




# Queries
query = '''SELECT *
             FROM taxi_trips
            LIMIT 100'''


if __name__ == "__main__":
    conn = SQLiteConnection('data/frogtek.db')
    conn.connect()
    conn.query_data(query)


