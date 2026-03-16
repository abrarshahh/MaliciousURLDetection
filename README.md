# Malicious URL Detection

A machine learning-powered web application built with Django that classifies URLs to detect malicious intent. The application leverages a Random Forest classifier trained on URL features to identify various types of threats.

## 🌟 Features

- **Real-time URL Scanning**: Enter any URL to get an instant safety classification.
- **Machine Learning Classification**: Uses a trained Random Forest model (`RF_model`) along with a TF-IDF vectorizer (`vecotrizer.pkl`).
- **Multiple Threat Categories**: Classifies URLs into one of the following four categories:
  - **Benign**: Safe and normal URLs.
  - **Defacement**: URLs associated with websites that have been compromised or altered.
  - **Malware**: URLs that host or distribute malicious software.
  - **Phishing**: URLs designed to steal sensitive information by mimicking legitimate entities.
- **Continuous Integration / Web Interface**: Simple and intuitive Django Web Interface (`WebApp/`) for submitting queries and displaying results.

## 📂 Project Structure

- `model.ipynb`: Jupyter Notebook containing the data exploration, preprocessing, model training, and evaluation steps for the Random Forest classifier.
- `WebApp/`: The Django web application directory structure.
  - `manage.py`: Django command-line utility for administrative tasks.
  - `appDeploy/`: The main Django app containing views and routing.
    - `views.py`: Contains the core logic to load the `.pkl` models (`RF_model.pkl`, `vecotrizer.pkl`), preprocess the user input, make a prediction, and return the result to the template.
  - `templates/`: HTML templates for the web interface (`home.html`, `result.html`).

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed on your system. You will need the following libraries:
- Django
- pandas
- scikit-learn
- pickle (built-in)

You can install the required packages using pip:

```bash
pip install django pandas scikit-learn
```

### Running the Web Application

1. Open your terminal or command prompt.
2. Navigate to the `WebApp` directory:
   ```bash
   cd WebApp
   ```
3. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
4. Open your web browser and visit `http://127.0.0.1:8000/` to access the application.

## 🧠 How it Works

1. **Input**: The user submits a URL string via the web interface (`home.html`).
2. **Vectorization**: The backend receives the input and transforms the textual URL data into numerical features using a pre-trained TF-IDF vectorizer (`vecotrizer.pkl`).
3. **Prediction**: The vectorized input is passed to the trained Random Forest model (`RF_model.pkl`), which predicts the URL's class.
4. **Output**: The integer prediction is mapped to its corresponding human-readable label (Benign, Defacement, Malware, or Phishing) and displayed to the user (`result.html`).
