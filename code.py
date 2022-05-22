from googleapiclient.discovery import build

from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'servicekey.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']



creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES) 
SAMPLE_SPREADSHEET_ID = '1NZuZ4gMR3W_6NvfD0ywBh3uEp0MAvdv-9GyE2662qNQ'


service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Sheet1!A1:H25").execute()

print(result)