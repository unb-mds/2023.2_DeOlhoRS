import MenuBar from "../components/MenuBar";
import styles from "./PesquisaAvancada.module.css";
//import TesteTabela from '../components/TesteTabela.tsx';
import Tabela from "../components/Tabela";
import { useState } from "react";
import { MDBBtn, MDBBtnGroup } from "mdb-react-ui-kit";

function PesquisaAvancada() {

  const [value, setValue] = useState("")

  return (
    <div className={styles.container}>
      <MenuBar />
      {/*<div className={styles.content}>
        <h1 className={styles.titulo}>Pesquisa Avançada</h1>
        <TesteTabela />
      </div>*/}
      <div className={styles.content}>
        <form>
          <input type="text" placeholder="Nome..." value={value} onChange={(e) => setValue(e.target.value)}/>
          <MDBBtnGroup>
            <MDBBtn>Pesquisar</MDBBtn>
          </MDBBtnGroup>
        </form>
        <Tabela></Tabela>
      </div>
    </div>
  );
}

export default PesquisaAvancada;
