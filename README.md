# 🍽️ AI Nutrition Analyzer with Gemini AI  

The **AI Nutrition Analyzer** is a Streamlit-based application powered by **Google Gemini AI**.  
It analyzes food images to identify items, estimate portion sizes, calculate calories, break down macronutrients, and provide personalized dietary suggestions.  

This project demonstrates the use of **multimodal AI**, **nutritional analysis**, and **goal-based recommendations** for health and fitness tracking.  
<img width="1893" height="841" alt="image" src="https://github.com/user-attachments/assets/2c3b1ce2-40c9-45c8-a95e-66ed52edc831" />


---

## 🚀 Features  

- 🔍 **Food Recognition**  
  - Detects food items from uploaded images  
  - Supports multiple cuisines and preparation methods  

- ⚖️ **Portion & Calorie Estimation**  
  - Provides approximate grams or household measures  
  - Calculates calories per item and total meal calories  

- 📊 **Macronutrient Breakdown**  
  - Protein, Carbohydrates, Fat (per item & total)  

- ⚠️ **Allergen & Dietary Considerations**  
  - Flags likely allergens (nuts, dairy, gluten, etc.)  
  - Notes uncertainties when items are visually ambiguous  

- 🎯 **Goal-Oriented Insights**  
  - Choose from **Weight Loss, Muscle Gain, Maintenance**, or **General Info**  
  - Get quick portion guidance and healthy swap suggestions  

- 🖼️ **Streamlit UI**  
  - Upload food images (JPG, JPEG, PNG, WebP)  
  - Add custom notes (e.g., “homemade”, “restaurant serving”)  
  - Download analysis as a text file  

---

## 📂 Project Structure  

```
├── app.py            # Main Streamlit application
├── .env                 # API key storage 
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone 
```

### 2️⃣ Create Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Key  
Create a **`.env`** file in the root folder:  

```
GOOGLE_API_KEY=your_api_key_here
```

Get your API key from **Google AI Studio**.

### 5️⃣ Run the App  
```bash
streamlit run app.py
```

---

## 📊 Example Output  

```
============================================================
NUTRITION ANALYSIS
============================================================

Items Detected:
1) Grilled Chicken Breast — ~150g — ~250 kcal
   • Macros (est.): P ~45g, C ~0g, F ~5g
2) Brown Rice — ~1 cup (195g) — ~215 kcal
   • Macros (est.): P ~5g, C ~45g, F ~2g
3) Steamed Broccoli — ~100g — ~35 kcal
   • Macros (est.): P ~3g, C ~7g, F ~0g

Assumptions & Uncertainty:
• Chicken appears grilled with minimal oil; calories may vary ±10%  
• Rice portion estimated visually; possible 170–220g range  

Total Estimated Calories: ~500 kcal  

Notes & Tips:
• Balanced meal with protein and fiber  
• Consider adding healthy fats (avocado, nuts)  
```

---

## 🛠️ Technologies Used  

- **Python 3.10+**  
- **Google Gemini AI (`google-generativeai`)**  
- **Streamlit** (frontend)  
- **Pillow (PIL)** (image handling)  
- **dotenv** (API key management)  

---

## 📌 Future Enhancements  

- 📱 Mobile-friendly design  
- 🥗 Support for multiple food images per meal  
- 📊 Export nutrition logs to **CSV/Excel**  
- ☁️ Integration with fitness tracking apps  
- 🧠 Personalized nutrition advice using fine-tuned models  
