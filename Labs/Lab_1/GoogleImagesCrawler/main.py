# please install icrawler framework using
# pip install requirements.txt

from icrawler.builtin import GoogleImageCrawler

query = input("What do you want to search for? ")

google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=2,
    downloader_threads=4,
    storage={'root_dir': query})

filters = dict(
    size='large',
    color='color',
    license='noncommercial')
google_crawler.crawl(keyword=query, filters=filters, max_num=7000)