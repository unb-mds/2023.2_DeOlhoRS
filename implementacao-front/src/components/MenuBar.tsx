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
        <a className={styles.link} href="/">Home</a>
        <a className={styles.link} href="https://2023-2-squad08-p9gw-chx0naegn-my-team-1c098159.vercel.app/pesquisaAvancada">Pesquisa</a>
        <a className={styles.link} href="/pesquisaMunicipios">Municípios</a>
        <a className={styles.link} href="/anomalias">Anomalias</a>
        <a className={styles.link} href="/about">Sobre</a>
      </div>
    </div>
  )
}

export default MenuBar
