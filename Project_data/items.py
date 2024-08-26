import scrapy


class Database(scrapy.Item):
    draw_date = scrapy.Field()
    lottery_numbers = scrapy.Field()
    raffle_stars = scrapy.Field()
    day_of_week = scrapy.Field()
    day = scrapy.Field()
    month = scrapy.Field()
    year = scrapy.Field()
