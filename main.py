from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from os import system


# run the scraper
process = CrawlerProcess(get_project_settings())
process.crawl("hrvatski_vojnik")
process.start()
process.join()

# commit the scraped files
system('git config --global user.email "you@example.com"')
system('git config --global user.name "GitHub Actions"')
system("git add arhiva")
system("git commit -m 'Dodaj novi broj Hrvatskog vojnika'")
system("git push")
