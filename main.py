import os
from browser_agent import fetch_ai_headlines
from terminal_agent import format_headlines
from file_agent import write_headlines_to_file

def main():
    print("🚀 Executing instruction: Find top 5 AI headlines and save to file.")

    # Step 0: Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # Step 1: Browser - Fetch top 5 AI news
    headlines = fetch_ai_headlines()

    # Step 2: Terminal - Format headlines
    formatted_headlines = format_headlines(headlines)

    # Step 3: File System - Write headlines to file
    write_headlines_to_file(formatted_headlines, "output/result.txt")

    print("✅ Task completed successfully! Results saved in 'output/result.txt'.")

if __name__ == "__main__":
    main()
