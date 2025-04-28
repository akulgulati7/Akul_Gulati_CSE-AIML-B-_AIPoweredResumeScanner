import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleScan = async () => {
    if (!selectedFile) {
      alert('Please select a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('resume', selectedFile);

    try {
      const response = await fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Server error!');
      }

      const data = await response.json();
      console.log(data);
      alert('Resume scanned successfully!');
    } catch (error) {
      console.error(error);
      alert(error.message);
    }
  };

  return (
    <div className="App">
      <div className="container">
        <h1>AI Resume Scanner Pro</h1>
        <p>Upload your resume and discover your top skills instantly!</p>

        <div className="upload-box">
          <input type="file" onChange={handleFileChange} />
          {selectedFile && <p>{selectedFile.name}</p>}
        </div>

        <button className="scan-button" onClick={handleScan}>
          🚀 Scan Resume
        </button>

        <footer>
          © 2025 AI Resume Scanner | Built with ❤️ by BTECH STUDENTS
        </footer>
      </div>
    </div>
  );
}

export default App;
