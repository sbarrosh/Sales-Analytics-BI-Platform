CREATE TABLE staging.stg_superstore AS
SELECT
    row_id,
    order_id,
    
    -- Convert dates
    TO_DATE(order_date, 'DD/MM/YYYY') AS order_date,
    TO_DATE(ship_date, 'DD/MM/YYYY') AS ship_date,

    ship_mode,
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region,
    product_id,
    category,
    sub_category,
    product_name,

    -- Clean metric
    sales::numeric(12,2) AS sales

FROM raw.superstore_raw;