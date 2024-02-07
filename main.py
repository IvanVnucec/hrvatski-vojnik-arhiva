def exec(cmd):
    from os import system
    print(cmd)
    system(cmd)

def main():
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings
    # run the scraper
    process = CrawlerProcess(get_project_settings())
    process.crawl("hrvatski_vojnik")
    process.start()
    process.join()

    # commit the scraped files
    exec('git config --global user.email "you@example.com"')
    exec('git config --global user.name "GitHub Actions"')
    exec("git add arhiva")
    exec("git commit -m 'Dodaj novi broj Hrvatskog vojnika'")
    exec("git push")

if __name__ == "__main__":
    main()
