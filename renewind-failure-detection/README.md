# ReneWind Turbine Failure Detection

This project focuses on building predictive models to detect **wind turbine failures** before they occur, enabling **preventive maintenance** and reducing costly downtime. Using sensor-derived data, multiple deep learning architectures were tested and refined, with the final model achieving **~92% recall** on validation data—ensuring that the vast majority of failures are detected in advance.  

The project demonstrates how **machine learning and predictive maintenance** can directly translate into **operational efficiency, cost savings, and improved safety** in renewable energy operations.

---

## 🎯 Objective

The goal of this project is to develop a classification model that predicts **wind turbine generator failures**.  
Key business motivations include:

- **Reducing replacement costs** by detecting failures early and enabling repairs.  
- **Minimizing downtime** through predictive maintenance scheduling.  
- **Balancing inspection costs** against the risk of missed failures.  

In this context:  
- **True Positives (TP)** → Correctly predicted failures → Repair costs  
- **False Negatives (FN)** → Missed failures → Replacement costs (most expensive)  
- **False Positives (FP)** → False alarms → Inspection costs (least expensive)  

---

## 📊 Dataset Summary

- **Source**: Confidential sensor data (ciphered for privacy)  
- **Training set**: 20,000 observations  
- **Test set**: 5,000 observations  
- **Features**: 40 predictors (environmental + turbine component signals)  
- **Target**: Binary classification  
  - `1` = Failure  
  - `0` = No Failure  

Data preprocessing included:  
- Median imputation for missing values  
- Exploratory analysis with boxplots to identify class-separating features  
- Stratified train/validation/test split to preserve class balance  

---

## 🧠 Modeling Approach

A series of **12 models** were developed, each iteration introducing refinements in architecture, optimization, and training strategy:

- **Models 1–5**: Baseline dense networks with SGD → switched to Adam optimizer (recall improved from ~0.69 → ~0.80).  
- **Models 6–8**: Added depth, dropout, BatchNormalization, and He initialization (recall ~0.82).  
- **Model 9**: Introduced **balanced class weights** → recall ~0.83.  
- **Model 10**: Amplified class 1 weight ×2 → recall peaked at ~0.93 (slight overfit risk).  
- **Model 11**: Same as 10 + **EarlyStopping** → recall ~0.91, stable and efficient.  
- **Model 12**: Smaller batch size (64), 200 epochs with EarlyStopping → recall ~0.90, similar to Model 11.  

**Final Choice**: **Model 11**  
- Deep, regularized architecture with BatchNorm, Dropout, He init  
- Adam optimizer (lr = 0.0001)  
- Class 1 weight ×2  
- EarlyStopping at epoch ~17  

---

## 🔑 Key Findings

- **Class weighting** was the single most impactful technique for improving recall.  
- **EarlyStopping** prevented overfitting and ensured efficient training.  
- **Model 11** achieved the best balance:  
  - **Recall ≈ 0.91–0.92**  
  - Stable convergence  
  - Strong generalization  
- **Model 9** provides a more balanced option when inspection costs are high:  
  - Recall ≈ 0.86  
  - Fewer false positives → fewer unnecessary inspections  

---

## 💼 Business Recommendations

- **Adopt Model 11** for deployment:  
  - Captures ~92% of failures, minimizing costly replacements.  
  - Supports preventive maintenance scheduling, improving uptime and safety.  
  - Efficient training and reproducibility through EarlyStopping.  

- **Use Model 9** in scenarios where inspection costs are critical:  
  - Captures ~86% of failures while reducing false alarms.  
  - Provides a cost-efficient balance between recall and inspection overhead.  

- **Next Steps**:  
  - Perform **threshold tuning** to optimize precision–recall trade-offs.  
  - Integrate **cost-based evaluation** (repair vs. replacement vs. inspection).  
  - Deploy with monitoring and interpretability tools (e.g., SHAP).  

---

## 📂 Folder Structure
