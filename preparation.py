import pandas as pd
import matplotlib.pyplot as plt

def prepare_data(df: pd.DataFrame, years: list, show_histograms: bool) -> pd.DataFrame:

    # Ensure PublishedDate is in datetime format
    df["PublishedDate"] = pd.to_datetime(df["PublishedDate"], errors="coerce")

    # Drop rows with null values in Authors or PublishedDate
    df = df.dropna(subset=["Authors", "PublishedDate"])

    # Expand the possible multiple authors of a paper to an own entry for each author
    df = df.explode(column="Authors")

    # Define the years to analyze
    years = range(2018, 2022)

    if show_histograms:
        for year in years:
            # Filter for the specific year
            year_filtered_df = df[df["PublishedDate"].dt.year == year]

            # Skip the year if no data is found
            if year_filtered_df.empty:
                print(f"No data found for year {year}. Skipping.")
                continue

            # Count authors for the selected year and take the top 10 authors with the most publications
            top_author_counts = year_filtered_df["Authors"].value_counts().head(10)

            # Plot the histogram
            top_author_counts.plot(kind="bar")
            plt.title(f"Top 10 authors for {year}")
            plt.xlabel("Author")
            plt.ylabel("Count")
            plt.yticks(range(0, max(top_author_counts.max() + 1, 11), 1))
            plt.show()
    return df