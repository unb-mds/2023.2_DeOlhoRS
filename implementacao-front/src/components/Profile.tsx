import styles from './Profile.module.css'

function Profile(props) {
  return (
    <div className={styles.profile}>
        <p>{props.name}</p>
        <img className={styles.profilePictures} src={props.photo} alt="anaBorges" />
    </div>
  )
}

export default Profile
