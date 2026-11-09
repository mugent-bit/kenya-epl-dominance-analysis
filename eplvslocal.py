import pandas as pd
from pytrends.request import TrendReq
import time


def fetch_kenya_football_trends():
    print("Initializing Google Trends connection for Kenya...")


    pytrends = TrendReq(hl='en-US', tz=180)


    keywords = ["EPL", "FKF Premier League", "Gor Mahia", "Arsenal FC", "Manchester United"]

    print(f"Fetching interest over time for keywords: {keywords}")


    pytrends.build_payload(
        kw_list=keywords,
        cat=0,
        timeframe='today 12-m',
        geo='KE',
        gprop=''
    )

    # Retrieve interest over time dataframe
    df_interest = pytrends.interest_over_time()

    if df_interest.empty:
        print("Warning: No data returned. Google Trends might be rate-limiting. Try again in a few minutes.")
        return None

    # Drop the 'isPartial' column if present
    if 'isPartial' in df_interest.columns:
        df_interest = df_interest.drop(columns=['isPartial'])

    print("\n--- Data Sample Retrieved ---")
    print(df_interest.head())

    # Save clean dataset for local analysis / Tableau import
    output_filename = "kenya_football_google_trends.csv"
    df_interest.to_csv(output_filename)
    print(f"\nSuccessfully saved dataset to {output_filename}")

    return df_interest


if __name__ == "__main__":
    df = fetch_kenya_football_trends()
    # Melt wide DataFrame to long/tall format for Tableau
    df_melted = df.reset_index().melt(id_vars=['date'], var_name='Keyword', value_name='Search Interest')
    df_melted.to_csv("tableau_kenya_trends_tall.csv", index=False)
    print("Exported Tableau CSV successfully!")