import styles from './Rank.module.css'

interface RankProps {
  title: string;
  cities: string[];
  quantity: number[];
}

function Rank({title, cities, quantity}: RankProps) {
  return (
    <div className={styles.RankTable}>
      <h2>{title}</h2>
      <ol type='1'>
        <li>{cities[0]} ................. {quantity[0]}</li>
        <li>{cities[1]} ................. {quantity[1]}</li>
        <li>{cities[2]} ................. {quantity[2]}</li>
        <li>{cities[3]} ................. {quantity[3]}</li>
        <li>{cities[4]} ................. {quantity[4]}</li>
      </ol>
    </div>
  )
}

export default Rank
