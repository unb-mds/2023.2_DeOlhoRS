import MenuBar from "../components/MenuBar";
import styles from "./PesquisaAvancada.module.css";
//import TesteTabela from '../components/TesteTabela.tsx';
import Tabela from "../components/Tabela";

function PesquisaAvancada() {

  return (
    <div className={styles.container}>
      <MenuBar />
      {<div className={styles.content}>
        <h1 className={styles.titulo}>Pesquisa Avançada</h1>
        <div className={styles.lowerDiv}>
          <Tabela></Tabela>
        </div>
        <p>Atenção: Os dados referidos são apenas do ano de 2017.</p>
      </div>}
      <div className={styles.lowerDiv}>
        {/*<form>
          <input type="text" placeholder="Nome..." value={value} onChange={(e) => setValue(e.target.value)}/>
          <MDBBtnGroup>
            <MDBBtn>Pesquisar</MDBBtn>
          </MDBBtnGroup>
        </form>*/}
      </div>
    </div>
  );
}

export default PesquisaAvancada;
