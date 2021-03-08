# Import openpyxl

# import os 
# os.getcwd()
# os.chdir() #this changes our CWD, if the excel sheet is not in CWD

# import pandas as pd 
# file = ‘Sample.xlsx’
# data = pd.ExcelFile(file)
# print(data.sheet_names) #this returns the all the sheets in the excel file
# [‘Sheet1’]

# df = data.parse(‘Sheet1’)
# df.infodf.head(10)

import pandas as pd

df = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx', sheet_name='your Excel sheet name')
print (df)