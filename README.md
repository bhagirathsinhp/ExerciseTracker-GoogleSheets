# 🏃 Workout Tracker

A Python automation project that logs **daily workout activities** into a Google Sheet using the **Nutritionix API** (for exercise data) and **Sheety API** (for Google Sheets integration).  

This project helps you **track your fitness progress** automatically by recording the exercises you perform, their duration, and the calories burned.

---

## 🚀 Features

- ✍️ Enter natural language exercise queries (e.g., *"ran 3 miles and did 30 minutes of yoga"*).
- 🔍 Uses **Nutritionix API** to parse exercises, duration, and calories burned.
- 📊 Automatically logs results to a **Google Sheet** via Sheety API.
- ⏱️ Stores both **date and time** for each exercise entry.
- 🔐 Secure credential handling via `.env` file.

---

## 🛠️ Technologies Used

- Python 3
- `requests` — For API calls
- `dotenv` — For environment variables
- **Nutritionix API** — To interpret exercise data
- **Sheety API** — To update Google Sheets

---

## 📂 Project Structure
    
    workout-tracker/
    │
    ├── main.py            # Main Python script
    ├── .env               # Environment variables (API keys, endpoints, auth)
    └── README.md          # Project documentation

---

## 🔑 Environment Variables

- Create a .env file in the project root with:

      NIX_API_ID=your_nutritionix_api_id
      NIX_API_KEY=your_nutritionix_api_key
      NIX_ENDPOINT=https://trackapi.nutritionix.com/v2/natural/exercise
      
      SHEETY_ENDPOINT=https://api.sheety.co/your_project/workouts
      SHEETY_AUTH=Bearer your_auth_token

  ---

  ## ▶️ How to Run

1. Install dependencies:

        pip install requests python-dotenv

2. Configure .env file with your Nutritionix and Sheety API credentials.
3. Run the script:

        python main.py

4. Input exercises in natural language when prompted:

         Tell me which exercises you did: ran 5 km and cycled for 30 minutes

5. Data will be automatically logged into your connected Google Sheet.

---

## 📜 Example Google Sheet Entry

<img width="1024" height="281" alt="Screenshot 2025-08-19 121935" src="https://github.com/user-attachments/assets/51ab520d-0ee9-4b6f-9bdd-189c1de03fad" />

---

## Learning Outcome

- This project demonstrates how to:

  - Use external APIs with authentication
  - Handle JSON data
  - Automate fitness tracking
  - Securely manage credentials with .env
 
---


