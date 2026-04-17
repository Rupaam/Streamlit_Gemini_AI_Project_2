import google.generativeai as genai
from dotenv import load_dotenv
from gtts import gTTS
import os
import io

# loading the environment
load_dotenv()
my_api_key = os.getenv("Gemini_API_KEY")

# configure API
genai.configure(api_key=my_api_key)

# note generator
def hints_gen(images):
    prompt = """Find the problem of the code and give some hints to solve the code but not the correct code."""

    model = genai.GenerativeModel("gemini-3-flash-preview")

    response = model.generate_content([*images, prompt])
    
    return response.text

def sol_gen(image,difficulty):
     prompt = "Give the solution of the code. Give the right code and explain why that code was wrong"

     model = genai.GenerativeModel("gemini-3-flash-preview")

     response = model.generate_content([*image, prompt])
    
     return response.text