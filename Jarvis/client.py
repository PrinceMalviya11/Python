
from google import genai

client = genai.Client(api_key="AIzaSyBHW6xbsEaJTWHLuVr-HY3_C2yxhFNQPqs")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
 