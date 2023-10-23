import MenuBar from "../components/MenuBar"
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

function Home() {
  return (
    <div className={styles.container}>
      <MenuBar />
      <h1>Home Page</h1>
      <div className={styles.graphs}>
        <Chart options={pie.options} series={pie.series} type="pie" width={350} />
        <Chart options={column.options} series={column.series} type="bar" width={400} height={300} />
      </div>
    </div>
  )
}

export default Home
