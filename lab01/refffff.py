from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot


mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
count_ads = 0
count_eve = 0
count_wom = 0
#1. conect to database
client = MongoClient(mongo_uri)

#2. get database
db = client.get_default_database()
n = db["customers"]
list_customer = n.find()
# for customers in list_customer:
#     print(customers)

for ref in list_customer:
    if ref['ref'] == 'ads':
        count_ads += 1
    elif ref['ref'] == 'wom':
        count_wom += 1
    else:
        count_eve += 1

print(count_wom, count_ads, count_eve)

labels = ["advertisements","word of mouth","events"]
values =[count_ads,count_wom,count_eve]
color = ["red", "green", "yellow"]
pyplot.pie(values,
    labels=labels,
    colors=color,
    shadow=True)
pyplot.axis("equal")

pyplot.show()
