import colorama
from colorama import Fore
import requests
import json

api = "https://gitlab.com/api/v4/"
token = 'glpat-Sa6G7btfkL6Vm-e7maAY'

count_saved_files = 2

def request_id(option):         
        response = requests.get(f"{api}{option}", headers={'PRIVATE-TOKEN': f'{token}'})        
        content = response.content
        print(Fore.CYAN + str(response))
        resp_dict = json.loads(content)
        ids = []
        print(Fore.BLUE + option)
        if response.status_code != 200:
                return ids 
        for i in range(len(resp_dict)):
                if 'projects' in option:
                        filename = f"{resp_dict[i]['id']}-project.json"
                        with open(f"./projects/{filename}", "w") as write_file:
                                json.dump(resp_dict[i], write_file, indent=4)
                        print(Fore.GREEN + f'{filename} SAVED')
                else:
                        ids.append(resp_dict[i]['id'])
        return ids

def projects_main():
        print(Fore.YELLOW + "\nMAIN")
        id = '3544756'
        option = f'groups/{id}/subgroups'
        
        ids = request_id(option)
        main = []
        for i in ids:
                id = i
                option = f'groups/{id}/subgroups'
                main.extend(request_id(option))
        print("OK")
        
        print(Fore.YELLOW + "\nMAIN PROJECTS")
        project = []
        for i in ids:
                id = i
                option = f'groups/{id}/projects/'
                print(Fore.LIGHTBLUE_EX + option)
                res = request_id(option)
                if res:
                        project.extend(res)
        print("OK")
        print(Fore.WHITE + 'TOOK IDS: ' + str(main))
        return main

def projects_groups():
        print(Fore.YELLOW + "\nGROUPS")
        groups_ids = projects_main()
        for i in groups_ids:
                id = i
                option = f'groups/{id}/subgroups'
                groups_ids.extend(request_id(option))

        
        print(Fore.YELLOW + "\nGROUP PROJECTS")
        for i in groups_ids:
                id = i
                option = f'groups/{id}/projects/'
                print(Fore.LIGHTBLUE_EX + option)
                res = request_id(option)
                if res:
                        groups_ids.extend(res)
        print("OK")
        print(Fore.WHITE + 'TOOK IDS: ' + str(groups_ids))
        return groups_ids

def projects_subgroups():
        print(Fore.YELLOW + "\nSUBGROUPS")
        groups_ids = projects_groups()
        for i in groups_ids:
                id = i
                option = f'groups/{id}/subgroups'
                groups_ids.extend(request_id(option))

        
        print(Fore.YELLOW + "\nSUBGROUP PROJECTS")
        for i in groups_ids:
                id = i
                option = f'groups/{id}/projects/'
                print(Fore.LIGHTBLUE_EX + option)
                res = request_id(option)
                if res:
                        groups_ids.extend(res)
        print("OK")
        print(Fore.WHITE + 'TOOK IDS: ' + str(groups_ids))
        print(Fore.WHITE + 'IDS COUNT: ' + str(len(groups_ids)))
        return groups_ids

if __name__ == "__main__":
        projects_subgroups()
