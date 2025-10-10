# 🩺 GenAI Medical Assistant – Prompt Engineering & RAG

This project explores the development of a **Medical Assistant** powered by **Generative AI techniques**—specifically **Prompt Engineering** and **Retrieval-Augmented Generation (RAG)**. The assistant is designed to help healthcare professionals quickly access **reliable, context-aware, and clinically relevant information** from trusted medical references such as the **Merck Manual of Diagnosis and Therapy**.  

The project demonstrates how **domain-grounded AI** can address the challenges of **information overload, diagnostic support, and treatment planning**, ultimately improving **decision-making efficiency and patient outcomes**.

---

## 🎯 Objective

The goal of this project is to build a **RAG-based AI solution** that:  

- Provides **diagnostic assistance** by surfacing symptoms, differential diagnoses, and treatment options.  
- Supplies **drug information** including trade names and therapeutic uses.  
- Supports **treatment planning** with first-line and alternative options.  
- Offers **specialty knowledge** for complex conditions (e.g., endocrine disorders).  
- Delivers **critical care protocols** for time-sensitive emergencies (e.g., sepsis management).  

By combining **prompt engineering** for structured reasoning and **RAG** for domain grounding, the assistant ensures **accuracy, clarity, and clinical relevance**.

---

## 📊 Dataset Summary

- **Source**: *The Merck Manual of Diagnosis and Therapy, 19th Edition (2011)*  
- **Format**: PDF with ~4,000 pages across 23 sections  
- **Content**: Disorders, diagnostic steps, treatments, and drug information  
- **Preprocessing**:  
  - Removal of non-clinical front matter (cover, index, disclaimers)  
  - Cleaning repetitive footers to avoid embedding noise  
  - Chunking with `RecursiveCharacterTextSplitter.from_tiktoken_encoder`  
    - `chunk_size ≈ 1000 tokens`  
    - `chunk_overlap ≈ 100 tokens`  

---

## 🧠 Modeling Approach

Three methodologies were compared:

- **Vanilla LLMs**  
  - Strength: Detailed, fluent responses  
  - Limitation: May hallucinate or lack contextual specificity  

- **Prompt Engineering**  
  - Strength: Structured, step-by-step reasoning  
  - Limitation: Still relies on model’s internal knowledge, not always domain-grounded  

- **Retrieval-Augmented Generation (RAG)**  
  - Strength: Context-aware, clinically precise, grounded in Merck Manual  
  - Limitation: Requires preprocessing and retriever quality  

**Pipeline Overview**:  
1. **Document ingestion** → PDF parsing & cleaning  
2. **Chunking & embedding** → Vector database storage  
3. **Retriever** → Fetches top-k relevant chunks  
4. **LLM generation** → Combines user query + retrieved context  
5. **Evaluation** → Groundedness & relevance scoring  

---

## 🔑 Key Findings

- **RAG consistently outperformed** vanilla LLMs and prompt-only methods in accuracy and contextual relevance.  
- **Prompt Engineering** improved clarity and reasoning but could not guarantee domain fidelity.  
- **Vanilla LLMs** were informative but risked hallucination.  
- **Groundedness & Relevance evaluators** favored context-only derivation, but need refinement to ensure alignment with **current clinical standards**.  

---

## 💼 Business Recommendations

- **For clinicians**: Deploy **RAG-based assistants** to ensure timely, context-rich, and clinically precise responses.  
- **For education/general use**: Use **Prompt Engineering** to provide structured, accessible explanations for non-critical contexts.  
- **Evaluator refinement**: Enhance groundedness/relevance scoring to prioritize **up-to-date, evidence-based medical standards**.  
- **Scalability**: Extend pipeline to integrate additional trusted sources (e.g., PubMed, WHO guidelines).  

---

## 📂 Folder Structure
```plaintext
genai-medical-assistant/
├── data/                # Raw PDF and cleaned text
├── notebooks/           # Experiments and evaluations
├── html/ 
└── README.md

