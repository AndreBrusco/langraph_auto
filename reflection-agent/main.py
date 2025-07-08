from dotenv import load_dotenv
load_dotenv()
import os

if __name__ == '__main__':
    print("Hello LangGraph")

print(os.environ['OPENAI_API_KEY'])