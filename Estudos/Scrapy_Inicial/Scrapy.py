import scrapy 
class QuotesSpider(scrapy.Spider):
    # Url Inicial
    name = 'Spider'
    start_urls = ['https://quotes.toscrape.com/']
    # Método Parse, varre o código HTML obtendo as informações
    def parse(self, response):
        # a variavel textos recebe uma lista de todos os objetos div com classe igual a quote
        textos = response.xpath('*//div[@class="quote"]')
        for t in textos:
            yield {
                'Frase':t.xpath('.//span[@class="text"]/text()').get(),
                'Autor':t.xpath('.//small[@class="author"]/text()').get(),
                'Tags': t.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
            }
        # Recebe a próxima instancia de página
        next_pag = response.xpath('*//li[@class="next"]/a/@href').get()
        
        if next_pag is not None: 
            # scrapy faz a mudança de url para a próxima página e chama o método parse
            yield scrapy.Request(response.urljoin(next_pag), callback=self.parse)
            
            # Código executável
            # scrapy runspider Scrapy.py -o frases.json #
