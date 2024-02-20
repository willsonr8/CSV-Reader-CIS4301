import csv

def writeHelper(original_row):
    row = []
    for val in original_row:
        if "'" in val:
            new_val = ""
            for character in val:
                if character == "'":
                    new_val += "\'"
                else:
                    new_val += character
            row.append(new_val)
        else:
            row.append(val)
    return row


def write_sql(original_row, file):

    row = writeHelper(original_row)

    command = (f'INSERT INTO ToyCarOrdersAndSales VALUES ({row[0]}, {row[1]}, {row[2]}, {row[3]}, '
               f'{row[4]}, TO_DATE({row[5]}, \'dd/mm/yyyy\'), {row[6]}, \"{row[8]}\", '
               f'\"{row[11]}\", \"{row[13]}\", \"{row[14]}\", \"{row[15]}\", \"{row[16]}\", \"{row[17]}\", '
               f'\"{row[18]}\", \"{row[19]}\";\n')
    file.write(command)


if __name__ == "__main__":
    inFile = open('Auto_Sales_data.csv')
    outFile = open('ToyCarOrdersAndSales Insert Commands.sql', 'w')
    csvreader = csv.reader(inFile)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        write_sql(row, outFile)
    inFile.close()
    outFile.close()
