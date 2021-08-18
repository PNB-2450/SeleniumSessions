import xlrd

"""workbook = xlrd.open_workbook("C:/Users/pnb98/Desktop/TestData.xlsx")
sheet = workbook.sheet_by_name("Data")

# to get total number of rows & coloumns
rowCount = sheet.nrows
print("Number of Rows: ", rowCount)
colCount = sheet.ncols
print("No of colomns: ", colCount)
"""

data = {}
data["FName"]='Chanti'
data["Lname"]='Babu'
data["Mobile"]=254163
print(data)
