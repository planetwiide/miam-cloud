import hwid


print(hwid.get_hwid())
input(" ")

import yaml

def auth(pwd):
    with open('users.yml', 'r') as file:
        users = yaml.safe_load(file)
    
    for user in users['users']:
        if user['password'] == pwd:
            return True
    
    return False


hwid_to_check = "990B1818-BE34-42AF-83DB-75666198E928"
result = authenticate_hwid(hwid_to_check)
print(result) 
input(" ")
