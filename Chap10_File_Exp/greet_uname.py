import json

filename = 'usernames.json'

with open(filename) as f_obj:
    uname = json.load(f_obj)
    print("Welcome back " + uname)