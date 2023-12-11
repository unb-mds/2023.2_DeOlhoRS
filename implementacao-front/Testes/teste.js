import { Builder, By, Key, until } from 'selenium-webdriver';


(async function example() {
    const driver = await new Builder().forBrowser('chrome').build();
    try {
      await driver.get('http://localhost:5173/');
      // Realize interações no seu aplicativo React usando o WebDriver
      await driver.findElement(By.xpath('//*[@id="root"]/div/div[1]/div[2]/a[1]')).click();
      // Aguarde até que algum elemento  seja visível, indicando que a ação foi concluída
    } finally {
      // Feche o navegador após a execução dos testes
      await driver.quit();
    }
  })();