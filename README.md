# Diabetes Prediction Website

A simple Flask web application for diabetes risk prediction using an ML model.

## Features

- HTML/CSS frontend for user input
- Python/Flask backend for prediction
- Logistic regression model trained on a synthetic dataset
- Easy local run and deploy-ready structure

## Run locally

1. Create and activate a Python environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
python app.py
```

4. Open `http://127.0.0.1:5000` in your browser.

## Deploy

This app can be deployed to any Python hosting provider that supports Flask.

- For Heroku, use the included `Procfile`.
- For Render, PythonAnywhere, or similar services, point to `app.py` and install `requirements.txt`.

## App structure

- `app.py` — Flask application and ML prediction logic
- `templates/` — HTML templates
- `static/style.css` — site styling
- `requirements.txt` — Python dependencies
