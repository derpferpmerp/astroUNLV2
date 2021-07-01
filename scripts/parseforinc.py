import json
import re
import subprocess


subprocess.call("rm -rf out*.json", shell=True)


def removeExtension(inp):
    return re.sub(r"\..*", "", inp)


def patternInFile(filename):
    actualout = []
    with open(f"../{filename}") as fl:
        outjson = {}
        data = fl.read()
        data = re.sub(r'.*player\.load\("', "", data)
        data = re.sub('\\.?".*', "", data)
        outjson["Html Filename"] = filename
        outjson["Swf Filename"] = re.sub("\\n", "", filename.replace(".html", ""))
        outjson["Value In Html File"] = re.sub("\\n", "", data)
        if not [
            True
            if re.sub("\\n", "", filename.replace(".html", ""))
            == outjson["Value In Html File"]
            else False,
        ][0]:
            actualout.append(outjson)
            return actualout[0]
        else:
            return "None"


filesunbeautified = subprocess.check_output("cd ../; ls -l *.html", shell=True).decode(
    encoding="utf-8",
)
htmlfiles = re.sub(".* ? ", "", filesunbeautified)
htmlfilenames = [
    x
    for x in removeExtension(htmlfiles).replace("ALL-MAIN", "").split("\n")
    if x != ""
]
withextensionhtml = [x for x in htmlfiles.replace("ALL-MAIN.html", "").split("\n") if x != ""]
outlist = []
for itm in withextensionhtml:
    if patternInFile(itm) != "None":
        outlist.append(patternInFile(itm))

print(json.dumps(outlist, sort_keys=True, indent=4))

with open("out.json", "x+") as outfile:
    outfile.write(str(outlist))
