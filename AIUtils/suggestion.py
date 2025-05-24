import os
from dotenv import load_dotenv
from google import genai

def correct_grammer(text):
    try:
        load_dotenv()
        api = os.getenv("GOOGLE_API")
        client = genai.Client(api_key = api)
        response = client.models.generate_content(
            model = "gemini-2.0-flash",
            contents = text,
        )                                      
        result = f"{response.text}"
        return result
    except:
        print("this didnt work")

def suggestion(text):
    try:
        result = f"Suggested: {text}"
        return result
    except:
        print("this didnt work")

def init_grammer():
    load_dotenv()

if __name__ == "__main__":
    # Example usage
    text = "This are a example."
    print(correct_grammer(text))
    print(suggestion(text))
