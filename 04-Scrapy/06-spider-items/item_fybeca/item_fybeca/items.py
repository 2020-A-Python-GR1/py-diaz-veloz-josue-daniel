# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst


def transformar_url_imagen(texto):
    url_fybeca = 'https://www.fybeca.com'
    cadena_text = '../..'
    return texto.replace(cadena_text, url_fybeca)


class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        input_processor= MapCompose(
            transformar_url_imagen
        ),
        output_processor = TakeFirst() 
    )


class ItemFybecaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
