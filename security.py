#in-memory table of registered users
from werkzeug.security import safe_str_cmp #, generate_password_hash, check_password_hash
from user import User
users = [
  User(1, "bob", "asdf"),
  User(2, "susan", "xyz"),
  User(3, "mary", "mno"),
  User(4, "david", "qwer"),

]

username_mapping = {u.username: u for u in users}  #access dictionary by username

userid_mapping = {u.id: u for u in users} #access dictionary by userid

def authenticate(username, password): 
    #compare user input to stored username and password 
    user = username_mapping.get(username, None)
    #you can run into problems when comparing strings with each other
    #(e.g. ascii vs unicode, so use safe_str_cmp)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload): #payload is the contents of the JWT token
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None) #return None if no user found

