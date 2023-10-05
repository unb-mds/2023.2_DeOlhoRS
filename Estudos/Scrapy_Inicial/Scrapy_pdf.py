import scrapy

class PDFSpider(scrapy.Spider):
    name = 'pdf_spider'
    start_urls = ['https://altamira.pa.gov.br/diario-oficial/']  # Substitua pela URL do site que deseja vasculhar

    def parse(self, response):
        # essa response retorna uma lista com TODOS os sites que hospedam os PDFs de cada mês 
        for link in response.xpath("//div[@class='post-content']/ul/li/a"):
            url = link.xpath('./@href').get()
            yield {
                'url': url
                
            }
            # Siga o link para o site externo
            yield scrapy.Request(url=url, callback=self.parse_pdf)
    def parse_pdf(self, response):
        pdf_url = response.xpath('//a[contains(@href, ".pdf")]/@href').get()
        if pdf_url is not None:
            yield {
                'PDF do Diario': pdf_url,
            }