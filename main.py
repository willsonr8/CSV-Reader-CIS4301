import csv
import string

def writeSQL(row, file):
    command = (f'INSERT INTO ToyCarOrdersAndSales VALUES (int({row[0]}), int({row[1]}), float({row[2]}), int({row[3]}), '
               f'float({row[4]}), TO_DATE({row[5]}, \'dd/mm/yyyy\'), int({row[6]}), {row[7]}, {row[8]}, {row[9]}, '
               f'{row[10]}, {row[11]}, {row[12]}, {row[13]}, {row[14]}, {row[15]};\n')
    file.write(command)

def writeSQLnew(row, file):
    command = (f'INSERT INTO ToyCarOrdersAndSales VALUES ({row[0]}, {row[1]}, {row[2]}, {row[3]}, '
               f'{row[4]}, TO_DATE({row[5]}, \'dd/mm/yyyy\'), {row[6]}, {row[7]}, {row[8]}, {row[9]}, '
               f'{row[10]}, {row[11]}, {row[12]}, {row[13]}, {row[14]}, {row[15]};\n')
    file.write(command)


if __name__ == "__main__":
    inFile = open('Auto_Sales_data.csv')
    outFile = open('TESTToyCarOrdersAndSales Insert Commands.sql', 'a')
    csvreader = csv.reader(inFile)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        writeSQLnew(row, outFile)
    inFile.close()
    outFile.close()
