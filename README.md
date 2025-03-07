# Walmart Sales Prediction

## 📌 Project Overview
This project aims to predict weekly sales for Walmart stores using historical data. By leveraging **Exploratory Data Analysis (EDA)** and **Machine Learning (Regression Models)**, we identify key factors influencing sales, such as **holidays, CPI, unemployment rate, and temperature**.

## 📂 Dataset
The dataset consists of Walmart store sales data with the following key features:
- **Store**: Store number (1-45)
- **Weekly_Sales**: Sales for a given week (Target Variable)
- **Holiday_Flag**: Whether the week includes a holiday (1 = Holiday, 0 = Non-Holiday)
- **Temperature**: Temperature in the region
- **CPI (Consumer Price Index)**: Economic indicator
- **Unemployment**: Regional unemployment rate

## 🛠 Tech Stack
- **Python**
- **Pandas, NumPy** (Data Manipulation)
- **Matplotlib, Seaborn** (Data Visualization)
- **Scikit-Learn** (Machine Learning)
- **Flask** (Web App Deployment)

## 📊 Exploratory Data Analysis (EDA)
- **Handling missing values**
- **Outlier detection and treatment**
- **Feature correlation analysis**
- **VIF analysis for multicollinearity**
- **Feature selection using F-test (ANOVA)**

## 🔮 Model Building
We trained and evaluated multiple regression models:
1. **Linear Regression**
2. **Random Forest Regressor**
3. **XGBoost Regressor**
4. **Decision Tree Regressor**

### **Model Evaluation Metrics**
- **R² Score** (Goodness of fit)
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**

## 📝 Future Enhancements
- Improve model accuracy using hyperparameter tuning
- Deploy using **Docker & Kubernetes**
- Add a feature for real-time data updates

## 🏆 Results & Insights
- **Holidays significantly impact sales**
- **Temperature has a slight negative correlation with sales**
- **Unemployment & CPI have low impact**
- **Random Forest & XGBoost performed best in terms of accuracy**

## 💡 Contributors
- **Akshay Yede** – Aspiring Data Scientist

## 📜 License
This project is **open-source** under the MIT License.
