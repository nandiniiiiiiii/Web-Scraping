import './App.css'
import { Route, Routes } from 'react-router-dom'
import Demo from './components/Demo';

function App() {
  return (
    <div>
      <Routes>
        <Route path='/' element={<Demo />}></Route>
      </Routes>
    </div>
  )
}

export default App
