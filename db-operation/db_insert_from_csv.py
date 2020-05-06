import psycopg2
import csv
from config import config


def insert():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        with open('employee_file1.csv', 'r') as f:
            next(f)  # skip header row
            cur.copy_from(f, 'employees1', sep=',')
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('DB connection is closed')


if __name__ == '__main__':
    insert()
