from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl
import os, json

def RunAPI(author_id):
    params = {
        "api_key": input("Enter your API key: "),
        # "api_key": os.getenv("API_KEY"),
        "engine": "google_scholar_author",
        "hl": "en",
        "author_id": author_id
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    return search, results


def ScrapeGScholar(search, results):
    author_results_data = {
        "author_data": {},
        "author_articles": []
    }

    author_results_data["author_data"]["name"] = results.get("author").get("name")
    print(author_results_data["author_data"])

    # extracting all author articles
    while True:
        results = search.get_dict()

        for article in results.get("articles", []):
            author_results_data["author_articles"].append([
                article.get("title"),
                article.get("link"),
            ])

        if "next" in results.get("serpapi_pagination", []):
            search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination").get("next")).query)))
        else:
            break

    print(json.dumps(author_results_data, indent=2, ensure_ascii=False))
    print(
        f"Done. Extracted {len(author_results_data['author_articles']) - 1} articles.")  # counts extra empty line, that's why -1.

    # writing data to a .txt file
    file_name =  author_results_data["author_data"]["name"] + "_articles.txt"
    with open(file_name, "w") as file:
        for i in author_results_data["author_articles"]:
            file.write(str(i[0]+'\n'))