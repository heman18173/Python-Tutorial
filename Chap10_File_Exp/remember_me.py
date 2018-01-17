import json

username = input("What is your name ? :")
filename = 'usernames.json'
with open(filename, 'w') as file_obj:
    json.dump(username, file_obj)
    print("\n Thanks " + username + " your information saved")