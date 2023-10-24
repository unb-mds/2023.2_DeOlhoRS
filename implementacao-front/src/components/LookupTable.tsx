import styles from './LookupTable.module.css'

function LookupTable() {
  return (
    <div className={styles.LookupTable}>
      <table>
        <tr>
          <th>Nome</th>
          <th>CPF</th>
          <th>Cargo</th>
          <th>Anomalia</th>
        </tr>
      </table>
    </div>
  )
}

export default LookupTable