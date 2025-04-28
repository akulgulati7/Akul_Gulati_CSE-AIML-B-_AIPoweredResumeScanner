from flask import Flask, request, jsonify
import os
import spacy
import pdfplumber
import docx2txt
import re
from flask_cors import CORS  # Important to allow React to connect!

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the Spacy NLP model
nlp = spacy.load('en_core_web_sm')

# Create 'resumes' folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_text(filepath):
    text = ''
    if filepath.endswith('.pdf'):
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    elif filepath.endswith('.docx'):
        text = docx2txt.process(filepath)
    return text

def extract_email(text):
    email_pattern = r'\S+@\S+'
    match = re.search(email_pattern, text)
    return match.group() if match else ''

def extract_phone(text):
    phone_pattern = r'\+?\d[\d\-\s]{7,}\d'
    match = re.search(phone_pattern, text)
    return match.group() if match else ''

def extract_education(text):
    education_keywords = ['B.Tech', 'M.Tech', 'MBA', 'B.Sc', 'M.Sc', 'PhD', 'Bachelor', 'Master']
    found = []
    for edu in education_keywords:
        if edu.lower() in text.lower():
            found.append(edu)
    return found

def extract_info(text):
    doc = nlp(text)
    name = ''
    skills = []
    experience = ''
    email = extract_email(text)
    phone = extract_phone(text)
    education = extract_education(text)

    skill_list = ['python', 'java', 'c++', 'machine learning', 'data analysis', 'deep learning', 'nlp', 'sql', 'html', 'css', 'javascript']
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            name = ent.text
            break

    text_lower = text.lower()
    for skill in skill_list:
        if skill in text_lower:
            skills.append(skill.capitalize())

    exp_match = re.search(r'(\d+)\+?\s+(years|yrs)', text_lower)
    if exp_match:
        experience = exp_match.group(0)

    return {
        'name': name,
        'skills': skills,
        'experience': experience,
        'email': email,
        'phone': phone,
        'education': education
    }

@app.route('/', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['resume']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    text = extract_text(file_path)
    info = extract_info(text)

    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
