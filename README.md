# Dynamic Pricing Model for Used Cars   

This project is all about creating a **smart pricing system** for used cars, helping **dealerships** and **online platforms** price cars in a way that’s **competitive, fair, and profitable**.  

✅ The goal is to ensure:  
- **Customers** get a good deal   
- **Companies (dealerships)** maximize profits   
- **Prices reflect** both the car's true value and market conditions 
## CRISP-DM Framework

1️⃣ [**Business Understanding**](#Business-Understanding) – Business Understanding of the used car market. \
2️⃣ [**Data Understanding**](#Data-Understanding) – Explored the dataset, key features, and issues like missing values. \
3️⃣ [**Data Preparation**](#Data-Preparation) – Cleaned, transformed, and preprocessed data for modeling.  \
4️⃣ [**Modeling**](#Modeling) – Build predictive models using machine learning to estimate the best car prices. \
5️⃣ [**Evaluation**](#Modeling) – Monitored model performance.  \
6️⃣ **Deployment** –  (in future) Implement the model into websites/apps for making it accesable for everyone. 

This structured approach ensures a **scalable, accurate, and business-impactful solution**.  

## Business Understanding  

#### 1️⃣ Market Overview: Used Car Industry in India  
The used car market in India is growing fast due to:  

- **Affordability** – More middle-class buyers prefer second-hand cars.  
- **Online Marketplaces** – Platforms like OLX, CarDekho, Cars24.  
- And many...

#### 2️⃣ Key Problems  
- **Overpricing** – Reduces sales and slows inventory movement.  
- **Underpricing** – Leads to loss for dealers.  
- **Slow Sales** – Cars remain unsold, increasing storage costs.  
- **Lack of Price Transparency** – Customers hesitate due to unpredictable pricing.  

#### 3️⃣ Who Benefits?  
- **Dealerships & Online Platforms** – Need a pricing tool to maximize profits.  
- **Car Buyers** – Want fair pricing and transparency.  
- **Car Sellers** – Need competitive pricing to sell their old cars faster.  

#### 4️⃣ Business Benefits  
- **Higher Sales Conversions**  
- **Better Profit Margins** 
- **Optimized Inventory Management**  
- **Data-Driven Pricing**

## Data Understanding

#### 1️⃣ Data Sources  
- **Historical Sales Data** – Prices of sold used cars.   
- Dataset is taken from **Kaggle** platform.

#### 🔹 **Dataset Features**

- **Brand:** Car manufacturer  
- **Model:** Specific car model
- **Year:** Manufacturing year of the vehicle 
- **Age:** Age of the vehicle in years  
- **kmDriven:** Total kilometers driven by the vehicle  
- **Transmission:** Type of transmission (M/A)  
- **Owner:** Ownership status (1/2)  
- **FuelType:** Type of fuel
- **PostedDate:** When the car listing was posted  
- **AdditionalInfo:** Extra details about the vehicle  
- **AskPrice:** Listed price in Indian Rupees (₹)  

#### 2️⃣ Exploratory Data Analysis (EDA) Overview  

![Tableau_Dashboard_image](https://github.com/gagandeepsingh04/Dynamic_pricing_of_used_cars/blob/main/Tableau%20Dashboard%20screeenshort.png)

- **Descriptive Statistics:-** \
    **Observations**:
    - `Year` (1986 - 2024) → Dataset includes cars from 1986 to 2024.
    - `Age` (0 - 38 years) → Some cars are very old, others are brand new.
![year_vs_askPrice](https://github.com/gagandeepsingh04/Dynamic_pricing_of_used_cars/blob/main/yearVsPrice.png)
- **Categorical Data Analysis:-** \
    **Observations**:
    - `Brand` (39 unique values) → 39 different car brands (e.g., Maruti Suzuki is the most frequent).
    - `Model` (400 unique values) → High variety of car models (e.g., City is most common).
    - `Transmission` (2 unique values: Manual, Automatic) → Majority are manual (4666 cars).
    - `Owner` (2 unique values: 1, 2) → Most are first-owner (4596 cars).
    - `FuelType` (3 unique values: Petrol, Diesel, Hybrid/CNG) → Diesel is most common (3520 cars).
    - `PostedDate` (12 unique values) → Most listings are recent (Nov-24 is most frequent).
- **Missing Values** – `kmDriven` have some missing values, replaced by median.
- **Outliers & Anomalies** – remove outliers from both `age` and `kmDriven`.
- **Binning of data** - binned data of `Age` and `Year`
- **Log Transformed** - `kmDriven`, `AskPrice`.
![log_transformed_kmDriven](https://github.com/gagandeepsingh04/Dynamic_pricing_of_used_cars/blob/main/logTransformed_kmDriven.png)
![log_transformed_AskPrice](https://github.com/gagandeepsingh04/Dynamic_pricing_of_used_cars/blob/main/logTransformed_askPrice.png)
- **Feature Relationship** – `Age` and `Year` shows good relationship with `AskPrice`.
- **Feature Distributions Analysis** – checked distribution of `AskPrice`, `Age`, `Year` and `kmDriven`.
- **Removed Duplicate Rows**

## Data Preparation  

#### 1️⃣ Feature Selection
`Brand`, `Year`, `Age`, `log_kmDriven`, `Transmission`, `Owner`, `FuelType`, `PostedMonth`, `AskPrice`

#### 2️⃣ Feature Engineering  
- Encoding Categorical Variables  
`Brand`, `Transmission`, `FuelType`, `PostedMonth`

#### 3️⃣ Data Splitting  
- **Train-Test Split** – 80% for training, 20% for testing.
- 
## Modeling

#### 1️⃣ Choosing the Right Model  
Since we are predicting car prices (a continuous variable), this is a regression problem. Possible models:  

- **Simple Linear Regression**
- **Multiple Linear Regression**
- **polynomial Regression**

#### 2️⃣ Model Training & Hyperparameter Tuning
- Findout the Best Degree of the Polynomial Regression.
- Uses Regularization (Lasso/Ridge) to prevent overfitting.

![polynomial_model_graph](https://github.com/gagandeepsingh04/Dynamic_pricing_of_used_cars/blob/main/polynomial_model_graph.png)
![SVR_graph](https://github.com/gagandeepsingh04/Dynamic_pricing_of_used_cars/blob/main/SVR_graph.png)
![XGBoost_graph](https://github.com/gagandeepsingh04/Dynamic_pricing_of_used_cars/blob/main/XGBoost_graph.png)

#### 3️⃣ Performance Metrics of Best Model

| Metric | Value |
|---|---|
| MAE (Mean Absolute Error) | 0.29 |
| MSE (Mean Squared Error) | 0.17 |
| R² Score | 0.81 |

![feature_importance_in_XGBoost](https://github.com/gagandeepsingh04/Dynamic_pricing_of_used_cars/blob/main/feature_importance.png)
![graphical_compare_models](https://github.com/gagandeepsingh04/Dynamic_pricing_of_used_cars/blob/main/model_performance_graph.png)

## Model Deployed on Streamlit
link: https://dynamicpricingofusedcars-ofbx77mzyn7cixnvkbrmfz.streamlit.app/

![Model Deployed Image](https://github.com/gagandeepsingh04/Dynamic_pricing_of_used_cars/blob/main/model_deployed.png)
