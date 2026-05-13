import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Env file se keys load karein
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def insert_data(text_input):
    try:
        # Aapke table ka naam "Aashu Yt" aur column "aashu_yt" hai
        data = {"aashu_yt": text_input}
        response = supabase.table("Aashu Yt").insert(data).execute()
        print("Data GitHub code se save ho gaya!")
    except Exception as e:
        print(f"Error: {e}")

# Test run
if __name__ == "__main__":
    insert_data("Entry via GitHub Code")
  
