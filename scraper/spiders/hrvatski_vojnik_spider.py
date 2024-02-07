import scrapy
from scrapy.linkextractors import LinkExtractor

class HrvatskiVojnikSpider(scrapy.Spider):
    name = "hrvatski_vojnik"
    allowed_domains = ["hrvatski-vojnik.hr"]
    start_urls = ["https://hrvatski-vojnik.hr/kategorija/magazin/"]
    articles_link_extractor = LinkExtractor(allow=r"/kategorija/magazin/", restrict_css="h3.article-preview__title a")

    def parse(self, response):
        # filter articles
        article_urls = self.articles_link_extractor.extract_links(response)
        yield from response.follow_all(article_urls, callback=self.parse_articles)
        # next page
        yield from response.follow_all(css="a.next", callback=self.parse)

    def parse_articles(self, response):
        yield {
            "file_url": response.css("a.btn--download-magazin::attr(href)").get(),
        }
