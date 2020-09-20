# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader.processors import MapCompose,TakeFirst
import re

class Proyecto2BItem(scrapy.Item):
    nombre = scrapy.Field()
    pass
