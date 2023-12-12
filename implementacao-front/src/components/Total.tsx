import styles from './Total.module.css'

function Total(props) {
  return (
    <div className={styles.totalTable}>
      <h2>Total Mapeado</h2>
      <ol>
        <li>{props.quantity[1]} Exonerações</li>
        <li>{props.quantity[0]} Nomeações</li>
      </ol>
    </div>
  )
}

export default Total