import pandas as pd
import time

df = pd.read_csv('employee_file.csv')
start = time.time()
Total = df['Age'].sum()
print("Sum is {}".format(Total))
stop = time.time()
print("--- %s seconds ---" % (stop - start))


start = time.time()
Total = df['Salary'].mean()
print("Average is {}".format(Total))
stop = time.time()
print("--- %s seconds ---" % (stop - start))

# Sum is 499999500000
# --- 0.0011210441589355469 seconds ---
# Average is 500099.5
# --- 0.005947113037109375 seconds ---


