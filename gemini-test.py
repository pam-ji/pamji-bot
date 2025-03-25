import os
import json
from google import genai



GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
client = genai.Client(api_key=GEMINI_API_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)

def generate_text(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text


#import google.generativeai as genai
# from google.oauth2 import service_account
# from googleapiclient.discovery import bui

# genai. .configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel('gemini-1.5-flash')
# response = model.generate_content(
#     'Tell me a story in 300 words'
# )
# print(response.text)

# # Setze deine API-Schlüssel und -Projekt-ID

# PROJECT_ID = "dein-projekt-id"

# # Erstelle ein Service-Konto und lade die Schlüsseldatei
# creds = service_account.Credentials.from_service_account_file(
#     "path/to/dein-schluessel-datei.json",
#     scopes=["https://www.googleapis.com/auth/cloud-platform"]
# )

# # Erstelle ein Client-Objekt für die Gemini-API
# gemini_client = build("generativelanguage", "v1beta", credentials=creds)

# # Definiere die Anfrage-Daten
# request_data = {
#     "contents": [
#         {
#             "parts": [
#                 {"text": "Write a story about a magic backpack."}
#             ]
#         }
#     ]
# }

# # Sende die Anfrage an die Gemini-API
# response = gemini_client.projects().locations().models().generateContent(
#     name=f"projects/{PROJECT_ID}/locations/-/models/gemini-1.5-flash",
#     body=request_data
# ).execute()

# # Verarbeite die Antwort
# print(response)