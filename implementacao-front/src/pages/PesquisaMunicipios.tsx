
import { Autocomplete, TextField } from "@mui/material";
import { useEffect, useState, ChangeEvent } from "react";
import MenuBar from "../components/MenuBar";
import styles from "./PesquisaMunicipios.module.css";
import Chart from "react-apexcharts";
import { Qtd_2009, Qtd_2013, Qtd_2017, Qtd_2020, Qtd_2021 } from "../data/municipioDados";


interface Municipio {
  nome: string;
}

function PesquisaMunicipios(): JSX.Element {
  const [municipios, setMunicipios] = useState<string[]>([]);
  const [selectedMunicipio, setSelectedMunicipio] = useState<string>('');
  const [chartData, setChartData] = useState<any>({
    options: {
      chart: {
        id: 'bar-graphic'
      },
      xaxis: {
        categories: [2009, 2013, 2017, 2020, 2021]
      }
    },
    series: [{
      name: 'Nomeações',
      data: [0, 0, 0, 0, 0], // inicia com dados vazios
      color: "#FCA622",
      },
      {
        name: 'Exonerações',
        data: [0, 0, 0, 0, 0], // inicia com dados vazios
        color: "#A11208",
      }
    ]
  });

  const apiIBGE = async () => {
    try {
      const response = await fetch(
        "https://servicodados.ibge.gov.br/api/v1/localidades/estados/RS/municipios"
      );
      const data: Municipio[] = await response.json();
      setMunicipios(data.map((municipio) => municipio.nome.toLowerCase()));
    } catch (error) {
      console.error("Erro ao buscar municípios:", error);
    }
  };
  useEffect(() => {
    apiIBGE();
  }, []);

    // função para buscar os dados do município selecionado no arquivo municipioDados.ts
  const getDataFromMunicipio = (municipio: string) => {
    const nomeacoes = [];
    const exoneracoes = [];
    // criando um array com os dados de cada ano
    const dados = [Qtd_2009, Qtd_2013, Qtd_2017, Qtd_2020, Qtd_2021];
    // iterando sobre o array de dados
    for (let i = 0; i < dados.length; i++) {
      // buscando o município no array de dados do ano correspondente
      const found = dados[i].find(
        (item) => item.municipio.toLowerCase() === municipio.toLowerCase()
      );
      // se encontrou o município, adiciona as nomeações e exonerações aos arrays
      if (found) {
        nomeacoes.push(Number(found.nomeacoes));
        exoneracoes.push(Number(found.exoneracoes));
      } else {
        // se não encontrou o município, adiciona zero aos arrays
        nomeacoes.push(0);
        exoneracoes.push(0);
      }
    }
    return { nomeacoes, exoneracoes };
  };

    const handleMunicipio = (event: ChangeEvent<{}>, selectedValue: string | null) => {
      event.preventDefault(); // evita que o formulário seja enviado
      if (selectedValue) {
        setSelectedMunicipio(selectedValue);
        console.log(selectedValue); // mostra o município selecionado no console
        const { nomeacoes, exoneracoes } = getDataFromMunicipio(
          selectedValue
        ); // busca os dados do município no arquivo
        setChartData({
          // atualiza o estado do gráfico com os novos dados
          ...chartData,
          series: [
            {
              name: "Nomeações",
              data: nomeacoes,
              color: "#FCA622",
            },
            {
              name: "Exonerações",
              data: exoneracoes,
              color: "#A11208",
            },
          ],
        });
      }
    };

        <div className={styles.middleDiv}>
            <div className={styles.left}>  
                {/* <Total quantity={total}/> */}
            </div>         
        </div>

        <div className={styles.lowerDiv}>
          <Chart
            options={chartData.options}
            series={chartData.series}
            type="bar"
            width={1000}
            height={400}
          />
        </div>
      </div>
    </div>
  );
}

export default PesquisaMunicipios;
