from dotenv import load_dotenv
import os
from google import genai

# load variables from .env
load_dotenv()


client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how human life works in few words"
)

print(response.text)