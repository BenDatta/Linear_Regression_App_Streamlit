# 🛍️ E-Commerce Spending Predictor 💰

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

> 🎯 **Predict customer spending with the power of Linear Regression!** This interactive web app helps e-commerce businesses forecast yearly customer spending based on engagement metrics.

---
The app predicts customer spending based on **4 key metrics**:

1. **⏱️ Average Session Length** - How long customers stay per session (30-40 minutes)
2. **📱 Time on App** - Minutes spent on the mobile app (10-15 minutes)
3. **🌐 Time on Website** - Minutes spent on the website (35-41 minutes)
4. **🎖️ Length of Membership** - How many years they've been a customer (0-6 years)

Simply adjust the sliders, hit **Predict**, and watch the magic happen! ✨

---

## 🚀 Quick Start  

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/BenDatta/Linear_Regression_App_Streamlit.git
cd Linear_Regression_App_Streamlit
```

2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Run the app**
```bash
streamlit run ecommerce_app.py
```

4️⃣ **Open your browser** 🌐  
The app will automatically open at `http://localhost:8501`

---

## 📁 Project Structure

```
📦 Linear_Regression_App_Streamlit
├── 🎯 ecommerce_app.py              # Main Streamlit application
├── 📊 linear_reg_ecom.ipynb         # ML model training & EDA
├── 📈 Ecommerce.csv                 # Customer dataset
├── 🤖 ecommerce_model_pipeline.pkl  # Trained model (generated)
├── 📋 requirements.txt              # Python dependencies
└── 📖 README.md                     # You are here!
```

---

## 🔬 The Science Behind It

### Model Development Process

1. **📥 Data Loading** - Customer e-commerce dataset with 500+ records
2. **🔍 Exploratory Data Analysis** - Correlation analysis, pairplots, and joint plots
3. **🎯 Feature Selection** - 4 key predictive features identified
4. **⚙️ Pipeline Creation** - StandardScaler + LinearRegression
5. **🎓 Model Training** - Fitted on historical customer data
6. **💾 Model Serialization** - Saved as pickle file for deployment
7. **🌐 Web Deployment** - Interactive Streamlit interface

### 📊 Technologies Used

- **Streamlit** - Web app framework
- **scikit-learn** - Machine learning model & preprocessing
- **Pandas** - Data manipulation
- **NumPy** - Numerical computations
- **Seaborn & Matplotlib** - Data visualization
- **Pickle** - Model serialization

---

<div align="center">

### ⭐ Star this repo if you found it helpful! ⭐

**Made with 💻 and ☕**

</div>
