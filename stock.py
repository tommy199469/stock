import pandas as pd
import requests , datetime , os , xlsxwriter
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

# get data from html
page = requests.get('http://www.etnet.com.hk/www/tc/stocks/industry_adu.php')
soup = BeautifulSoup(page.text, 'lxml')
headers = soup.find("tr" , "greyTxt").findChildren()
rows = soup.find_all( "tr" , {"class": ["oddRow", "evenRow"]})
header_txt = []
plate = []
sheet_name = datetime.date.today().strftime("%B %d, %Y")
excel_name = 'stock.xlsx'
for i in headers:
    header_txt.append(i.getText())

for i in rows:
    plate.append(
        {
            "name" : i.find('td').getText() ,
            "平均升/跌幅" : i.findAll('td')[1].getText()
        }
    )

# hanlde on excel
df = pd.DataFrame(plate)
writer = pd.ExcelWriter(excel_name, engine='openpyxl')
if os.path.isfile(excel_name):
    book = load_workbook(excel_name)
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

df.to_excel(writer, sheet_name=sheet_name)
# set column width
column_list = pd.Series(range(len(df.columns))).tolist()
worksheet = writer.sheets[sheet_name]
for column_cells  in column_list:
    i = get_column_letter(column_cells+2)
    worksheet.column_dimensions[i].width = 20

writer.save()
writer.close()
