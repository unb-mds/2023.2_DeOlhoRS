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
      <MDBRow>
        <MDBCol size={4}>
          <input
            type="text"
            placeholder="Pesquisar nome..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </MDBCol>
        <MDBCol size={2}>
          <MDBBtn onClick={handleSearch} color="primary">
            Pesquisar
          </MDBBtn>
        </MDBCol>
      </MDBRow>
      <MDBRow>
        <MDBCol size={12}>
          <MDBTable>
            <MDBTableHead dark>
              <tr>
                <th scope="col">Nome</th>
                <th scope="col">Cargo</th>
                <th scope="col">Ação</th>
                <th scope="col">Data</th>
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
                    <td>{item.nome}</td>
                    <td>{item.cargo}</td>
                    <td>{item.acao}</td>
                    <td>{item.data}</td>
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