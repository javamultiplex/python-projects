import pandas as pd
import timeit


def read():
    df = pd.read_csv('employee_file.csv')
    total = df['Age'].sum()
    print("Sum is {}".format(total))
    avg = df['Salary'].mean()
    print("Average is {}".format(avg))


print(timeit.timeit(read, number=1))

# 1 million rows, 100 columns
# Sum is 499999500000
# Average is 500099.5
# 11.170137809


# 4 millions rows, 200 columns
# Sum is 7999998000000
# Average is 2000099.5
# 133.885191919
