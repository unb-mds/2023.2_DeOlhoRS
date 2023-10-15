import styles from './MenuBar.module.css'
import logo from "../assets/logo.png"

function MenuBar() {
  return (
    <div className={styles.menuBar}>
      <br></br>
      <div className={styles.logo}>
        <img src={logo} className="logo" alt="" width="220" height="185"/>
      </div>
    </div>
  )
}

export default MenuBar
