import csv

def writeSQL(row, file):
    command = (f'INSERT INTO ToyCarOrdersAndSales VALUES ({row[0]}, {row[1]}, {row[2]}, {row[3]}, '
               f'{row[4]}, TO_DATE({row[5]}, \'dd/mm/yyyy\'), {row[6]}, {row[8]}, '
               f'{row[11]}, {row[13]}, {row[14]}, {row[15]}, row{16}, row{17}, row{18}, row{19};\n')
    file.write(command)


if __name__ == "__main__":
    inFile = open('Auto_Sales_data.csv')
    outFile = open('TESTToyCarOrdersAndSales Insert Commands.sql', 'w')
    csvreader = csv.reader(inFile)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        writeSQL(row, outFile)
    inFile.close()
    outFile.close()
