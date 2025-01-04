import pandas as pd
import matplotlib.pyplot as plt

def prepare_data(df: pd.DataFrame, years: list, show_histograms: bool) -> pd.DataFrame:
    # Expand the possible multiple authors of a paper to an own entry for each author.
    # This makes the analysis of the quantity of an author much simpler
    df = df.explode(column="Authors")

    # Drop null values and duplicates
    df = df.dropna()
    df = df.drop_duplicates()

    if show_histograms:
        for year in years:
            # Filter for year
            year_filtered_df = df[df["PublishedDate"].isin([year])]

            # Counts authors for the selected year (2018-2021) and take the 10 authors with the most publications
            top_author_counts = year_filtered_df["Authors"].value_counts().head(10)

            # Print the histogram
            top_author_counts.plot(kind="bar")
            plt.title(f"Top 10 authors across {year}")
            plt.xlabel("Author")
            plt.ylabel("Count")
            plt.yticks(range(0, 11, 1))
            plt.show()
    return df