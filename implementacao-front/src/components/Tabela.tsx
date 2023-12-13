import {
  MDBCol,
  MDBContainer,
  MDBRow,
  MDBTable,
  MDBTableBody,
  MDBTableHead,
  MDBBtn,
} from "mdb-react-ui-kit";
import { useState, useEffect } from "react";
import { data2 } from "../data/nomesLimpos2";
import styles from "./Tabela.module.css";

// Interface para a estrutura dos dados a serem exibidos na tabela
interface TabelaData {
  data: string;
  nome: string;
  cargo: string;
  acao: string;
}

function Tabela() {
  const [data, setData] = useState<TabelaData[]>([]);
  const [searchTerm, setSearchTerm] = useState<string>("");

  useEffect(() => {
    // A tabela deve estar vazia inicialmente
    setData([]);
  }, []);

  const handleSearch = () => {
    const formattedData: TabelaData[] = [];

    for (const [dia, valores] of Object.entries(data2)) {
      const nomeados = valores.nomes_nomeados
        .filter((nome) => nome.toLowerCase().includes(searchTerm.toLowerCase()))
        .map((nome) => ({
          data: dia,
          nome: nome.split(" - ")[0],
          cargo: nome.includes("-") ? nome.split(" - ")[1] : "não especificado",
          acao: "nomeação",
        }));

      const exonerados = valores.nomes_exonerados
        .filter((nome) => nome.toLowerCase().includes(searchTerm.toLowerCase()))
        .map((nome) => ({
          data: dia,
          nome: nome.split(" - ")[0],
          cargo: nome.includes("-") ? nome.split(" - ")[1] : "não especificado",
          acao: "exoneração",
        }));

      formattedData.push(...nomeados, ...exonerados);
    }

    setData(formattedData);
  };

  return (
    <MDBContainer style={{ marginTop: "10px" }}>
      <MDBRow gap={3}>
        <MDBCol size={5}>
          <input
            type="text"
            placeholder="Pesquisar nome..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </MDBCol>
        <MDBCol size={2} style={{ marginLeft: '60px' }}>
          <MDBBtn onClick={handleSearch} rounded color="success">
          Pesquisar
          </MDBBtn>
        </MDBCol>
      </MDBRow>
      <MDBRow>
        <MDBCol size={12}>
          <MDBTable>
            <MDBTableHead light>
              <tr>
                <th scope="col"><p className={styles.body}>Nome</p></th>
                <th scope="col"><p className={styles.body}>Cargo</p></th>
                <th scope="col"><p className={styles.body}>Ação</p></th>
                <th scope="col"><p className={styles.body}>Data</p></th>
              </tr>
            </MDBTableHead>
            <MDBTableBody>
              {data.length === 0 ? (
                <tr>
                  <td colSpan={4} className="text-center mb-0">
                    Nenhum dado encontrado
                  </td>
                </tr>
              ) : (
                data.map((item, index) => (
                  <tr key={index}>
                    <td className={styles.body}>{item.nome}</td>
                    <td className={styles.body}>{item.cargo}</td>
                    <td className={styles.body}>{item.acao}</td>
                    <td className={styles.body}>{item.data}</td>
                  </tr>
                ))
              )}
            </MDBTableBody>
          </MDBTable>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
}

export default Tabela;