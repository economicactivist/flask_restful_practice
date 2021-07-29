#in-memory table of registered users

users = [
    {"id" : 1, "name" : "John", "username" : "john", "password" : "john123"},
    {"id" : 2, "name" : "Michael", "username" : "michael", "password" : "michael123"},
]

username_mapping = {u["username"] : u for u in users}  #access dictionary by username

userid_mapping = {u["id"] : u for u in users}  #access dictionary by userid

def authenticate(username, password): 
    user = username_mapping.get(username, None)
    if user and user["password"] == password:
        return user

def identity(payload): #payload is the contents of the JWT token
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None) #return None if no user found

