import styles from './LookupTable.module.css'

function LookupTable() {
  return (
    <div className={styles.LookupTable}>
      <table>
        <tr>
          <th scope="col">Nome</th>
          <th scope="col">CPF</th>
          <th scope="col">Cargo</th>
          <th scope="col">Ação</th>
          <th scope="col">Data</th>
        </tr>
        <br></br>
        <tr>
          <th scope="row">Cleiton</th>
          <td>000.000.000-00</td>
          <td>Analista de processos</td>
          <td>Nomeação</td>
          <td>25/09/2003</td>
        </tr>
        <tr>
          <th scope="row">Vanessa</th>
          <td>000.000.000-00</td>
          <td>Analista de processos</td>
          <td>Nomeação</td>
          <td>25/09/2003</td>
        </tr>
        <tr>
          <th scope="row">Fabiano</th>
          <td>000.000.000-00</td>
          <td>Analista de processos</td>
          <td>Nomeação</td>
          <td>25/09/2003</td>
        </tr>
      </table>
    </div>
  )
}

export default LookupTable