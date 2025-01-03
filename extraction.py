def extract_data_from_arxiv():
    import arxiv
    import pandas as pd
    from arxiv import SortCriterion, Search

    # Variables
    articles = []
    years = [2018, 2019, 2020, 2021]
    number_of_articles = 200
    client = arxiv.Client()

    for year in years:

        # Define search query
        search_query = f"Deep Reinforcement Learning AND submittedDate:[{year}01010000 TO {year}12312359]"

        # Search for the articles
        search = Search(
            query=search_query,
            max_results=number_of_articles,
            sort_by=SortCriterion.SubmittedDate,
        )

        # Request the articles
        results = client.results(search)

        # Save retrieved data in array
        for result in results:
            article = {
                "Title": result.title,
                "Authors": result.authors,
                "Abstract": result.summary,
                "PublishedDate": result.published.date().year,
            }
            articles.append(article)

    # Save articles in data frame
    df = pd.DataFrame(articles)
    return df