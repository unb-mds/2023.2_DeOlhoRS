import React from 'react';
import BarChart from './BarChart';
import { Qtd_RS } from 'totalPorAno.json';

const App = () => {
  return (
    <div>
      <h1>Gráfico de Exonerações e Nomeações</h1>
      <BarChart data={Qtd_RS} />
    </div>
  );
};

export default App;