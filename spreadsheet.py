import sys
# sys.path.append("/Users/hoop105ryouga/Documents/LineBot/.venv/lib/python3.9/site-packages")
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("EngBot_Sheet1").sheet1
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
user_id = "user_id"
    
#空のcell(Noneが帰ってくるまで)に行き着くまでになるまで、繰り返し見ていく
row_count = 1
while sheet.cell(row_count, 1).value != None:
    row_count += 1
    print(sheet.cell(row_count, 1).value)
list_of_hashes = sheet.update_cell(row_count, 1, user_id)