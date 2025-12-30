from guardian_api.client import fetch_data
import pandas as pd

def main():
    articles = fetch_data(query="ukraine-Russian-war")
    try:
        df = pd.json_normalize(articles)
        print(df)
        print(f"Total articles fetched: {len(articles)}")
    except Exception as e:
        # Catch any error and print a friendly message
        print("Could not normalize articles into a DataFrame.")
        print("Reason:", e)
        print("Raw articles output:", articles)

if __name__ == "__main__":
    main()
