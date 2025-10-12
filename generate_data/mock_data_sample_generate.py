import rstr
import random

from faker import Faker
fake = Faker()


class Product:
    wearing_items = [
    # Tops
    "T-shirt", "Shirt", "Sweater", "Hoodie", "Jacket", "Coat",
    
    # Bottoms
    "Jeans", "Pants", "Shorts", "Skirt", "Leggings", "Trousers",

    # Footwear
    "Sneakers", "Sandals", "Boots", "Slippers", "Heels", "Loafers",

    # Headwear
    "Cap", "Hat", "Beanie", "Helmet", "Scarf", "Hood",

    # Accessories
    "Sunglasses", "Watch", "Bracelet", "Necklace", "Ring", "Earrings",

    # Sports / Special
    "Swimsuit", "Tracksuit", "Uniform", "Socks", "Tie", "Belt"
    ]

    category = ["Tops", "Bottoms", "Footwear", "Headwear", "Accessories", "Sports"]    
    
    category_ranges = {
    "Tops": wearing_items[0:6],
    "Bottoms": wearing_items[6:12],
    "Footwear": wearing_items[12:18],
    "Headwear": wearing_items[18:24],
    "Accessories": wearing_items[24:30],
    "Sports": wearing_items[30:36]
    }
    
    reverse_category_ranges = {}
    for cate, item_list in category_ranges.items():
        for item in item_list:
            reverse_category_ranges[item] = cate
            
    


    colors = ["Red", "Blue", "Green", "Black", "White", "Gray", "Yellow", "Navy", "Beige"]

    sizes = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]

    
    wearing_items_price = {
        # Tops
        "T-shirt": 15,
        "Shirt": 25,
        "Sweater": 35,
        "Hoodie": 40,
        "Jacket": 60,
        "Coat": 80,

        # Bottoms
        "Jeans": 50,
        "Pants": 45,
        "Shorts": 25,
        "Skirt": 30,
        "Leggings": 20,
        "Trousers": 40,

        # Footwear
        "Sneakers": 75,
        "Sandals": 30,
        "Boots": 90,
        "Slippers": 15,
        "Heels": 65,
        "Loafers": 55,

        # Headwear
        "Cap": 12,
        "Hat": 18,
        "Beanie": 10,
        "Helmet": 50,
        "Scarf": 20,
        "Hood": 25,

        # Accessories
        "Sunglasses": 70,
        "Watch": 150,
        "Bracelet": 45,
        "Necklace": 65,
        "Ring": 40,
        "Earrings": 35,

        # Sports / Special
        "Swimsuit": 40,
        "Tracksuit": 60,
        "Uniform": 55,
        "Socks": 8,
        "Tie": 20,
        "Belt": 25
    }

price_list = [price for price in Product.wearing_items_price.values()]


saleperson_list = [
'Christine Richardson',
'Richard Patel',
'Nicole Garcia',
'Joseph Brown',
'William Hughes',
'Christopher Wright',
'Nicole Harrington',
'Robin Callahan',
'Taylor Flores',
'Anthony Lee',
'Gregory Wheeler',
'Richard Steele',
'Mark Cummings',
'Susan Rivera',
'Jonathon King',
'Cynthia Bradshaw',
'Jeremy Cook',
'Marcus Guzman',
'Amy Fisher',
'Martin Johnson',
'Susan Werner',
'Amy Burke',
'Christopher Cook',
'Dawn Vaughan',
'Melissa Thomas',
'Randall Sims',
'Stephanie Martinez',
'Michael Mendoza',
'Hayden Henry',
'Linda Terrell',
'Casey Ortiz',
'Cynthia Sanchez',
'Ronald Johnson',
'Mark Richardson',
'Richard Johnson DVM',
'Carrie Smith',
'Anna Thomas',
'Mary King',
'Mr. Ricardo Holland',
'John Mendez',
'James Quinn',
'Mary Baker',
'Kyle Smith',
'Katelyn Wilkins',
'Rebecca Blackburn',
]

saleperson_list2 = [
'Robert Lee',
'Paul Foster',
'Caitlin Harvey',
'Kimberly Francis',
'Miguel Valdez',
'Mr. Angel Colon DVM',
'Kerry Wilson',
'Sean Morse',
'Stephen Saunders',
'Nancy Rivera',
'Lauren House',
'Jacob Mitchell',
'Franklin Silva',
'Kim Smith',
'Ryan Morris'
]


#---------------------------------------------------------------------------------------------
invoiceNum = []
salePerson = []
distributeChannel = []
customerName = []
customerGender = []
birthYear = []
productName = []
productColor = []
productSize =[]
productCategory = []
productQty = [] 
productUnitPrice = []
orderDate = []
shipInterval = []


data_dict = {
    "invoiceNum": invoiceNum,
    "salePerson": salePerson,
    "distributeChannel": distributeChannel,
    "customerName": customerName,
    "customerGender": customerGender,
    "birthYear": birthYear,
    "productName": productName,
    "productColor": productColor,
    "productSize": productSize,
    "productCategory": productCategory,
    "productQty": productQty,
    "productUnitPrice": productUnitPrice,
    "orderDate": orderDate,
    "shipInterval": shipInterval
}



for i in range(10000):
    
    invoiceNum.append(rstr.xeger(r'^\d{8}$'))
    salePerson.append(random.choice(saleperson_list))
    distributeChannel.append(random.choice([1,2,3,4,5,6,7,8,9])) # thêm giá trị vào đây
    
    
    customerName.append(fake.name())
    customerGender.append(random.choice(['F', 'M']))    
    birthYear.append(rstr.xeger(r'^(?:19[6-9][0-9])|20(?:0[0-9]|1[0-5])$'))
    
    #-----
    product_name = random.choice(Product.wearing_items)
    productName.append(product_name)
    #-----
    
    productColor.append(random.choice(Product.colors))
    productSize.append(random.choice(Product.sizes))
    
    productCategory.append(Product.reverse_category_ranges[product_name])
    
    productQty.append(random.choice(range(1,9)))
    productUnitPrice.append(Product.wearing_items_price[product_name])

    orderDate.append(rstr.xeger(r'^(?:0[1-9]|1[0-2])/(?:0[1-9]|[1-2][0-9]|30|31)/(?:2024|2025|2026)$')) # thêm ngày ở đây
    shipInterval.append(random.choice(range(2,9)))    
    
    

#-------------------------------------------------------------------------------
import pandas as pd 
from datetime import datetime
datetime_now = datetime.now().strftime('%Y%m%d_%H%M%S')

saleOrder_df = pd.DataFrame(data_dict)

saleOrder_df.to_csv(fr'C:\Users\admin\Desktop\local_env_ppeline_project\raw_data\saleOrder_{datetime_now}.csv', index=False)



