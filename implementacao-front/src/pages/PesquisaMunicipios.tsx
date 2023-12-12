import { Autocomplete, TextField } from "@mui/material";
import { useEffect, useState } from "react";
import MenuBar from "../components/MenuBar";
import styles from "./PesquisaMunicipios.module.css";

interface Municipio {
  nome: string;
}

function PesquisaMunicipios(): JSX.Element {
  const [municipios, setMunicipios] = useState<string[]>([]);

  const onSearch = async () => {
    try {
      const response = await fetch(
        "https://servicodados.ibge.gov.br/api/v1/localidades/estados/RS/municipios"
      );
      const data: Municipio[] = await response.json();
      setMunicipios(data.map((municipio) => municipio.nome.toLowerCase()));
    } catch (error) {
      console.error("Erro ao buscar municípios:", error);
    }
  };
  useEffect(() => {
    onSearch();
  }, []);

  return (
    <div className={styles.container}>
      <MenuBar />
      <div className={styles.content}>
        <div className={styles.upperDiv}>
          <div className={styles.left}>
            <h1 className={styles.subTitle}>Pesquisa por município</h1>
            <br></br>
            <br></br>
            <div className={styles.inputs}>
              <Autocomplete
                disablePortal
                id="combo-box-demo"
                options={municipios}
                sx={{ width: 300 }}
                renderInput={(params) => (
                  <TextField {...params} label="Busque um município..." />
                )}
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default PesquisaMunicipios;