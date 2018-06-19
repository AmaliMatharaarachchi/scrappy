import scrapy


class QuotesSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        # 'http://www.dailymirror.lk/sports',
        'http://www.dailymirror.lk/sports/15',
        # 'http://www.dailymirror.lk/sports/30',
        # 'http://www.dailymirror.lk/sports/45',
        # 'http://www.dailymirror.lk/sports/60',
        # 'http://www.dailymirror.lk/sports/75',
        # 'http://www.dailymirror.lk/sports/90',
        # 'http://www.dailymirror.lk/sports/105',
        # 'http://www.dailymirror.lk/sports/120',
        # 'http://www.dailymirror.lk/sports/135'

    ]

    def parse(self, response):
        for news in response.css('div.media'):
            yield {
                'title': news.css('div.media-body').css('h2.media-heading a::text').extract(),
                'summary': news.css('div.media-body::text').extract(),
                'views': news.css('div.media-body div.well div.comment-views::text').extract(),
                'date' : news.css('div.media-body div.well::text').extract(),
            }