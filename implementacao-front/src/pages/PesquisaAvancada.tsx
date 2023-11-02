import LookupTable from "../components/LookupTable"
import MenuBar from "../components/MenuBar"
import styles from './PesquisaAvancada.module.css'
import TesteTabela from '../components/TesteTabela.jsx'

function PesquisaAvancada() {
  return (
    <div className={styles.container}>
        <MenuBar />
        <div className={styles.content}>
            <LookupTable />
            <TesteTabela />
        </div>
    </div>
  )
}

export default PesquisaAvancada
