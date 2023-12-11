const { Builder, By, until } = require('selenium-webdriver');
const chai = require('chai');
const chaiAsPromised = require('chai-as-promised');

chai.use(chaiAsPromised);
const assert = chai.assert;

describe('Testes da Home', function () {
  let driver;

  before(async function () {
    driver = await new Builder().forBrowser('chrome').build();
  });

  after(async function () {
    await driver.quit();
  });

  it('Deve comparar a quantidade de exonerações e nomeações que aparecem na home com as reais', async function () {
    await driver.get('http://localhost:5173/');
    const botaoHome = await driver.findElement(By.xpath('//*[@id="root"]/div/div[1]/div[2]/a[1]'));
    await botaoHome.click();
    const xpathDoElementoNomeia = '//*[@id="root"]/div/div[2]/div[1]/div[1]/div/ol/li[1]';
    const elementoNomeia = await driver.findElement(By.xpath(xpathDoElementoNomeia));
    const textoDoElementoNomeia = await elementoNomeia.getText();

    const xpathDoElementoExonera = '//*[@id="root"]/div/div[2]/div[1]/div[1]/div/ol/li[2]';
    const elementoExonera = await driver.findElement(By.xpath(xpathDoElementoExonera));
    const textoDoElementoExonera = await elementoExonera.getText();

    
    const textoEsperadoNomeia = '6714 Nomeações';
    const textoEsperadoExonera = '1530 Exonerações';
    assert.equal(textoDoElementoExonera, textoEsperadoNomeia, 'O texto do elemento corresponde ao esperado.');
    assert.equal(textoDoElementoNomeia, textoEsperadoExonera, 'O texto do elemento corresponde ao esperado.');
  });
  it('Deve comparar os nomes dos municipios que mais exoneram', async function () {
    await driver.get('http://localhost:5173/');
    const botaoHome = await driver.findElement(By.xpath('//*[@id="root"]/div/div[1]/div[2]/a[1]'));
    await botaoHome.click();

    const xpathDoQueMaisNomeia = '//*[@id="root"]/div/div[2]/div[1]/div[3]/ol/li[1]';
    const elementoQueMaisNomeia = await driver.findElement(By.xpath(xpathDoQueMaisNomeia));
    const textoDoQueMaisNomeia = await elementoQueMaisNomeia.getText();
    
    const xpathDoQueMaisExonera = '//*[@id="root"]/div/div[2]/div[2]/div[2]/ol/li[1]';
    const elementoQueMaisExonera = await driver.findElement(By.xpath(xpathDoQueMaisExonera));
    const textoDoQueMaisExonera = await elementoQueMaisExonera.getText();
    
    const textoEsperadoNomeia = 'Campo Bom ................. 700';
    const textoEsperadoExonera = 'Independência ................. 149';
  
    assert.equal(textoDoQueMaisNomeia, textoEsperadoNomeia, 'O texto do elemento corresponde ao esperado.');
    assert.equal(textoDoQueMaisExonera, textoEsperadoExonera, 'O texto do elemento corresponde ao esperado.');
  });
});
