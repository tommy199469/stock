from stock import  get_data , handle_excel , analysis_data
from s3 import  download_file , upload_file


file_name = "stock.xlsx"
#download_file(file_name)
data = get_data()

data = analysis_data(data , file_name)
handle_excel(data , file_name)
#upload_file(file_name)
