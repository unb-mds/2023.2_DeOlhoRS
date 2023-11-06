import MenuBar from "../components/MenuBar"
import Total from "../components/Total"
import styles from "./PesquisaMunicipios.module.css"
import Chart from "react-apexcharts"
import { DataTable } from 'primereact/datatable'
import { useState } from 'react'
import { FilterMatchMode } from 'primereact/api'
import { InputText } from 'primereact/inputtext'

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
  options: {
    labels: ['Nomeações', 'Exonerações'],
    colors: ["#FCA622", "#A11208"]
  },
  series: [30, 70],
}

const total = [87465, 84577]

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