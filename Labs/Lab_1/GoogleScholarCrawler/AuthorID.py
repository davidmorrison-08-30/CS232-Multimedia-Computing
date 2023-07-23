import requests
from bs4 import BeautifulSoup

def GetAuthorId(author_name):
    query = author_name.replace(' ', '+')

    # url used for querying
    url = f'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={query}&btnG=&start=0'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # get author id from the author's profile link
    author_a_class = soup.find('h4', {'class': 'gs_rt2'})
    if author_a_class == None:
        author_id = None
    else:
        author_id = author_a_class.a.get("href").split("/citations?user=")[1].split("&")[0]

    return author_id