import styles from './Total.module.css'

interface TotalProps {
  quantity: number[];
}

function Total({quantity} : TotalProps) {
  return (
    <div className={styles.totalTable}>
      <h2>Total Mapeado</h2>
      <ol className={styles.list}>
        <li>{quantity[0]} Nomeações</li>
        <li>{quantity[1]} Exonerações</li>
      </ol>
    </div>
  )
}

export default Total