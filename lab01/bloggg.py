from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1. conect to database
client = MongoClient(mongo_uri)

#2. get database
db = client.get_default_database()

#3. creat collection
posts = db['posts']
new_post = {
    'title':'ᕕ(ᐛ)ᕗ ',
    'author': '@metotelololala',
    'content': "I just don't see how a world that makes such wonderful things could be bad..."
}
posts.insert_one(new_post)
