import json

class Hotkeys:
    def __init__(self):
        with open('C:\\Users\\mihir\\Desktop\\CodingProjects\\PythonProjects\\SpotifyProject\\hotkeys.json', 'r') as openfile:
            self.hotkeys = json.load(openfile)



    def save(self):
        json_object = json.dumps(self.hotkeys, indent=4)
        with open("C:\\Users\\mihir\\Desktop\\CodingProjects\\PythonProjects\\SpotifyProject\\hotkeys.json", "w") as outfile:
            outfile.write(json_object)

        with open('C:\\Users\\mihir\\Desktop\\CodingProjects\\PythonProjects\\SpotifyProject\\hotkeys.json', 'r') as openfile:
            self.hotkeys = json.load(openfile)


    def change(self, key, value):
        self.hotkeys.update({key: value})
        self.save()


