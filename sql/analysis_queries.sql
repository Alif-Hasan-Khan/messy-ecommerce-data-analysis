-- refresh

CREATE DATABASE ecommerce_analysis;

USE ecommerce_analysis;

USE ecommerce_analysis;

CREATE TABLE ecommerce_sales (
    ID INT,
    Customer_Name VARCHAR(100),
    Order_ID VARCHAR(50),
    Order_Date DATE,
    Product VARCHAR(100),
    Category VARCHAR(50),
    Quantity INT,
    Price DECIMAL(10,2),
    Payment_Method VARCHAR(50),
    Status VARCHAR(50),
    Total DECIMAL(12,2)
);
USE ecommerce_analysis;

SHOW TABLES;


USE ecommerce_analysis;

SELECT COUNT(*) AS total_rows
FROM ecommerce_sales;

SELECT *
FROM ecommerce_sales
LIMIT 10;



-- 1. Basic dataset overview

SELECT 
    COUNT(*) AS total_orders,
    COUNT(DISTINCT Customer_Name) AS total_customers,
    COUNT(DISTINCT Product) AS total_products
FROM ecommerce_sales;

-- 2. Revenue Analysis

SELECT 
    ROUND(SUM(Total), 2) AS total_revenue,
    ROUND(AVG(Total), 2) AS average_order_value,
    ROUND(MIN(Total), 2) AS minimum_order_value,
    ROUND(MAX(Total), 2) AS maximum_order_value
FROM ecommerce_sales;


-- 3. Sales by Category

SELECT 
    Category,
    COUNT(*) AS total_orders,
    ROUND(SUM(Total), 2) AS total_revenue
FROM ecommerce_sales
GROUP BY Category
ORDER BY total_revenue DESC;

-- 4. Sales by Product

SELECT 
    Product,
    Category,
    COUNT(*) AS total_orders,
    ROUND(SUM(Total), 2) AS total_revenue
FROM ecommerce_sales
GROUP BY Product, Category
ORDER BY total_revenue DESC;

-- 5. Sales by Payment Method

SELECT 
    Payment_Method,
    COUNT(*) AS total_orders,
    ROUND(SUM(Total), 2) AS total_revenue
FROM ecommerce_sales
GROUP BY Payment_Method
ORDER BY total_revenue DESC;
-- 6. Order Status Analysis

SELECT 
    Status,
    COUNT(*) AS total_orders,
    ROUND(SUM(Total), 2) AS total_revenue
FROM ecommerce_sales
GROUP BY Status
ORDER BY total_orders DESC;

-- 7. Monthly Sales Analysis

SELECT 
    DATE_FORMAT(Order_Date, '%Y-%m') AS month,
    COUNT(*) AS total_orders,
    ROUND(SUM(Total), 2) AS total_revenue
FROM ecommerce_sales
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY month;

-- 8. Top 5 Products by Revenue

SELECT 
    Product,
    ROUND(SUM(Total), 2) AS total_revenue
FROM ecommerce_sales
GROUP BY Product
ORDER BY total_revenue DESC
LIMIT 5;
