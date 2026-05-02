# 📊 Customer Segmentation using Self-Organizing Maps (SOM)

## 📌 Project Overview

This project implements a Self-Organizing Map (SOM) to perform customer segmentation using unsupervised learning. The model maps high-dimensional customer data onto a 2D grid, enabling visualization of patterns and identification of distinct customer groups.

---

## 🎯 Objective

* Perform clustering using SOM (Kohonen Network)
* Reduce dimensionality of customer data
* Identify meaningful customer segments
* Generate actionable business insights

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* MiniSom

---

## 📂 Project Structure

```id="c4k8kw"
SOM-Assignment/
│
├── data/
│   └── data.csv
│
├── src/
│   ├── preprocess.py
│   ├── som_model.py
│   ├── visualize.py
│   ├── cluster.py
│
├── main.py
├── requirements.txt
├── README.md
├── report.pdf
```

---

## 📦 Dataset

* Dataset: Customer dataset (Wholesale / Credit Card)
* Source: Kaggle / UCI Repository
* Features: Customer purchasing behavior attributes

---

## 🔁 Workflow

1. Data Loading
2. Data Cleaning (handling missing values)
3. Feature Scaling (Min-Max normalization)
4. SOM Training (MiniSom)
5. Visualization (U-Matrix, Heatmap)
6. Clustering using K-Means
7. Cluster Analysis & Insights

---

## 🧠 Model Details

* SOM Grid: 10 × 10
* Learning Rate: 0.5
* Neighborhood Function: Gaussian
* Training Iterations: 1000
* Distance Metric: Euclidean

---

## 📊 Visualizations

* Correlation Heatmap
* U-Matrix (distance map)
* <img width="713" height="574" alt="image" src="https://github.com/user-attachments/assets/767f4a85-12a7-4f2e-8187-da132ca8d00f" />
* Cluster Analysis (mean values)
* <img width="917" height="716" alt="Screenshot 2026-05-01 105914" src="https://github.com/user-attachments/assets/ca115aa2-bfa2-4e62-8691-e33e31a9d724" />

---

## 📈 Results

* Successfully identified 3 customer segments
* Clear cluster separation observed in U-Matrix
* Meaningful patterns discovered in customer behavior

---

## 💼 Business Insights

* High-value customers → premium offers
* Low-value customers → discounts & promotions
* Moderate customers → upselling opportunities

---

## 🚀 How to Run

### 1. Install Dependencies

```id="2jjg3u"
pip install -r requirements.txt
```

### 2. Run Project

```id="1l52ks"
python main.py
```

---

## 📌 Conclusion

SOM is an effective tool for customer segmentation, providing both clustering and visualization capabilities. It helps businesses understand customer behavior and make data-driven decisions.
