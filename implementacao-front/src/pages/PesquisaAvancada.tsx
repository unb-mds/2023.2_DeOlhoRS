import MenuBar from "../components/MenuBar";
import styles from "./PesquisaAvancada.module.css";
//import TesteTabela from '../components/TesteTabela.jsx'

function PesquisaAvancada() {
  return (
    <div className={styles.container}>
      <MenuBar />
      {/*<div className={styles.content}>
        <h1 className={styles.titulo}>Pesquisa Avançada</h1>
        <TesteTabela />
      </div>*/}
    </div>
  );
}

export default PesquisaAvancada;
