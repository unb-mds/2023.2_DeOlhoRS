import styles from './MenuBar.module.css'
import logo from "../assets/logo.png"

function MenuBar() {
  return (
    <div className={styles.menuBar}>
      <br></br>
      <div className={styles.logo}>
        <img src={logo} className="logo" alt="" width="220" height="185"/>
      </div>
      <div className={styles.links}>
        <a href="url">Home</a>
        <a href="url">Pesquisa</a>
        <a href="url">Municípios</a>
        <a href="url">Anomalias</a>
        <a href="url">Sobre</a>
      </div>
    </div>
  )
}

export default MenuBar
