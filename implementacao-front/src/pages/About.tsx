import MenuBar from "../components/MenuBar"
import Profile from "../components/Profile"
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
            <div className={styles.upperProfiles}>
              <Profile name = 'Ana Borges' photo = 'https://avatars.githubusercontent.com/u/109738757?v=4'/>
              <Profile name = 'Bianca Patrocínio' photo = 'https://avatars.githubusercontent.com/u/70040539?v=4'/>
            </div>
           </div>
        </section>
    </div>
  )
}

export default About
