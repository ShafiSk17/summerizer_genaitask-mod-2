from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai
import os
gemini_api_key="AIzaSyB2ILnUXepfWGQ62jFcSx6MlwCmbqW59kI"

genai.configure(api_key=gemini_api_key)


model = genai.GenerativeModel(
    model_name="gemini-pro",  # Replace with the desired Gemini model
)

if __name__ == "__main__":
  text = input("Enter the text you want to summarize: ")
 

  prompt = [f"Summarize the following text:\n\n{text}"]
  response = model.generate_content(prompt)
  print(f"Summary:\n{response.text}")
