# 🚀 Fernando Orozco Avila – AI & ML Portfolio

Welcome to my portfolio repository! I’m a Commercial Director and Product Strategist with a technical edge—passionate about solving business problems through AI, machine learning, and statistical modeling.

This space showcases projects that blend customer-centric design, advanced analytics, and model-driven decision-making.

---

## 🧠 Key Projects
### 🛒 [SuperKart Sales Forecasting – ML Deployment for Retail Strategy](superkart-sales-forecasting)  
Machine Learning deployment project to forecast quarterly sales revenue across SuperKart’s national retail network:
- **Objective**: Build and **deploy a machine learning solution** that integrates predictive modeling into SuperKart’s decision-making systems for inventory optimization and regional sales strategy  
- Conducted **univariate and bivariate analysis**:
  - Numerical features: `Product_Weight` and `Product_MRP` showed strong positive correlations with sales (r = 0.74 and r = 0.79)  
  - `Product_Allocated_Area` was highly skewed and showed no correlation with sales  
  - Categorical features revealed imbalances: dominance of `OUT004`, `Medium` stores, `Tier 2` cities, and `Supermarket Type2`  
- Benchmarked multiple regressors; **Tuned XGBoost** selected for deployment with **R² = 0.940** and **RMSE ≈ 257**, offering the best balance between accuracy and generalization  
- Final **XGBoost model saved as a `.joblib` file** for reproducibility and integration into production workflows  
- Built and validated a **FastAPI backend** with three endpoints (welcome, single prediction, batch prediction), containerized with Docker, and hosted on **Hugging Face Spaces**  
  - **Backend Home URL**: [https://ferruss-superkart-backend.hf.space](https://ferruss-superkart-backend.hf.space)  
  - **Backend Prediction URL**: [https://ferruss-superkart-backend.hf.space/v1/predict](https://ferruss-superkart-backend.hf.space/v1/predict)  
  - **Backend Batch Prediction URL**: [https://ferruss-superkart-backend.hf.space/v1/batch_predict](https://ferruss-superkart-backend.hf.space/v1/batch_predict)  
- Developed a **Streamlit frontend** for interactive single predictions and batch CSV uploads, ensuring usability for both technical and business stakeholders  
  - **Frontend URL**: [https://ferruss-superkart-frontend.hf.space](https://ferruss-superkart-frontend.hf.space)  
- Recommended **WAPE** as the operational metric for production deployment due to its interpretability and scale-awareness  
- Business recommendations:
  - Expand high-performing categories (Fruits & Vegetables, Snack Foods, Dairy) and reassess underperforming ones (Seafood, Breakfast)  
  - Replicate successful practices from `OUT004` and Medium stores; investigate underperformance of High-sized stores  
  - Prioritize Tier 2 cities for growth while strengthening presence in Tier 1 and Tier 3  
  - Apply targeted discounts or bundling strategies to stimulate demand in underperforming categories  
- Demonstrates the value of **end-to-end ML deployment** (EDA → model selection → joblib export → backend API → frontend UI → Hugging Face hosting) for scalable, interpretable retail forecasting solutions


### 🛡️ [SafeGuard Helmet Detection – Computer Vision for Safety Compliance](helmet-detection-system)  
Image classification project using deep learning to detect helmet usage in industrial environments:
- Developed and compared four models: custom CNN, VGG16 base, VGG16 + FFNN, and VGG16 + FFNN + Data Augmentation  
- Final model (VGG16 + FFNN + Augmentation) achieved **100% accuracy, precision, recall, and F1-score** on validation and test sets  
- Applied **data augmentation** (rotation, shift, zoom, flip) to improve generalization on limited data  
- Prioritized **precision for the “No Helmet” class** to minimize false alerts and ensure reliable safety enforcement  
- Business recommendation: deploy final model for scalable, automated helmet compliance monitoring; expand dataset to improve robustness in real-world conditions  
- Demonstrates the effectiveness of **transfer learning and augmentation** in building reliable computer vision systems for workplace safety
### 🩺 [GenAI Medical Assistant – Prompt Engineering & RAG](genai-medical-assistant)  
Applied generative AI techniques to build a medical assistant that delivers context‑aware, clinically relevant responses using the Merck Manual as a trusted knowledge base:
- Compared **vanilla LLMs**, **prompt engineering**, and **retrieval‑augmented generation (RAG)** for diagnostic, drug, and treatment queries  
- Implemented **RAG pipeline**: PDF ingestion → text cleaning (removal of front matter & repetitive footers) → chunking with `RecursiveCharacterTextSplitter.from_tiktoken_encoder` → embeddings with **gte‑large** (Hugging Face) → storage in **Chroma** vector database → retrieval + generation with **llama‑2‑13b‑chat.Q5_K_M.gguf** via **llama.cpp**  
- **RAG consistently outperformed** other methods, producing grounded, precise, and context‑specific answers for complex cases (e.g., sepsis protocols, appendicitis treatment)  
- Prompt engineering improved reasoning clarity but lacked domain grounding; vanilla LLMs were fluent but risked hallucination  
- Key insight: **context‑aware retrieval is essential** for high‑precision medical tasks, while prompt engineering is better suited for educational or non‑critical use cases  
- Business recommendation: adopt **RAG‑based assistants** for clinicians to ensure reliable, evidence‑based decision support; use prompt‑engineered LLMs for general education and patient‑facing explanations  
- Demonstrates the feasibility of **scalable, compliant AI solutions in healthcare** that reduce information overload and improve decision‑making efficiency

### 🔧 [ReneWind Turbine Failure Detection](renewind-failure-detection)  
Classification modeling project using sensor‑derived turbine data to support predictive maintenance:
- Benchmarked 12 deep learning architectures with increasing complexity (SGD vs. Adam, dropout, BatchNormalization, He initialization, class weighting, EarlyStopping, and batch size tuning)  
- **Model 11** selected for deployment: deep regularized network with Adam optimizer, He initialization, class weighting ×2, and EarlyStopping (epoch ~17)  
- Achieved **~92% recall**, ensuring the vast majority of failures are detected before breakdowns  
- **Model 9** highlighted as an alternative when inspection costs are high, capturing ~86% of failures while reducing false positives  
- Key insight: **class weighting and EarlyStopping** were the most impactful strategies for balancing recall and generalization  
- Business recommendation: deploy Model 11 to minimize costly replacements and downtime; use Model 9 in cost‑sensitive inspection scenarios  
- Demonstrates the value of recall‑optimized models in operational contexts where **false negatives carry the highest financial risk**

### 🛂 [Visa Certification Prediction](easy-visa-prediction) 
EasyVisa Project Classification modeling project using historical visa application data to support certification decisions:
- Benchmarked Gradient Boosting, AdaBoost, and XGBoost with original, SMOTE-oversampled, and undersampled datasets
- GBM with original data selected for deployment based on highest F1 Score (0.821) and balanced recall–precision performance
- Key predictors included education level, job experience, prevailing wage, wage unit, continent of origin, and U.S. employment region
- GBM minimized false positives (18.3%) while maintaining strong recall (88.7%)
- Business recommendation: prioritize applicants with graduate education, prior experience, and yearly wages > $70K
- Highlights importance of F1-optimized models in regulatory contexts where fairness and efficiency must coexist

### 🏦 [Personal Loan Conversion Prediction – AllLife Bank](personal-loan-prediction/)
Decision tree classification model to support targeted marketing:
- Compares pre-pruning and post-pruning strategies  
- Post-pruned tree highlighted income, CCAvg, family size, and education as key predictors  
- Post-pruning reduced false positives by 30% while maintaining high accuracy  
- Business recommendation: focus campaigns on high-income, high-spending, graduate-educated segments with families ≥ 3  
- Suggests F1-optimized models for better recall–precision balance if misclassification risk rises

### 🍽️ [Exploratory Data Analysis – FoodHub](food-delivery-data-analysis) 
Exploratory data analysis project using real customer order data from a New York-based food delivery aggregator:
- Univariate, bivariate, and correlation analysis applied to cost, rating, cuisine, and delivery metrics
- Identified high weekend activity (71%) and dominance of American, Japanese, and Italian cuisines
- Found that 65% of customers are one-time buyers; proposed loyalty program and retargeting strategies
- Faster delivery times linked to higher customer ratings; weekday operations flagged for efficiency improvement
- High-cost orders (> $20) correlated with better ratings and higher margins—suggested upsell/cross-sell tactics
- Business recommendations focus on customer retention, rating incentives, delivery optimization, and margin expansion

---

## 🛠 Tools & Techniques

- **Languages:** C, Java, Python, SQL  
- **Libraries:** NumPy, Pandas. Matplotlib, Seaborn, Scikit-Learn, TensorFlow, OpenCV, Llama-ccp, Langchain  
- **Skills:** Feature engineering, recall optimization, cost modeling  
- **Visualization:** Tableau, Power BI  
- **Project Ops:** Structured logging, dashboarding, model lifecycle tracking

---

## 🎓 Background

- **Post Graduate Program – AI & Machine Learning** (2025), Texas McCombs  
- **MBA – Business Strategy & Ops**, ITAM  
- **B.S. in Systems Engineering**, ITESM  
- **Certifications:** SCRUM Master, Investment Strategies, Java Programming  

---

## ✉️ Let’s Connect

📧 fernando88@gmail.com  
🌍 [GitHub](https://github.com/fernando-orozcoa) • [LinkedIn](https://www.linkedin.com/in/forozco/)  

---

> ⚡ Data transforms strategy when it’s delivered with clarity and purpose. This portfolio is my journey to bring both to life.
