# 🛒 SuperKart Sales Forecasting – Robust Revenue Prediction for Retail Strategy

## 📌 Problem Statement

Accurate sales forecasting is critical for retail organizations to optimize inventory, plan regional operations, and reduce risks in the sales pipeline.  
SuperKart, a retail chain operating supermarkets and food marts across tier cities, partnered with a data science firm to build and deploy a **scalable forecasting solution**.  
The objective is to **predict quarterly outlet-level sales revenue** using historical data, enabling better decision-making across supply chain, marketing, and finance.

---

## 📊 Data Overview

- **Rows**: 8,763  
- **Columns**: 12 (5 numeric, 7 categorical)  
- **Missing Values**: None  

### Key Features:
- **Product_Weight**: Mean = 12.65 kg, Std = 2.22, Range = 4–22  
- **Product_Allocated_Area**: Mean = 0.0688, skewed distribution  
- **Product_MRP**: Mean = 147.03, Range = 31–266  
- **Store_Establishment_Year**: Centered around 2002, max = 2009  
- **Product_Store_Sales_Total (Target)**: Mean = 3,464, Range = 33–8,000  

---

## 🔎 Exploratory Analysis

### Univariate Insights
- Most numeric features are well-behaved (`Product_Weight`, `Product_MRP`)  
- Skewness observed in `Product_Allocated_Area` and `Product_Store_Sales_Total`  
- Categorical imbalance: dominance of `OUT004`, `Medium` stores, `Tier 2` cities, and `Supermarket Type2`

### Bivariate Insights
- Strong positive correlation:  
  - `Product_Weight` vs Sales (r = 0.74)  
  - `Product_MRP` vs Sales (r = 0.79)  
- No correlation between `Product_Allocated_Area` and Sales  
- High-performing categories: Fruits & Vegetables, Snack Foods, Dairy  
- Underperforming categories: Seafood, Breakfast  
- Sales concentrated in stores established in 2009

---

## 🤖 Model Selection

- **Baseline Models**: Random Forest, Bagging → high training accuracy but moderate overfitting  
- **Tuned Models**: Introduced regularization → improved generalization  
- **Best Models**:
  - **Tuned Bagging Regressor**: Highest validation R² = 0.941  
  - **Tuned XGBoost Regressor**: R² = 0.940, RMSE ≈ 257, smallest train–validation gap (0.017)  
- **Final Choice**: **Tuned XGBoost** selected for deployment due to superior generalization and stability

---

## ⚙️ Deployment

### 🔙 Backend (FastAPI + Docker)
- **Endpoints**:
  - `/` → Welcome message  
  - `/predict` → Single product prediction  
  - `/predict_batch` → Batch prediction via CSV upload  
- **Environment**: Python 3.13.2, Dockerized for reproducibility  
- **Requirements**: `requirements.txt` ensures dependency consistency  
- **Hosting**: Hugging Face Space for API deployment

### 🖥️ Frontend (Streamlit)
- **Single Prediction**: Form input → POST request → predicted revenue displayed  
- **Batch Prediction**: CSV upload → backend processing → collective results returned  

---

## 📈 Evaluation Metrics

- **Model comparison**: R² used to benchmark explanatory power  
- **Operational metric**: WAPE chosen for production (scale-aware, interpretable)  
- **Diagnostics**: RMSE and MAE used to monitor error magnitude and distribution  

---

## 🔍 Actionable Insights

- **Data Preprocessing**: StandardScaler applied to normalize numeric features  
- **Feature Engineering**: Store age derived from establishment year; rare product types grouped  
- **Bias Awareness**: Monitor overrepresentation of OUT004, Medium stores, Tier 2 cities  
- **Revenue Drivers**: Product_Weight and Product_MRP are key predictors  
- **Operational Readiness**: Batch endpoint validated for large-scale forecasting  

---

## 💼 Business Recommendations

- **Category Management**: Expand high-performing categories (Fruits & Vegetables, Snack Foods, Dairy); reassess low-performing ones (Seafood, Breakfast)  
- **Store Strategy**: Replicate successful practices from OUT004 and Medium stores; investigate underperformance of High-sized stores  
- **Market Expansion**: Prioritize Tier 2 cities; strengthen presence in Tier 1 and Tier 3  
- **Promotional Tactics**: Apply discounts to underperforming categories or bundle them with top sellers  
- **Inventory Optimization**: Use forecasts to align stock levels with expected demand  

---

## 📁 Repository Structure
```plaintext
superkart-sales-forecasting/
│
├── backend_files/
│   ├── app.py
│   ├── xgb_tuned_model.joblib
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── notebooks/
│   └── Full_Code_SuperKart_Model_Deployment_Notebook.ipynb
│
├── html/
│   └── Full_Code_SuperKart_Model_Deployment_Notebook.html
│
└── README.md
```

---

## 🚀 Outcome

This project demonstrates the deployment of a **scalable, interpretable regression system** for retail revenue forecasting.  
It bridges **exploratory data analysis, model benchmarking, and full-stack deployment** to deliver actionable insights and operational value for SuperKart’s national retail strategy.
