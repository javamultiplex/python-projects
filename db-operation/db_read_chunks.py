import psycopg2
import timeit
import pandas as pd
from config import config


def read_and_calculate_sum_avg():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        generator_df = pd.read_sql(sql='SELECT * FROM employees1', con=conn, chunksize=10000)
        age_total = 0
        avg = 0
        for data_frame in generator_df:
            age_total += data_frame['age'].sum()
            avg += data_frame['salary'].mean()
        print("Age Total is {}".format(age_total))
        print("Avg is {}".format(avg))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('DB connection closed.')


if __name__ == '__main__':
    print(timeit.timeit(read_and_calculate_sum_avg, number=1))


# 1 million rows, 100 columns (chunk size = 10000)
# loaded all columns - 54.362647460999995 seconds
# loaded integer and decimal columns - 1.9676299580000003 seconds
# 4 million rows, 200 columns
# loaded all columns - 663.068275675
