from ScholarAPI import *
from AuthorID import *
from NonIDCrawler import *

author_name = input("Enter the author's name whose articles you would like to crawl: ")

author_id = GetAuthorId(author_name)

if author_id != None:
    search, results = RunAPI(author_id)
    ScrapeGScholar(search, results)
else:
    print(f"{author_name}'s id can't be found, so I decide to crawl on 5 first query pages ")
    get_articles(author_name)