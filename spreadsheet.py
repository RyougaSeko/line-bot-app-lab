import sys
# sys.path.append("/Users/hoop105ryouga/Documents/LineBot/.venv/lib/python3.9/site-packages")
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class RemoteControlGoogleSpreadSheet:

    def __init__(self, user_id):
        # use creds to create a client to interact with the Google Drive API
        scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        # sheet = client.open("飲食店DB").sheet1
        sheet = client.open("EngBot")

        try :
            #新たにワークシートを作成し、Worksheetオブジェクトをworksheetに格納します。
            worksheet = sheet.add_worksheet(title="UserId", rows="100", cols="2")
        except :
            #すでにワークシートが存在しているときは、そのワークシートのWorksheetオブジェクトを格納します。
            worksheet = sheet.worksheet("UserId")

        self.worksheet = worksheet #worksheetをメンバに格納
        self.num = 1 #書き込む行を指定しているメンバ
        #Worksheetオブジェクト.update_cell(行番号, 列番号, "テキスト")
        # で指定したセルにテキストを書き込めます。
        self.worksheet.update_cell(1, self.num, user_id)

    #Todoリストの最後の行を返す
    def detect_last_row(self):
        row_count = 1
        while self.worksheet.cell(row_count, self.num).value != "":
            row_count += 1
        return row_count

    #受け取ったテキストをTodo列に順番に書いていく
    def write_UserId(self, user_id):
        self.worksheet.update_cell(self.detect_last_row(), self.num, user_id)


    #Todoのcolの中身をすべて取得して返す
    def get_UserId(self):
        #UserId列の値をリストにしてすべて取得
        UserList  = self.worksheet.col_values(self.num)

        return UserList


# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# restaurant_info = list_of_hashes[0]
# info = "あいうえお"
# for myvalue in restaurant_info.values():
#     info += myvalue
