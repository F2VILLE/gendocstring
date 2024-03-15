#!/bin/python3
import os
import sys
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
            else:
                print(f"Error loading config: {e}")

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


class DocString:
    def __init__(self, datas: dict):
        self.datas = datas

    def generate(self, clipboard: bool = False):
        spacing = " " * 5
        print("\n\n\x1b[94m\"\"\"")
        def formatToDisplay(k, v): return f"{spacing}{k:<20} : {v}"
        for k, v in self.datas.items():
            print(formatToDisplay(k, v))
        print("\"\"\"\x1b[0m")
        dstring = '"""\n' + \
            '\n'.join(map(lambda x: formatToDisplay(
                x[0], x[1]), self.datas.items())) + '\n"""'
        if clipboard:
            os.system(f"echo '{dstring}' | xclip -sel c")
            print("\n\x1b[92mCopied to clipboard\x1b[0m")
        return dstring

config = Config()
args = sys.argv[1:]

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
            print(
                f"[{i}] {profile['Firstname']} {profile['Lastname']} - {profile['Email']} - {profile['Matricule']}")
            i += 1
        print("\n[c] Create new profile")
        print("[d <index>] Delete profile")
        print("[q] Quit\n")
        index = ""
        while index != "c" and index != "q" and (not index.startswith("d ") and (len(index.split(' ')) != 2 or not index.split(' ')[1].isdigit())) and (not index.isdigit() or int(index) >= len(config.profiles)):
            index = input("Selection : ").lower()
        print("\n")
        if index == "c":
            config.createProfile()
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
        docstring = DocString(obj)
        copyClipBoard = (args.count("-c") > 0 or args.count("--copy") > 0)
        ds = docstring.generate(clipboard=copyClipBoard)
        if (args.count("-f") > 0 or args.count("--file") > 0):
            filename = args[args.index("-f") + 1] if args.count("-f") > 0 else args[args.index("--file") + 1]
            with open(filename, "r+") as f:
                fcontent = f.read()
                f.seek(0, 0)
                f.write(ds + "\n\n" + fcontent)
                print(f"\n\x1b[92mDocstring written to {filename}\x1b[0m")

    else:
        if (autoCreate):
            config.createProfile()
        main()


if __name__ == "__main__":
    if (args.count("-h") > 0 or args.count("--help") > 0):
        print("Usage : gendocstring [options]\n\nOptions :")
        print("\t-c, --copy : Copy the generated docstring to clipboard")
        print("\t-f, --file <filename> : Write the generated docstring to a file")
        print("\t-h, --help : Display this help message")
        exit(0)

    if args.count("-f") > 0 or args.count("--file") > 0:
        try:
            filename = args[args.index("-f") + 1] if args.count("-f") > 0 else args[args.index("--file") + 1]
            if not os.path.exists(filename):
                print("Error : File not found")
                exit(1)
        except:
            print("Error : No filename provided")
            exit(1)
    main(autoCreate=True)
