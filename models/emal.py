import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from base64 import urlsafe_b64decode, urlsafe_b64encode
import os

scopes = ['https://mail.google.com']
our_email = "atienofaith12@gmail.com"
class Email:
    def __init__(self, email):
        self.scope = ['https://mail.google.com/']
        self.email = email

    #authenticate
    def gmail_authenticate(self):
        creds = None
        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                creds = pickle.load(token)
        #if there are no valid credentials available
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials2.json', self.scope)
                creds = flow.run_local_server(port=0)
            with open("token.pickle", "wb") as token:
                pickle.dump(creds, token)
        return build('gmail', 'v1', credentials=creds)




A = Email("atienofaith12@gmail.com")
service = A.gmail_authenticate()
print(service)



