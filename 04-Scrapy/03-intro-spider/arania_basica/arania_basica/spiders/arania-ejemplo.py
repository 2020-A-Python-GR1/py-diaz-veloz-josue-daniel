import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()
        imagenes = etiqueta_contenedora.css(
            'div.image_container > a > img::attr(src)'
        ).extract()
        precio = etiqueta_contenedora.css(
            'div.product_price > p.price_color::text'
        ).extract()
        stock = etiqueta_contenedora.css(
            'div.product_price > p.instock.availability::text'
        ).extract()
        lista_precios=[]
        for p in precio:
            p = p[1:]
            lista_precios.append(p)
        [float(i) for i in lista_precios]

        stock_final = [b.replace('\n', '').replace(' ', '') for b in stock]

        stars = etiqueta_contenedora.css('.star-rating').xpath("@class").extract()
        stars_final= [b.replace('star-rating ', '') for b in stars]        
        print(titulos)
        print(imagenes)
        print(lista_precios)
        print(stock_final)
        print(stars_final)

# scrapy crawl nombre_arania
