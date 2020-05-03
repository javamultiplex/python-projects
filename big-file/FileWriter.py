import csv

ROWS_COUNT = 1000000

FILE_HEADER = ['Name', 'Department', 'Age', 'Salary', 'Address',
               'Attribute1', 'Attribute2', 'Attribute3', 'Attribute4', 'Attribute5',
               'Attribute6', 'Attribute7', 'Attribute8', 'Attribute9', 'Attribute10',
               'Attribute11', 'Attribute12', 'Attribute13', 'Attribute14', 'Attribute15',
               'Attribute16', 'Attribute17', 'Attribute18', 'Attribute19', 'Attribute20',
               'Attribute21', 'Attribute22', 'Attribute23', 'Attribute24', 'Attribute25',
               'Attribute26', 'Attribute27', 'Attribute28', 'Attribute29', 'Attribute30',
               'Attribute31', 'Attribute32', 'Attribute33', 'Attribute34', 'Attribute35',
               'Attribute36', 'Attribute37', 'Attribute38', 'Attribute39', 'Attribute40',
               'Attribute41', 'Attribute42', 'Attribute43', 'Attribute44', 'Attribute45',
               'Attribute46', 'Attribute47', 'Attribute48', 'Attribute49', 'Attribute50',
               'Attribute51', 'Attribute52', 'Attribute53', 'Attribute54', 'Attribute55',
               'Attribute56', 'Attribute57', 'Attribute58', 'Attribute59', 'Attribute60',
               'Attribute61', 'Attribute62', 'Attribute63', 'Attribute64', 'Attribute65',
               'Attribute66', 'Attribute67', 'Attribute68', 'Attribute69', 'Attribute70',
               'Attribute71', 'Attribute72', 'Attribute73', 'Attribute74', 'Attribute75',
               'Attribute76', 'Attribute77', 'Attribute78', 'Attribute79', 'Attribute80',
               'Attribute81', 'Attribute82', 'Attribute83', 'Attribute84', 'Attribute85',
               'Attribute86', 'Attribute87', 'Attribute88', 'Attribute89', 'Attribute90',
               'Attribute91', 'Attribute92', 'Attribute93', 'Attribute94', 'Attribute95']

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file)
    employee_writer.writerow(FILE_HEADER)
    for index in range(ROWS_COUNT):
        employee_writer.writerow(['Rohit{}'.format(index), 'IT', index, float(100+index), 'Address{}'.format(index),
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp',
                                  'temp', 'temp', 'temp', 'temp', 'temp'
                                  ])
