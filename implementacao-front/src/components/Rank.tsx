import styles from './Rank.module.css'

function Rank(props) {
  return (
    <div className={styles.RankTable}>
      <h2>{props.title}</h2>
      <ol type='1'>
        <li>{props.cities[0]} ................. {props.quantity[0]}</li>
        <li>{props.cities[1]} ................. {props.quantity[1]}</li>
        <li>{props.cities[2]} ................. {props.quantity[2]}</li>
        <li>{props.cities[3]} ................. {props.quantity[3]}</li>
        <li>{props.cities[4]} ................. {props.quantity[4]}</li>
      </ol>
    </div>
  )
}

export default Rank
