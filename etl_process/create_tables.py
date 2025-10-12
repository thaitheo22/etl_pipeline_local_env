import pandas as pd 
import delivery_tools


# create table rules
# 1. PK-FK have same datatype 
# 2. inject data into dim tables (parent tables) first
# 3. alter or update columns having PK-FK -> must drop PK-FK relationship first 

delivery_tools.pure_sql_execute(
    """
    CREATE SCHEMA IF NOT EXISTS sale;

    CREATE TABLE IF NOT EXISTS sale.dim_customer_info (
        customer_id SERIAL PRIMARY KEY,
        customer_name VARCHAR(225) NOT NULL,
        gender VARCHAR(10),
        birth_year DATE
    );

    CREATE TABLE IF NOT EXISTS sale.dim_product (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(225) NOT NULL,
        color VARCHAR(10) NOT NULL,
        size VARCHAR(10) NOT NULL,
        category VARCHAR(50) NOT NULL,
        unit_price INT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS sale.dim_saleperson (
        saleperson_id SERIAL PRIMARY KEY,
        saleperson_name VARCHAR(225) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS sale.dim_channel (
        channel_id SERIAL PRIMARY KEY,
        channel_number INT NOT NULL
    );
    """
)


delivery_tools.pure_sql_execute(
    """
    CREATE TABLE IF NOT EXISTS sale.fact_sale_order(
        invoice_number BIGINT PRIMARY KEY,
        saleperson_id INT NOT NULL,
        channel_id INT NOT NULL,
        customer_id INT NOT NULL,
        product_id INT NOT NULL,
        product_color VARCHAR(10) NOT NULL,
        product_size VARCHAR(10) NOT NULL,
        quantity INT NOT NULL,
        unit_price INT NOT NULL
    );             
    """
)


foreign_key_sql = [
    """
    ALTER TABLE sale.fact_sale_order
    ADD CONSTRAINT fk_fact_customer
    FOREIGN KEY (customer_id)
    REFERENCES sale.dim_customer_info(customer_id)
    ON DELETE CASCADE;
    """,
    """
    ALTER TABLE sale.fact_sale_order
    ADD CONSTRAINT fk_fact_saleperson
    FOREIGN KEY (saleperson_id)
    REFERENCES sale.dim_saleperson(saleperson_id)
    ON DELETE CASCADE;
    """,
    """
    ALTER TABLE sale.fact_sale_order
    ADD CONSTRAINT fk_fact_product
    FOREIGN KEY (product_id)
    REFERENCES sale.dim_product(product_id)
    ON DELETE CASCADE;
    """,
    """
    ALTER TABLE sale.fact_sale_order
    ADD CONSTRAINT fk_fact_channel
    FOREIGN KEY (channel_id)
    REFERENCES sale.dim_channel(channel_id)
    ON DELETE CASCADE;
    """
]

for fk in foreign_key_sql:
    delivery_tools.pure_sql_execute(fk)











