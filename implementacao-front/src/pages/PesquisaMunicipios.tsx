import MenuBar from "../components/MenuBar"
import Total from "../components/Total"
import styles from "./PesquisaMunicipios.module.css"
import Chart from "react-apexcharts"
//import { useState } from "react"
import { Qtd_RS } from "../data/totalPorAno"
import { Qtd_2023 } from "../data/totalPorAno"

//import { DataTable } from 'primereact/datatable'
//import { FilterMatchMode } from 'primereact/api'
//import { InputText } from 'primereact/inputtext'


const column = {
  options: {
    chart: {
      id: 'apexchart-example'
    },
    xaxis: {
      categories: Qtd_RS.map((item) => item.ano)
    }
  },  
  series: [{
    name: 'Nomeações',
    data: Qtd_RS.map((item) => parseInt(item.nomeacoes)),
    color: "#FCA622",
    },
    {
      name: 'Exonerações',
      data: Qtd_RS.map((item) => parseInt(item.exoneracoes)),
      color: "#A11208",
    }
  ]
}

const exo_2023: number[] = Qtd_2023.map((item) => parseInt(item.exoneracoes))
const nome_2023: number[] = Qtd_2023.map((item) => parseInt(item.nomeacoes))
const total_2023: number[] = Qtd_2023.map((item) => parseInt(item.total))
const exo_porcen: number = (exo_2023[0] / total_2023[0]) * 100
const nome_porcen: number = (nome_2023[0] / total_2023[0]) * 100

const pie = {
  options: {
    labels: ['Nomeações', 'Exonerações'],
    colors: ["#FCA622", "#A11208"]
  },
  series: [nome_porcen, exo_porcen]
}

const total = [exo_2023, nome_2023]

function PesquisaMunicipios() {
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
                <input type="text" name="municipio" id="municipio" placeholder="Busque um município..."/>
                <input type="submit" value="Buscar"/>            
            </div>          
          </div>
        </div>
        <div className={styles.middleDiv}>
            <div className={styles.left}>  
                <Total quantity={total}/>
            </div>         
        </div>
        <div className={styles.lowerDiv}>
          <Chart options={column.options} series={column.series} type="bar" labels="" width={750} height={400} />
          <div className={styles.pieGraph}>
            <h2 className={styles.graphTitle}>Exonerações x Nomeações em 2023</h2>
            <Chart options={pie.options} series={pie.series}type="pie" width={370}/>            
          </div>
      </div>
      </div>
    </div>
  )
}

export default PesquisaMunicipios