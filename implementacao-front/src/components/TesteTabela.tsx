import { Column } from "primereact/column";
import { DataTable } from "primereact/datatable";
import "primereact/resources/primereact.min.css";
import "primereact/resources/themes/lara-light-indigo/theme.css";
import { useState } from "react";
import styles from "./TesteTabela.module.css";

{
  /*import { useState } from 'react'
import { FilterMatchMode } from 'primereact/api'
import { InputText } from 'primereact/inputtext'*/
}

function TesteTabela() {
  const [filtro, setFiltro] = useState();

  const data = [
    {
      nome: "Cleiton Rasta Robson",
      cpf: "000.000.000-00",
      cargo: "Analista de Processos",
      acao: "Nomeação",
      dia: "25/09/2003",
    },
    {
      nome: "Cleiton Robson Rastah",
      cpf: "000.000.000-01",
      cargo: "Analista financeiro",
      acao: "Nomeação",
      dia: "25/09/2007",
    },
    {
      nome: "Cleiton Arrasta",
      cpf: "000.000.000-02",
      cargo: "Analista de Processos",
      acao: "Exoneração",
      dia: "25/09/2010",
    },
    {
      nome: "Cleiton Arrasta",
      cpf: "000.000.000-02",
      cargo: "Analista de Processos",
      acao: "Exoneração",
      dia: "25/09/2010",
    },
    {
      nome: "Cleiton Arrasta",
      cpf: "000.000.000-02",
      cargo: "Analista de Processos",
      acao: "Exoneração",
      dia: "25/09/2010",
    },
  ];

  return (
    <div className={styles.container}>
      <div className={styles.inputs}>
        <form>
          <input
            type="text"
            name="nome"
            id="nome"
            placeholder="Nome ou CPF..."
          />
          <input type="text" name="cargo" id="cargo" placeholder="Cargo..." />
          <input type="submit" value="Buscar" />
        </form>
      </div>
      <div className={styles.tabela}>
        <DataTable value={data} filters={filtro}>
          <Column field="nome" header="Nome" />
          <Column field="cpf" header="CPF" />
          <Column field="cargo" header="Cargo" />
          <Column field="acao" header="Ação" />
          <Column field="dia" header="Data" />
        </DataTable>
      </div>
    </div>
  );
}

export default TesteTabela;
