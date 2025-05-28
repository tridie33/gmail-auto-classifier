from __future__ import print_function
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes requis pour lire, modifier et appliquer des labels aux mails
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def connect_gmail():
    """Connexion à l'API Gmail et authentification via OAuth"""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def search_messages(service, user_id, query):
    """Recherche les messages correspondant à une requête Gmail"""
    try:
        response = service.users().messages().list(userId=user_id, q=query).execute()
        messages = response.get('messages', [])
        return [msg['id'] for msg in messages]
    except Exception as error:
        print(f"Erreur lors de la recherche : {error}")
        return []

def apply_label(service, user_id, msg_id, label_name):
    """Applique un libellé à un message. Crée le libellé s'il n'existe pas."""
    try:
        # Vérifie si le libellé existe
        label_id = get_or_create_label(service, user_id, label_name)
        # Applique le label
        service.users().messages().modify(
            userId=user_id,
            id=msg_id,
            body={'addLabelIds': [label_id]}
        ).execute()
        print(f"Label '{label_name}' appliqué au mail {msg_id}")
    except Exception as error:
        print(f"Erreur lors de l'application du label : {error}")

def get_or_create_label(service, user_id, label_name):
    """Vérifie si un label existe déjà, sinon le crée et retourne son ID"""
    try:
        labels = service.users().labels().list(userId=user_id).execute().get('labels', [])
        for label in labels:
            if label['name'].lower() == label_name.lower():
                return label['id']
        # Le label n'existe pas, on le crée
        new_label = {
            'name': label_name,
            'labelListVisibility': 'labelShow',
            'messageListVisibility': 'show',
        }
        label = service.users().labels().create(userId=user_id, body=new_label).execute()
        print(f"Nouveau label créé : {label_name}")
        return label['id']
    except Exception as error:
        print(f"Erreur lors de la création du label : {error}")
        return None
