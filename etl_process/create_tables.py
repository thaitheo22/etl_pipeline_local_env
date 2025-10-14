import pandas as pd 
import delivery_tools


# create table rules
# 1. PK-FK have same datatype 
# 2. inject data into dim tables (parent tables) first
# 3. alter or update columns having PK-FK -> must drop PK-FK relationship first \


delivery_tools.pure_sql_execute(
    """DROP TABLE IF EXISTS sale.staging_sale_order"""
)

delivery_tools.pure_sql_execute(
    """
    CREATE TABLE IF NOT EXISTS sale.staging_sale_order(
        invoice_number BIGINT NOT NULL, 
        sale_person VARCHAR(225) NOT NULL, 
        distribution_channel INT NOT NULL, 
        customer_name VARCHAR(225) NOT NULL, 
        customer_gender VARCHAR(10),
        birth_year INT, 
        product_name VARCHAR(225) NOT NULL,
        product_color VARCHAR(225) NOT NULL, 
        product_size VARCHAR(10) NOT NULL,
        product_category VARCHAR(225) NOT NULL, 
        quantity INT NOT NULL, 
        unit_price FLOAT NOT NULL,
        order_date DATE NOT NULL, 
        ship_interval INT NOT NULL 
    )
    """
)    
    
 
    
    


