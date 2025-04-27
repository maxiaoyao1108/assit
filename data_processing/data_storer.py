import pymysql
from config.config import DB_CONFIG


def store_data(data, table_name):
    try:
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        for item in data:
            columns = ', '.join(item.keys())
            values = ', '.join([f'"{value}"' for value in item.values()])
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            cursor.execute(query)
        connection.commit()
        print(f"Data stored successfully in {table_name}")
    except pymysql.Error as e:
        print(f"Error storing data: {e}")
    finally:
        if connection:
            connection.close()

    