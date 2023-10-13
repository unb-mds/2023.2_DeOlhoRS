import MenuBar from "../components/MenuBar"
import styles from "./About.module.css"

function About() {
  return (
    <div className={styles.container}>
        <MenuBar/>
        <section className={styles.content}>
           <h1>Conheça um pouco mais do nosso projeto!</h1> 
           <p>Este projeto é resultado da disciplina de Métodos de Desenvolvimento de Software, ministrada na Universidade de Brasília.</p>
           <hr />
           <p>O objetivo principal do projeto é contribuir para a transparência e responsabilidade governamental a partir da coleta de diários oficiais municipais de diferentes municípios do Rio Grande do Sul e analisar informações relacionadas a nomeações e exonerações de servidores públicos.</p>
           <hr />
           <h2>Equipe de estudantes desenvolvedores:</h2>
           <div className={styles.teamContainer}>
            aaaaaaaaaa
           </div>
        </section>
    </div>
  )
}

export default About
