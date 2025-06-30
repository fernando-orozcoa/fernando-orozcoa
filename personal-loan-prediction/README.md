# 🏦 Personal Loan Conversion Prediction – AllLife Bank

This project presents a decision tree–based classification model aimed at predicting which liability customers at AllLife Bank are most likely to adopt a personal loan. The objective is to enable precise targeting for future marketing campaigns by identifying high-propensity segments based on behavioral and demographic factors.

---

## 🎯 Objective

To predict personal loan adoption using decision tree classifiers and draw actionable insights for customer segmentation and campaign design. Special attention is placed on comparing **pre-pruning** and **post-pruning** techniques to assess model generalization and business impact.

---

## 🧾 Dataset Summary

- **Customer Profile Attributes:** Age, Income, Experience, Family size, Education, Mortgage, CCAvg  
- **Banking Behavior:** CD and securities accounts, online banking usage, external credit card usage  
- **Target Variable:** `Personal_Loan` (0 = No, 1 = Yes)  

---

## 🧪 Modeling Approach

- **Algorithm:** CART Decision Tree  
- **Techniques:**  
  - Pre-Pruned Tree with depth limit  
  - Post-Pruned Tree using cost-complexity pruning  
- **Metrics Evaluated:** Accuracy, False Positives, False Negatives, Model Depth, Leaf Count

---

## 📌 Key Findings

### ✅ Post-Pruned Tree
- **Root Split:** `Income ≤ 98.5` → most influential predictor  
- **Supporting Splits:** `CCAvg ≤ 2.95`, `Family`, `Education`  
- Depth: 4, Leaves: 6  
- **False Negatives:** 2 (0.13%)  
- **False Positives:** 95 (6.33%)  
- Better generalization and simplicity through pruning  
- Strong candidate model for deployment in future campaigns  

### ⚠️ Pre-Pruned Tree
- Overly constrained → underfitting  
- Higher false positive rate  
- Complexity didn’t translate into improved predictive power

---

## 📈 Business Recommendations

- Focus campaigns on segments with:
  - Higher income
  - Credit card average spending above $2,950
  - Families of 3 or more
  - At least a graduate-level education
- Minimize false positives to reduce customer fatigue and optimize outreach costs
- Consider models optimized for F1-score to balance recall and precision if misclassification cost becomes a concern

---

## 📂 Folder Structure

```plaintext
personal-loan-prediction/
├── data/
├── html/
├── notebooks/
├── src/
├── visuals/
├── README.md
└── decision_tree_final_model.pkl
