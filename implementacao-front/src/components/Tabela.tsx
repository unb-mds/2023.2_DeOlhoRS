import {
  MDBCol,
  MDBContainer,
  MDBRow,
  MDBTable,
  MDBTableBody,
  MDBTableHead,
} from "mdb-react-ui-kit";
import { useState } from "react";
import { Pessoas } from "../data/db";

function Tabela() {
  const [data] = useState(Pessoas);

  return (
    <MDBContainer>
      <div style={{ marginTop: "100px" }}>
        <MDBRow>
          <MDBCol size={12}>
            <MDBTable>
              <MDBTableHead dark>
                <tr>
                  <th scope="col">nome</th>
                  <th scope="col">cpf</th>
                  <th scope="col">cargo</th>
                  <th scope="col">acao</th>
                  <th scope="col">dia</th>
                </tr>
              </MDBTableHead>
              {data.length === 0 ? (
                <MDBTableBody className="align-center mb-0">
                  <tr>
                    <td colSpan={8} className="text-center mb-0">
                      No Data Found
                    </td>
                  </tr>
                </MDBTableBody>
              ) : (
                data.map((item) => (
                  <MDBTableBody>
                    <tr>
                      <td>{item.nome}</td>
                      <td>{item.cpf}</td>
                      <td>{item.cargo}</td>
                      <td>{item.acao}</td>
                      <td>{item.dia}</td>
                    </tr>
                  </MDBTableBody>
                ))
              )}
            </MDBTable>
          </MDBCol>
        </MDBRow>
      </div>
    </MDBContainer>
  );
}

export default Tabela;
