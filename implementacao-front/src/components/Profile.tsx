import styles from './Profile.module.css'

interface ProfileProps {
  name: string;
  photo: string;
}

function Profile({name, photo}: ProfileProps) {
  return (
    <div className={styles.profile}>
        <p>{name}</p>
        <img className={styles.profilePictures} src={photo} alt="fotoDeMembro" />
    </div>
  )
}

export default Profile
