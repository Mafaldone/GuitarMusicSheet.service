import pymongo

class MongoDb() :
    
    username = 'admin'
    password = 'v-Na76heNTrj'
    dbname = 'guitarmusicsheet'
    collection = 'musicsheets'
    client = ''
    
    def Create(object) :
         #client = pymongo.MongoClient('mongodb://$OPENSHIFT_MONGODB_DB_HOST:$OPENSHIFT_MONGODB_DB_PORT/', 8000)
         client = pymongo.MongoClient("localhost", 27017)
         print client
         print 'a'
    
    def InsertSheet() : 
        return '1'
        
        
        
    def GetSheet():
        
        db.my_collection = Collection(Database(client, dbname), collection)
        
        db.my_collection.save({"x": 10})
        db.my_collection.save({"x": 8})
        db.my_collection.save({"x": 11})
        
        db.my_collection.find_one()

        for item in db.my_collection.find():
            print item["x"]

        db.my_collection.create_index("x")
        for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
            print item["x"]
        
        

mymongo = MongoDb()
mymongo.Create()