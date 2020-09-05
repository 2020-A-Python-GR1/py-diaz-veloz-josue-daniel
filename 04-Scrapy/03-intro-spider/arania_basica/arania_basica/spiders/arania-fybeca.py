import scrapy

class IntroSpider(scrapy.Spider):
    name = 'fybeca_spider'

    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        etiqueta_contenedora = response.css(
            'div.product-tile-inner'
        )
        imagenes = etiqueta_contenedora.css(
            'div.detail > a.image > img#gImg::attr(src)'
        ).extract()

        precios = etiqueta_contenedora.css(
            'div.detail>div.side > div.price'
        ).xpath("@data-bind").extract()

        precios_final = [b.replace("text:'$' + (", '').replace(").formatMoney(2, '.', ',')", '') for b in precios] 

        lista_precios=[]
        for p in precios_final:
            lista_precios.append(p)
        [float(i) for i in lista_precios]

       
        precios_miembro = etiqueta_contenedora.css(
            'div.detail>div.side > div.price-member >div'
        ).xpath("@data-bind").extract()
        
        precios_miembro_final = [b.replace("text:'$' + (", '').replace(").formatMoney(2, '.', ',')", '') for b in precios_miembro] 

        lista_precios_miembros=[]
        for p in precios_miembro_final:
            lista_precios_miembros.append(p)
        [float(i) for i in lista_precios_miembros]

        print(imagenes)
        print(lista_precios)
        print("El precio normal minimo es : " + str(min(float(sub) for sub in lista_precios))) 
        print("El precio normal maximo es : " + str(max(float(sub) for sub in lista_precios))) 
        print(precios_miembro_final)
        print("El precio miembro minimo es : " + str(min(float(sub) for sub in precios_miembro_final))) 
        print("El precio miembreo maximo es : " + str(max(float(sub) for sub in precios_miembro_final))) 

        difference = [round((float(x1) - float(x2)),2) for (x1, x2) in zip(lista_precios, lista_precios_miembros)]
        
        total = sum(difference)
        print("El ahorro total en compra de afiliado es de  : "+ str(total)) 



# scrapy crawl nombre_arania
