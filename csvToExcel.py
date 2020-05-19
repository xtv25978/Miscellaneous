import csv
import openpyxl


def csvToExcel()

  wb = openpyxl.Workbook()
  ws = wb.active
  with open('csvFile.csv') as f:
      reader = csv.reader(f, delimiter=':')
      for row in reader:
          ws.append(row)
  wb.save('csvFile.xlsx')
