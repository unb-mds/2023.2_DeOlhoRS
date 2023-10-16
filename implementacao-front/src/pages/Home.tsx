import MenuBar from "../components/MenuBar"
import styles from "./Home.module.css"

function Home() {
  return (
    <div className={styles.container}>
      <MenuBar />
      <h1>Home Page</h1>
    </div>
  )
}

export default Home
