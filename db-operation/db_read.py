import psycopg2
import timeit
from config import config


def read_fetchone():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name')
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('DB connection closed.')


def read_and_calculate_sum_avg():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT SUM(AGE), AVG(SALARY) FROM employees1')
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('DB connection closed.')


def read_fetchall():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT vendor_id, vendor_name FROM vendors')
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('DB connection closed.')


if __name__ == '__main__':
    print(timeit.timeit(read_and_calculate_sum_avg, number=1))


# 1 million rows, 100 columns
# (499999500000, Decimal('500099.500000000000'))
# 0.18974972 seconds

# 4 million rows, 200 columns

