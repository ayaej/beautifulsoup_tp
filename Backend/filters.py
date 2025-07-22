from Backend.database import get_db

def get_by_subcategory(subcat):
    db = get_db()
    return list(db["articles"].find({"subcategory": subcat}))

def get_by_author(author):
    db = get_db()
    return list(db["articles"].find({"author": author}))

def get_by_title_search(keyword):
    db = get_db()
    return list(db["articles"].find({"title": {"$regex": keyword, "$options": "i"}}))

def get_by_date_range(start_date, end_date):
    db = get_db()
    return list(db["articles"].find({
        "date": {
            "$gte": start_date,
            "$lte": end_date
        }
    }))
