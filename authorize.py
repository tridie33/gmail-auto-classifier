from __future__ import print_function
import os.path
import pickle
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes d'accès : lecture, écriture et gestion des mails
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def main():
    creds = None
    # Si token.json existe déjà, on le recharge
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # Sinon, on démarre un nouveau flow OAuth
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Sauvegarde du token dans token.json
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Juste pour tester que ça marche :
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    print("Connexion réussie. Voici vos labels :")
    for label in labels:
        print(f"- {label['name']}")

if __name__ == '__main__':
    main()
