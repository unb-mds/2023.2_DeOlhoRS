import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import About from './pages/About'
import Home from './pages/Home';
import PesquisaAvancada from './pages/PesquisaAvancada';

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/pesquisaAvancada" element={<PesquisaAvancada />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
