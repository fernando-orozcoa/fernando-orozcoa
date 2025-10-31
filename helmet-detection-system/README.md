# 🛡️ SafeGuard Helmet Detection System

This project focuses on building a computer vision system to automatically detect **safety helmet compliance** in industrial environments. By classifying images of workers as either wearing or not wearing helmets, the system helps enforce safety regulations, reduce manual oversight errors, and prevent head injuries in hazardous workplaces.

The final model achieved **100% accuracy, precision, recall, and F1-score** on validation data, demonstrating strong classification capability. The project showcases how **deep learning and transfer learning** can be applied to improve **workplace safety, operational efficiency, and compliance monitoring**.

---

## 🎯 Objective

The goal of this project is to develop an image classification model that detects whether a worker is **wearing a safety helmet**.  
Key business motivations include:

- **Reducing injury risk** by enforcing helmet compliance.  
- **Minimizing human error** in manual safety inspections.  
- **Scaling safety monitoring** across large industrial sites.  

In this context:  
- **True Positives (TP)** → Correctly identified non-helmeted workers → Enables intervention  
- **False Positives (FP)** → Helmeted workers misclassified as non-compliant → Unnecessary alerts  
- **False Negatives (FN)** → Missed non-compliance → Increased injury risk  

Precision for the "No Helmet" class was prioritized to minimize false alarms and ensure reliable enforcement.

---

## 📊 Dataset Summary

- **Source**: Internal dataset from SafeGuard Corp  
- **Total images**: 631 RGB images (200×200×3)  
  - `With Helmet`: 311 images  
  - `Without Helmet`: 320 images  
- **Split**:  
  - Training: 504 images (~80%)  
  - Validation: 63 images (~10%)  
  - Test: 64 images (~10%)  

Dataset characteristics:  
- Diverse industrial settings (construction, factories)  
- Variations in lighting, angles, and worker postures  
- Balanced class distribution → no resampling required  

---

## 🧠 Modeling Approach

Four models were developed and evaluated:

- **Model 1**: Custom CNN  
  - 3 Conv blocks + 2 Dense layers  
  - ~8.77M trainable parameters  
  - Strong baseline performance  

- **Model 2**: VGG16 Base  
  - Transfer learning with frozen convolutional layers  
  - Final Dense layer trained for binary classification  
  - Efficient and stable  

- **Model 3**: VGG16 + FFNN  
  - Added 2 Dense layers (256, 128) + Dropout  
  - Improved flexibility and decision boundaries  

- **Model 4**: VGG16 + FFNN + Data Augmentation  
  - Introduced rotation, shift, zoom, flip  
  - Enhanced generalization and robustness  

**Final Choice**: **Model 4**  
- Combines VGG16 feature extraction with FFNN and data augmentation  
- Achieved perfect scores across all metrics  
- Demonstrated strong generalization on unseen data  

---

## 🔑 Key Findings

- **Transfer learning** with VGG16 provided a powerful feature extraction backbone.  
- **Data augmentation** was critical for overcoming dataset limitations and reducing overfitting.  
- **Model 4** consistently outperformed simpler architectures and maintained zero misclassifications.  
- **Perfect scores** suggest the need for further testing on more diverse and noisy data to validate real-world performance.  

---

## 💼 Business Recommendations

- **Deploy Model 4** for helmet compliance monitoring:  
  - High precision ensures reliable alerts  
  - Scalable across industrial sites  
  - Robust to environmental variability  

- **Next Steps**:  
  - Acquire more diverse and representative data  
  - Test on real-time video feeds or edge devices  
  - Integrate with safety dashboards and alert systems  

---

## 📂 Folder Structure
```plaintext
safeguard-helmet-detection/
├── data/
├── notebooks/
├── models/
└── README.md
