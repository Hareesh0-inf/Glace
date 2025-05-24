import os
from google import genai
from dotenv import load_dotenv


def correct_grammer(text):
    try:
        # load_dotenv()
        # api = os.getenv("GOOGLE_API")
        # client = genai.Client(api)
        # response = client.models.generate_content(
        #     model = "gemini-2.0-flash",
        #     contents = "hey how ya doing"
        # )                                      
        # result = f"Grammered: {response.text}"
        result = "corrected"
        return result
    except:
        print("this didnt work")

def suggestion(text):
    try:
        # user_input = input()
        result = f"Suggested: {text}"
        return result
    except:
        print("this didnt work")
