import time


def get_sum(lines):
    addition = 0
    for row in range(1, len(lines)):
        addition += int(lines[row].split(',')[2])
    return addition


def get_avg(lines):
    addition = 0
    for row in range(1, len(lines)):
        addition += float(lines[row].split(',')[3])
    avg = float(addition)/float(len(lines)-1)
    return avg


with open('employee_file.csv', mode='r') as employee_file:
    file_lines = employee_file.readlines()
    start = time.time()
    print("sum is : {}".format(get_sum(file_lines)))
    stop = time.time()
    print("--- %s seconds ---" % (stop - start))

    start = time.time()
    print("avg is : {}".format(get_avg(file_lines)))
    stop = time.time()
    print("--- %s seconds ---" % (stop - start))

# sum is : 499999500000
# --- 4.740206003189087 seconds ---
# avg is : 500099.5
# --- 4.7077178955078125 seconds ---


