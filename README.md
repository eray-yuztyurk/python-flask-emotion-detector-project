# Emotion Detection Web App (Flask)

This project is a simple web application that analyzes emotions in a text input. It was built as part of the **IBM Skills Network course final project**, where the goal was to combine a Python backend, an external NLP service, and a minimal browser interface.

The app sends user‑provided text to a cloud‑based NLP emotion model and returns the scores for the main emotions—**anger, disgust, fear, joy, sadness**—along with a calculated **dominant emotion**.

<img width="839" height="529" alt="image" src="https://github.com/user-attachments/assets/3d59db5c-93e2-4100-98e2-ec4db1c7f124" />

---

## Features

* Text input field for emotion analysis
* Flask backend exposing an `/emotionDetector` route
* Integration with an external Watson-based NLP emotion API
* Clean HTML interface with a small JavaScript helper script
* Returns both individual emotion scores and the dominant emotion
* Includes unit tests to validate emotion classification logic

---

## Tech Stack

* **Python 3**
* **Flask** for the backend web server
* **Requests** for API calls
* **HTML + JavaScript** for the frontend
* **Bootstrap** (CDN) for quick styling
* **unittest** for the test suite

---

## Project Structure

```
.
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py   # Core logic calling the NLP API
├── server.py                  # Flask routes and app setup
├── templates/
│   └── index.html             # Main user interface
├── static/
│   └── mywebscript.js         # Frontend JS logic
└── test_emotion_detection.py  # Unit tests
```

---

## How the App Works

1. The user opens the web page served by Flask.
2. The text entered in the input box is sent to `/emotionDetector` using JavaScript.
3. The backend calls the NLP API with the provided text.
4. The API responds with emotion scores.
5. Flask returns a formatted text response summarizing:

   * each emotion score
   * the dominant emotion
6. The result is displayed directly on the page.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

Create a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
# or
venv\Scripts\activate       # Windows
```

Install dependencies:

```bash
pip install flask requests
```

---

## Running the Application

Start the Flask server:

```bash
python server.py
```

Open the application in your browser:

```
http://localhost:5000/
```

Enter any text, click **Run Sentiment Analysis**, and the result will appear on the page.

---

## Running the Tests

```bash
python -m unittest test_emotion_detection.py
```

These tests check whether known example sentences correctly map to their expected dominant emotions.

---

## License Reference

This project includes instructional components originally provided through the IBM Skills Network learning platform.
Course materials are distributed under the **Apache License 2.0**, and this project follows the same licensing standard for compatibility.
The full license text can be found in the included `LICENSE` file.

---

## Notes

* The application relies on an external API; an internet connection is required.
* The NLP model is optimized for English text.
* Error handling can be expanded for production use.

---

