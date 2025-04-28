AI Powered Resume Scanner 

Team Members :
Akul Gulati (2301730136)
Krish Yadav (2301730130)
Vansh Dhaka (2301730108)
Anant Bhardwaj (2301730076)

Short Project Description :
An AI-powered web application that intelligently analyzes resumes and extracts key information like skills, experience, education, email, and phone number within seconds.
Built using React.js (frontend) and Flask (backend) with Natural Language Processing (NLP) techniques.

Technologies Used
Frontend:
React.js — JavaScript library for building user interfaces
HTML5 — Structuring the web pages
CSS3 — Styling and designing the frontend
Axios — Handling HTTP requests from frontend to backend
React Hooks — Managing component states and lifecycle

Backend:
Flask — Lightweight Python web framework
Python — Core backend programming language
spaCy — NLP library used for Name Entity Recognition (NER)
pdfplumber — Extracting text from PDF resumes
docx2txt — Extracting text from DOCX (Word) resumes
re (Regular Expressions) — For extracting emails, phone numbers, experience years
FPDF (optional) — To generate downloadable PDF analysis reports

Server Communication:
Flask API — REST API endpoint to receive and process resume files
JSON — Data exchange format between frontend and backend

Others:
Node.js & npm — Managing React dependencies
Visual Studio Code — Main code editor
Postman (optional) — For testing backend API separately
GitHub — Version control and project hosting


Steps to Run/Execute the Project
Clone or Download the Project
Download the project folder from GitHub or your shared files.
Make sure you have frontend and backend folders separately inside the main project directory.

Backend Setup (Flask API)
Step 1: Navigate to the backend folder
bash
Copy
Edit
cd backend
Step 2: Create a virtual environment (Recommended)
bash
Copy
Edit
python -m venv venv
Activate it:

On Windows:
bash
Copy
Edit
venv\Scripts\activate

On Mac/Linux:
bash
Copy
Edit
source venv/bin/activate
Step 3: Install required Python packages
bash
Copy
Edit
pip install -r requirements.txt
(or manually install necessary packages like Flask, pdfplumber, spacy, docx2txt)

Also make sure you have downloaded the spaCy model by running:

bash
Copy
Edit
python -m spacy download en_core_web_sm
Step 4: Start the Flask backend server
bash
Copy
Edit
python app.py
Flask server will start at http://127.0.0.1:5000

Backend is ready!

Frontend Setup (React.js)
Step 1: Open a new terminal window.
Navigate to the frontend folder:
bash
Copy
Edit
cd frontend
Step 2: Install node modules
bash
Copy
Edit
npm install
Step 3: Start the React frontend server
bash
Copy
Edit
npm start
React app will start at http://localhost:3000

Frontend is ready!

How to Use the Project
Open your browser and go to: http://localhost:3000
Click the Choose File button and select your resume (in .pdf or .docx format).
Click Scan Resume.
In a few seconds, the system will show your Name, Skills, Education, Experience, Email, and Phone Number!

Important Notes:
Make sure both frontend and backend servers are running at the same time.

Use only PDF or DOCX files (other types like .jpg will not work).

If any CORS issue occurs, you can install and use flask-cors in backend.


