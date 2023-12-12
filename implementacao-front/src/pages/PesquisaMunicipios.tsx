import { Autocomplete, TextField } from "@mui/material";
import { useEffect, useState, ChangeEvent } from "react";
import MenuBar from "../components/MenuBar";
import styles from "./PesquisaMunicipios.module.css";
import Chart from "react-apexcharts";

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

    // função para gerar dados aleatórios para os municípios
    const generateRandomData = () => {
      const nomeacoes = [];
      const exoneracoes = [];
      for (let i = 0; i < 5; i++) {
        nomeacoes.push(Math.floor(Math.random() * 1000)); // gera um número inteiro entre 0 e 999
        exoneracoes.push(Math.floor(Math.random() * 1000)); // gera um número inteiro entre 0 e 999
      }
      return {nomeacoes, exoneracoes};
    };

    const handleMunicipio = (event: ChangeEvent<{}>, selectedValue: string) => {
      if (selectedValue) {
        setSelectedMunicipio(selectedValue);
        console.log(selectedValue); // mostra o município selecionado no console
        const {nomeacoes, exoneracoes} = generateRandomData(); // gera dados aleatórios para o município
        setChartData({ // atualiza o estado do gráfico com os novos dados
          ...chartData,
          series: [{
            name: 'Nomeações',
            data: nomeacoes,
            color: "#FCA622",
            },
            {
              name: 'Exonerações',
              data: exoneracoes,
              color: "#A11208",
            }
          ]
        });
      }
    };

  return (
    <div className={styles.container}>
      <MenuBar />
      <div className={styles.content}>
        <div className={styles.upperDiv}>
          <div className={styles.left}>
            <h1 className={styles.subTitle}>Pesquisa por município</h1>
            <br></br>
            <br></br>
            <div className={styles.inputs}>
              <Autocomplete
                disablePortal
                id="combo-box-demo"
                options={municipios}
                value={selectedMunicipio}
                isOptionEqualToValue={(option, value) => option === value}
                sx={{ width: 300 }}
                renderInput={(params) => (
                  <TextField {...params} label="Busque um município..." />
                )}
                onChange={handleMunicipio}
              />
            </div>
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
