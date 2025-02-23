# Flask Machine Learning API

This is a Flask-based API that serves a trained machine learning model for making predictions. The model was trained using Google Colab and exported as a `.joblib` file. The backend is deployed on **Render**, and the frontend (if applicable) can be deployed on **Vercel**.

## Features
- Accepts user input via a REST API.
- Loads a pre-trained machine learning model.
- Returns predictions based on input data.
- Deployed using **Render**.

---

## Project Structure
```
flask-backend/
│── app.py                # Flask API
│── requirements.txt      # Dependencies list
│── Procfile              # Render startup command
│── random_forest_model.joblib  # Trained model
└── README.md             # Documentation
```

---

## Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/flask-backend.git
cd flask-backend
```

### 2️⃣ Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask App Locally
```bash
python app.py
```
The API will run on `http://127.0.0.1:5000`.

---

## API Endpoints

### **1. Predict Endpoint**
**URL:** `/predict`  
**Method:** `POST`  
**Content-Type:** `application/json`  

#### **Request Body Example**
```json
{
  "distance": 500,
  "businesses": 10,
  "area": 2000
}
```

#### **Response Example**
```json
{
  "price": 150000
}
```

---

## Deployment

### **1️⃣ Deploy on Render**
1. Push your code to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```
2. Go to **Render** and create a **New Web Service**.
3. Connect your GitHub repository.
4. Set up the build and start commands:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Deploy**.
6. Once deployed, Render will provide an API URL like:
   ```
   https://your-backend.onrender.com
   ```

### **2️⃣ Connect React Frontend**
Update your frontend to call the API:
```javascript
const apiUrl = "https://your-backend.onrender.com/predict";
fetch(apiUrl, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ distance: 500, businesses: 10, area: 2000 }),
})
  .then((response) => response.json())
  .then((data) => console.log("Prediction:", data));
```

---

## Technologies Used
- **Flask** - Backend framework
- **Google Colab** - Model training
- **scikit-learn** - Machine learning
- **Render** - Deployment
- **Vercel** - Frontend deployment (if applicable)

---

## License
This project is licensed under the MIT License.

---

## Author
Pasan Athuluwage 
GitHub: [@MinjanaAP](https://github.com/MinjanaAP)