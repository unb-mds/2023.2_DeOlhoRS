const { Builder, By, until } = require('selenium-webdriver');
const chai = require('chai');
const chaiAsPromised = require('chai-as-promised');

chai.use(chaiAsPromised);
const assert = chai.assert;

describe('Testes da Pesquisa', function () {
  let driver;

  before(async function () {
    driver = await new Builder().forBrowser('chrome').build();
  });

  after(async function () {
    await driver.quit();
  });

  it('Deve comparar o nome do primeiro da lista da pesquisa de um nome arbitrário', async function () {
    await driver.get('http://localhost:5173/');
    const botaoLateral = await driver.findElement(By.xpath('//*[@id="root"]/div/div[1]/div[2]/a[2]'));
    await botaoLateral.click()

    const barraPesquisa = await driver.findElement(By.xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/div[1]/input'));
    await barraPesquisa.clear();
    await barraPesquisa.sendKeys("Carlos");
    
    const botaoPesquisar = await driver.findElement(By.xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/button'));
    await botaoPesquisar.click()
    
    const primeiroDaLista =  await driver.findElement(By.xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[1]'))
    const nomeDoPrimeiroDaLista = await primeiroDaLista.getText()

    const textoEsperadoPrimeiro = 'JOÃO CARLOS SIQUEIRA.';
    
    assert.equal(nomeDoPrimeiroDaLista, textoEsperadoPrimeiro, 'O texto do elemento corresponde ao esperado.');
    
  });
  it('Deve pesquisar um nome sem aparições nos dados e verificar a não existência de dados sobre', async function () {
    await driver.get('http://localhost:5173/');
    const botaoLateral = await driver.findElement(By.xpath('//*[@id="root"]/div/div[1]/div[2]/a[2]'));
    await botaoLateral.click();
    const barraPesquisa = await driver.findElement(By.xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/div[1]/input'));
    await barraPesquisa.clear();
    await barraPesquisa.sendKeys("Enzo da Silva Silveira");
    
    const botaoPesquisar = await driver.findElement(By.xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/button'));
    await botaoPesquisar.click()
    
    const msgSobreOsDados =  await driver.findElement(By.xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/table/tbody/tr/td'))
    const textoDaMsg = await msgSobreOsDados.getText()

    const textoEsperado = 'Nenhum dado encontrado';
    
    assert.equal(textoDaMsg, textoEsperado, 'O texto do elemento corresponde ao esperado.');
    
  });

});
