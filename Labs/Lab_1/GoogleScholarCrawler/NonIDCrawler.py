import requests
from bs4 import BeautifulSoup


def get_articles(author_name):
    # format the author name to include in the search query
    query = author_name.replace(' ', '+')

    # start with the first page of search results
    url = f'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={query}&btnG=&start=0'

    # keep fetching pages until there are no more results
    results = []
    while True:
        # fetch the search results page
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # extract the links to the author's articles
        articles = soup.find_all('div', {'class': 'gs_ri'})
        if not articles:
            break

        # extract the title and URL for each article
        for article in articles:
            title = article.find('h3', {'class': 'gs_rt'}).text
            link = article.find('a')['href']
            results.append({'title': title, 'link': link})

        # update the URL to fetch the next page of results
        start = int(url.split('start=')[1]) + 10
        if start > 40:
            break
        url = f'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={query}&btnG=&start={start}'

    # return results
    file_name = author_name + "_articles.txt"
    with open(file_name, "w") as file:
        for i in results:
            file.write((i["title"]) + '\n' + str(i["link"]) + '\n\n')