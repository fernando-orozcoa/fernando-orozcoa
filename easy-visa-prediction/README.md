# 🛂 Visa Certification Prediction – EasyVisa Project

This project presents a machine learning–based classification model aimed at predicting the likelihood of visa certification for foreign applicants based on employer and employee attributes. The goal is to support scalable, data-driven decision-making in high-volume certification workflows while surfacing interpretable insights for policy and operational refinement.

## 🎯 Objective

To predict visa certification outcomes using ensemble classifiers and derive actionable insights for applicant profiling. Special emphasis is placed on comparing sampling strategies and model architectures to optimize F1 Score and reduce misclassification risks.

## 🧾 Dataset Summary

- **Applicant Attributes**: Education level, job experience, training requirements, continent of origin  
- **Employer Attributes**: Number of employees, year of establishment, region of employment  
- **Compensation Details**: Prevailing wage, wage unit (hourly, monthly, yearly)  
- **Target Variable**: `case_status` (Certified = 1, Denied = 0)

## 🧪 Modeling Approach

- **Algorithms**: Gradient Boosting (GBM), AdaBoost, XGBoost  
- **Sampling Techniques**:
  - Original dataset  
  - Oversampling using **SMOTE**  
  - Undersampling using **RandomUnderSampler**  
- **Metrics Evaluated**: Accuracy, Precision, Recall, F1 Score, Confusion Matrix

## 📌 Key Findings

### ✅ GBM with Original Data
- **F1 Score**: 0.821 (highest across all models)  
- **Recall**: 88.7% → minimizes false negatives  
- **Precision**: 76.4% → balanced prediction quality  
- **False Positive Rate**: 18.3% (lower than XGBoost's 23.5%)  
- Strong generalization across training, validation, and test sets

### ⚠️ XGBoost with Oversampling
- **Recall**: 93.9% (highest)  
- **Precision**: 72.7%  
- **F1 Score**: 0.819  
- Higher false positive rate → risk of certifying unqualified applicants

## 📈 Business Recommendations

Prioritize applicants with:
- Graduate-level education (Master’s or PhD)  
- Prior job experience  
- Yearly wages above $70K  
- Employment in the Midwest region  
- Originating from Europe

Avoid profiles with:
- No formal education or experience  
- Hourly wage structures  
- Origins from South America, North America, or Oceania

Use F1-optimized models to balance recall and precision in high-stakes regulatory contexts. Consider ensemble methods with interpretable outputs for stakeholder alignment.

## 📂 Folder Structure
```plaintext
easyvisa-certification-prediction/
├── data/
├── notebooks/
├── src/
├── visuals/
├── html/
├── README.md
└── gbm_final_model.pkl

