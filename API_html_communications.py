import requests


key = "YjFjYWFjNWUtOTg4My00MDYxLWI4MDgtNWNjOGNhN2U4ODYw"


user_url = "https://api.clockify.me/api/v1/user"
 

api_key = {'X-Api-Key': key}
user_response = requests.get(user_url, headers=api_key)

user_dict = user_response.json()


for k, v in user_dict.items():

    if k == 'id':
        userId = v
        print("id:", userId)


for k, v in user_dict.items():

    if k == 'defaultWorkspace':

        workspaceId = v

        print("workspace id:", workspaceId)


workspaces_url = "https://api.clockify.me/api/v1/workspaces/{}/clients".format(workspaceId)
clients_response = requests.get(workspaces_url, headers=api_key)

clients_dict = clients_response.json()

clientsId = list()
i = 0
while i < len(clients_dict):
    for k, v in clients_dict[i].items():
        # if k == 'id' :
        #     clientsId[i] = v
        if k == 'name':
            print(v)
    i += 1


print("\n\n", clients_dict)


projects_url = "https://api.clockify.me/api/v1/workspaces/{}/projects".format(workspaceId)
projects_response = requests.get(projects_url, headers=api_key)

projects_dict = projects_response.json()


i = 0
while i < len(projects_dict):
    for k, v in projects_dict[i].items():
        # if k == 'id' :
        #     clientsId[i] = v
        if k == 'name':
            print(v)
    i += 1



# print("\n\n", projects_dict)





