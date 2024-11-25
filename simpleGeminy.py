import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load variables from the .env file
load_dotenv()

# Get the API Key from the environment variable
api_key = os.getenv("API_KEY")

# Configure the Generative AI API with the API key
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate content using the model
response = model.generate_content("Explain what is a LLM")

# Print the generated response
print(response.text)