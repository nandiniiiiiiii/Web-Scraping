import { useEffect, useState } from 'react'
import axios from 'axios';

function Demo() {
    const [value, setValue] = useState('');
    const handleSearch = async(e) => {
        const data = { value }
        console.log(data);
        e.preventDefault(); 
        try {
          await axios.post('http://localhost:3000/data', data);
          alert('Data submitted successfully!');
        }
        catch (error) {
          console.error('Error submitting data:', error);
          alert('Failed to submit data.');
        }
    }
    return (
        <div>
            <h3>Hello</h3>
            <input
                type='text'
                placeholder='Enter item to be searched'
                onChange={(e) => setValue(e.target.value)}
            />
            <button
                onClick={handleSearch}
            >Search</button>
        </div>
    )
}


export default Demo
