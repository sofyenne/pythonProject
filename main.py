import pymongo 

from mytekscrap import scrap_mytek
from  tunisianetscrap import scrap_tunisia_net
from  tel_mytek import *
from  scrap_tel import *


products1 = scrap_mytek()
products2 = scrap_mytek_tel()
products3 = scrap_tunisia_net_tel()
products4 = scrap_tunisia_net()
client = pymongo.MongoClient(
    'mongodb+srv://DbSofien:sofien@cluster0.cfeof.mongodb.net/databasetest?retryWrites=true&w=majority')
db = client.databasetest.product_products
try:
    db.insert_many(products1)
    print(f'inserted {len(products1)}articles')
    db.insert_many(products2)
    print(f'inserted {len(products2)}articles')
    db.insert_many(products3)
    print(f'inserted {len(products3)}articles')
    db.insert_many(products4)
    print(f'inserted {len(products4)}articles')
except:
    print('an error occurred products were not stored to db')


