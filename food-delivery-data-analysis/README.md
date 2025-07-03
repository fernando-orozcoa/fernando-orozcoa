# 🛵 Data Analysis - FoodHub

This project explores customer ordering behavior, delivery efficiency, and restaurant performance using FoodHub’s order dataset. As a Data Scientist for a food aggregator in New York, I conducted an end-to-end analysis to uncover patterns in customer preferences, identify drivers of high satisfaction, and evaluate operational bottlenecks. The insights helped shape strategic recommendations around customer loyalty, cuisine promotion, delivery optimization, and revenue growth. The analysis leveraged Python tools (Pandas, Matplotlib, Seaborn) to deliver actionable outcomes aimed at enhancing FoodHub’s business model and customer experience.

---
## 🔍 Objective

FoodHub, a food aggregator platform, wanted to leverage its historical order data to enhance app performance, streamline delivery, and identify key restaurant and cuisine trends. As a Data Scientist, I was tasked with answering critical business questions to guide product strategy, marketing, and operations.

---
## 🧾 Dataset Summary
The FoodHub dataset contains order-level data from a New York-based food delivery aggregator platform. Each row represents a unique customer order and includes attributes related to the customer, restaurant, cuisine type, order cost, time of the week, customer ratings, food preparation time, and delivery duration. The dataset enables detailed analysis of:
* **Customer behavior:** frequency, loyalty, and weekend vs. weekday trends
* **Restaurant and cuisine performance:** popularity, revenue contribution, and concentration of demand
* **Operational metrics:** food preparation and delivery times across different customer satisfaction levels
* **Revenue and cost analysis:** identifying high-margin orders and patterns in order value distribution
* **Customer satisfaction:** exploring correlations between order characteristics and ratings
  
---

## 🧪 Analytical Approach

To extract business-relevant insights from FoodHub’s order dataset, I followed a structured data analysis pipeline focused on both descriptive and relational exploration:

### 🔍 1. Univariate Analysis
Examined the distribution of individual variables to understand customer and operational patterns:
- Order volume trends across weekdays vs. weekends
- Most popular restaurants and cuisine types
- Customer rating distribution and frequency of missing ratings
- Cost and duration (preparation/delivery) ranges and outliers

### 🧭 2. Bivariate Analysis
Explored relationships between pairs of variables to uncover business-critical dynamics:
- Cuisine type vs. frequency of orders
- Order cost vs. customer rating trends
- Restaurant popularity vs. revenue impact
- Day of the week vs. delivery time

### 📈 3. Correlation Analysis
Quantified statistical relationships between numerical variables to identify influential drivers:
- Evaluated how delivery time and preparation time relate to customer satisfaction
- Assessed the influence of order value on received ratings
- Identified mild negative correlation between long delivery times and high ratings

---

## 💡 Key Findings

- **Customer Behavior**:  
  - 71% of orders were placed on weekends, signaling time-based promotional opportunities.  
  - 65% of customers placed only a single order—indicating a major opportunity for retention initiatives.

- **Cuisine & Restaurant Trends**:  
  - American (31%), Japanese (25%), and Italian (16%) were the most popular cuisines.  
  - Shake Shack was the top performer by volume and revenue.  

- **Customer Ratings**:  
  - 39% of orders lacked a rating—limiting feedback channels.  
  - Higher-cost orders tended to earn better ratings (5-star orders averaged ~$17).  
  - 4-star orders had the lowest delivery times, suggesting quick delivery improves satisfaction.

- **Delivery Performance**:  
  - Weekend deliveries were ~6 minutes faster than weekday deliveries (22.5 vs 28.3 min).  
  - Delivery times showed moderate correlation with ratings and should be optimized further.

- **Revenue Insights**:  
  - Total net revenue: **$6,166.30**  
  - Orders over $20 made up 29% of the total but drove disproportionately high profit.

---

## 🧭 Strategic Recommendations

1. **Boost Rating Collection**  
   - Add post-delivery reminders or incentives for customer reviews.  

2. **Promote Undervalued Restaurants**  
   - Bundle them with popular cuisine promos or offer “first try” discounts.  

3. **Develop a Loyalty Program**  
   - Offer discounts on second orders, push notifications for new items, and reward repeat buyers.

4. **Improve Delivery Operations**  
   - Strengthen weekday delivery logistics and ensure adequate staffing during high-volume weekends.

5. **Maximize Revenue Through Upsells**  
   - Create combo deals to nudge basket value past the $20 threshold and promote high-margin add-ons.

---

## 🧰 Tools & Techniques

- Python (Pandas, NumPy, Seaborn, Matplotlib)  
- Jupyter Notebook  
- Data Cleaning, EDA, Correlation Analysis, Business Insight Storytelling

---

## 📈 Business Impact

This project showcases how rigorous data analysis can inform business strategy in the on-demand food sector. From identifying operational inefficiencies to uncovering high-performing customer segments and maximizing revenue potential, the findings translate directly into strategic levers for growth.
