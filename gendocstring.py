#!/bin/python3
import os
import json

class Config:
    def __init__(self):
        self.profiles = []
        self._config_file_path_ = os.path.expandvars("$HOME/.gendocstring")
        if os.path.exists(self._config_file_path_):
            self.load()
        else:
            self.save()

    def addProfile(self, profile: dict):
        self.profiles.append(profile)

    def getProfiles(self):
        return self.profiles
    
    def save(self):
        f = open(self._config_file_path_, "w+")
        f.write(json.dumps(self.__dict__))

    def load(self):
        try:
            with open(self._config_file_path_, "r") as f:
                datas = f.read()
                if datas:
                    self.__dict__ = json.loads(datas)
        except Exception as e:
            if type(e) == FileNotFoundError:
                self.save()
            # print(f"Error loading config: {e}")

config = Config()

def generateDocString(datas: dict, clipboard: bool = False):
    spacing = " " * 5
    print("\n\n\x1b[94m\"\"\"")
    formatToDisplay = lambda k, v : f"{spacing}{k:<20} : {v}"
    for k, v in datas.items():
        print(formatToDisplay(k,v))
    print("\"\"\"\x1b[0m")
    if clipboard:
        dstring = '"""\n' + '\n'.join(map(lambda x: formatToDisplay(x[0],x[1]),datas.items())) + '\n"""'
        os.system(f"echo '{dstring}' | xclip -sel c")

def createProfile():
    global config
    fields = [
        "Firstname",
        "Lastname",
        "Email",
        "Matricule"
    ]
    profile = {}
    for field in fields:
        profile[field] = input(f"{field} ? : ")
    config.load()
    config.profiles.append(profile)
    config.save()

def main(autoCreate: bool = False):
    global config
    firstname = ""
    lastname = ""
    email = ""
    matricule = ""

    if (config.profiles and len(config.profiles) > 0):
        print("Profiles : ")
        i = 0
        for profile in config.profiles:
            print(f"[{i}] {profile['Firstname']} {profile['Lastname']} - {profile['Email']} - {profile['Matricule']}")
            i += 1
        print("\n[c] Create new profile")
        print("[d <index>] Delete profile")
        print("[q] Quit\n")
        index = ""
        while index != "c" and index != "q" and (not index.startswith("d ") and (len(index.split(' ')) != 2 or not index.split(' ')[1].isdigit())) and (not index.isdigit() or int(index) >= len(config.profiles)):
            index = input("Selection : ").lower()
        print("\n")
        if index == "c":
            createProfile()
            main()
        elif index.startswith("d "):
            index = int(index.split(' ')[1])
            config.profiles.pop(index)
            config.save()
            main()
        elif index == "q":
            exit(0)
        else:
            index = int(index)
            profile = config.profiles[index]
            firstname = profile["Firstname"]
            lastname = profile["Lastname"]
            email = profile["Email"]
            matricule = profile["Matricule"]
        lesson = input("Lesson ? (ex: INFO-F-101) : ")
        project_name = input("Project name ? : ")
        project_desc = input("Project description ? (leave blank for none) : ")
        obj = {
            "Lesson": lesson,
            "Project name": project_name,
            "Author": f"{firstname} {lastname}",
            "Email": email,
            "Matricule": matricule
        }
        if project_desc:
            obj["Project description"] = project_desc
        generateDocString(obj, clipboard=True)
                    
    else:
        if (autoCreate):
            createProfile()
        main()
if __name__ == "__main__":
    main(autoCreate=True)
