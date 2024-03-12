import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [value,setValue] = useState("");
  const handleSearch = () =>{
    const data = {value}
    useEffect(()=>{
      axios
            .post('http://localhost:3000/api/v1/book/data',data)
            .then((res) => {
              console.log(res.data);
            })
            .catch((error) => {
              alert('an error occur please check console');
              console.log(error);
            })
    })

  }
  return (
    <div>
      <h3>Hello</h3>
      <input 
        type='text' 
        placeholder='Enter item to be searched'
        onChange={(e)=>setValue(e.target.value)}
      />
      <button 
        onClick={handleSearch}
      >Search</button>
    </div>
  )
}

export default App
