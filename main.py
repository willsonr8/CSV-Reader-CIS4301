import csv

def writeSQL(row):

    return

if __name__ == "__main__":
    inFile = open('Auto_Sales_data.csv')
    outFile = open('ToyCarOrdersAndSales Insert Commands.sql', 'a')
    csvreader = csv.reader(inFile)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        writeSQL(row)
    inFile.close()
    outFile.close()
