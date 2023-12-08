import MenuBar from "../components/MenuBar"
import Rank from "../components/Rank"
import Total from "../components/Total"
import styles from "./Home.module.css"
import Chart from "react-apexcharts"
//import { Qtd_RS } from "../data/totalPorAno";

const column = {
  options: {
    chart: {
      id: 'apexcrt-example'
    },
    xaxis: {
      categories: [2009, 2013, 2017, 2020, 2021]
    }
  },
  series: [{
    name: 'Nomeações',
    data: [81, 217, 847, 2316, 3253],
    color: "#FCA622",
    },
    {
      name: 'Exonerações',
      data: [16, 39, 149, 618, 708],
      color: "#A11208",
    }
  ]
}

const cidades_nomeiam = ['Campo Bom', 'Ibirubá', 'Santo Ângelo', 'Augusto Pestana', 'Independência']
const cidades_exoneram = ['Independência', 'Campo Bom', 'Santana da Boa Vista', 'Augusto Pestana', 'Ibirubá']

const quantidade_nomeacoes = [700, 598, 459, 398, 350]
const quantidade_exoneracoes = [149, 116, 111, 107, 100]
const total = [6714, 1530]

const pie = {
  options: {
    labels: ['Nomeações', 'Exonerações'],
    colors: ["#FCA622", "#A11208"]
  },
  series: total,
}

function Home() {
  return (
    <div className={styles.container}>
      <MenuBar />
      <div className={styles.content}>
        <div className={styles.upperDiv}>
          <div className={styles.left}>
            <h1 className={styles.title}>Dashboard</h1>
            <h1 className={styles.subTitle}>Rio Grande do Sul</h1>
            <br></br>
            <br></br>   
            <Total quantity={total}/>         
          </div>
          <div className={styles.pieGraph}>
            <h2 className={styles.graphTitle}>Exonerações x Nomeações nos anos analisados</h2>
            <Chart options={pie.options} series={pie.series}type="pie" width={400}/>            
          </div>
          <Rank title='Municípios que mais nomeiam:' cities={cidades_nomeiam} quantity={quantidade_nomeacoes}/>
        </div>
        <div className={styles.lowerDiv}>
          <Chart options={column.options} series={column.series} type="bar" labels="" width={750} height={400} />
          <Rank title='Municípios que mais exoneram:' cities={cidades_exoneram} quantity={quantidade_exoneracoes}/>
      </div>
      </div>
    </div>
  )
}

export default Home