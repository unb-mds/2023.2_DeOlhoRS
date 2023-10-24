import MenuBar from "../components/MenuBar"
import Rank from "../components/Rank"
import Total from "../components/Total"
import styles from "./Home.module.css"
import Chart from "react-apexcharts"

const column = {
  options: {
    chart: {
      id: 'apexchart-example'
    },
    xaxis: {
      categories: [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    }
  },
  series: [{
    name: 'Nomeações',
    data: [30, 40, 35, 50, 49, 60, 70, 91, 125],
    color: "#FCA622",
    },
    {
      name: 'Exonerações',
      data: [20, 60, 50, 35, 45, 55, 67, 43, 90],
      color: "#A11208",
    }
  ]
}

const pie = {
  options: {},
  series: [30, 70],
  labels: ['Nomeações', 'Exonerações'],
}

const cities = ['Porto Alegre', 'Caxias do Sul', 'Canoas', 'Pelotas', 'Santa Maria']

const quantity = [7282, 5321, 3293, 3124, 2130]
const n = [87465, 84577]

function Home() {
  return (
    <div className={styles.container}>
      <MenuBar />
      <div className={styles.content}>
        <div className={styles.upperDiv}>
          <div className={styles.left}>
            <h1 className={styles.title}>Dashboard</h1>
            <h1 className={styles.title}>Rio Grande do Sul</h1>   
            <Total quantity={n}/>         
          </div>
          <Chart options={pie.options} series={pie.series} type="pie" width={400} />
          <Rank title='Municípios que mais nomeiam' cities={cities} quantity={quantity}/>
        </div>
        <div className={styles.lowerDiv}>
          <Chart options={column.options} series={column.series} type="bar" width={700} height={300} />
      </div>
      </div>
    </div>
  )
}

export default Home
