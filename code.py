from googleapiclient.discovery import build

from google.oauth2 import service_account

import pandas as pd

SERVICE_ACCOUNT_FILE = 'key.json' # Location of the Service account Key jason file.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']



creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES) 
SAMPLE_SPREADSHEET_ID = '1NZuZ4gMR3W_6NvfD0ywBh3uEp0MAvdv-9GyE2662qNQ' # Copy and paste the ID of Google sheet in which data need to be read/ write.


service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Sheet1!A1:H25").execute() # to read the data

values = result.get('values', [])

df = pd.DataFrame(values,index=None,columns=None) 

# To create a data set and writing into google sheet

new_values=[["1/1/2020",4000],["3/1/2020",7000],["5/1/2022",3000]]

request = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet2!A1", valueInputOption="USER_ENTERED", body={"values":new_values})
response = request.execute()
