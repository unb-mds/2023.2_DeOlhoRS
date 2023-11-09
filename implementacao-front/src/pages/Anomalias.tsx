import MenuBar from "../components/MenuBar"
import TesteTabela from "../components/TesteTabela"
import styles from "./Anomalias.module.css"

function Anomalias() {
  return (
    <div className={styles.container}>
        <MenuBar />
        <div className={styles.content}>
            <h1 className={styles.titulo}>Anomalias</h1>
            <p>Nesta seção você encontra informações adicionais e/ou atividades incomuns relacionadas a nomeações e exonerações em municípios do Rio Grande do Sul.</p>
            <TesteTabela />
        </div>
    </div>
  )
}

export default Anomalias
