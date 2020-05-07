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
        cur.execute('SELECT AGE,SALARY FROM employees')
        rows = cur.fetchall()
        age_total = 0
        salary_total = 0
        for row in rows:
            age_total += row[0]
            salary_total += row[1]
        avg = salary_total/len(rows)
        print("Age Total is {}".format(age_total))
        print("Avg is {}".format(avg))
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
# loaded all columns - 37.375320449 seconds
# loaded integer and decimal columns - 1.562145158 seconds
# 4 million rows, 200 columns - not able to load whole data at a time, getting below error
# server closed the connection unexpectedly
# 	This probably means the server terminated abnormally
# 	before or while processing the request.

