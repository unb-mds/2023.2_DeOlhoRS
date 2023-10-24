import styles from './Total.module.css'

function Total(props) {
  return (
    <div className={styles.totalTable}>
      <h2>Total</h2>
      <ol>
        <li>{props.quantity[0]} Exonerados</li>
        <li>{props.quantity[1]} Nomeações</li>
      </ol>
    </div>
  )
}

export default Total