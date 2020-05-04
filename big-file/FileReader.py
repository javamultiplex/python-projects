import timeit


def get_sum(lines):
    addition = 0
    for row in range(1, len(lines)):
        addition += int(lines[row].split(',')[2])
    return addition


def get_avg(lines):
    addition = 0
    for row in range(1, len(lines)):
        addition += float(lines[row].split(',')[3])
    avg = float(addition) / float(len(lines) - 1)
    return avg


def read():
    with open('employee_file.csv', mode='r') as employee_file:
        file_lines = employee_file.readlines()
        print("sum is : {}".format(get_sum(file_lines)))
        print("avg is : {}".format(get_avg(file_lines)))


print(timeit.timeit(read, number=1))

# 1 million rows, 100 columns
# sum is : 499999500000
# avg is : 500099.5
# 11.902159672000002

# 4 millions rows, 200 columns
# sum is : 7999998000000
# avg is : 2000099.5
# 113.34780171300001
