import psycopg2
from config import config


def insert(vendor_name):
    conn = None
    vendor_id = 0
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (vendor_name,))
        vendor_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('DB connection is closed')
    return vendor_id


def insert_list(vendor_list):
    conn = None
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO vendors(vendor_name) VALUES(%s)"""
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql, vendor_list)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('DB connection is closed')


if __name__ == '__main__':
   # print(insert('Bhavna'))
    print(insert_list([
        ('Ram', ),
        ('Mohan', ),
        ('Sohan', )
    ]))