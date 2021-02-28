import os


def handle_topic(section):
    splited = section.split("\n###")

    section_name = splited[0].replace(" ", "") +".md"
    assert(not os.path.isfile(section_name))

    with open(section_name, "w") as f:
        for t in splited[1:]:
            f.write("\n###"+t) # add back the ###

def handle_readme(readme):
    r_splits = readme.split("\n# Index")
    index = r_splits[1].split("\n")

    with open("README.md", "w") as f:
        f.write(r_splits[0] + "\n# Index") ## copy 1-to-1 up to inkl # Index
        section = ""
        for line in index[0:]:
            start = line.find("(")
            end = line.find(")")
            name = line[start+1:end]

            if end == start: # no linking
                pass
            elif line[0]=="-": # Topic, we can get file from
                section = line[line.find("[")+1 : line.find("]")].replace(" ","") + ".md" ## get the file name
                line = line[:start] + "(" + section + ")"
            else:
                line = line[:start] + "(" + section + name + ")" ## link to section in file

            f.write(line+"\n") # add back the "\n"

# Read READNE.md file we are reading from
file_ = open('README.md','r') # reade
data = file_.read()
file_.close()

os.system('rm *.md')

# Part that is going to README.md
splitData = data.split("\n## ")
handle_readme(splitData[0])

# Topics == Seperate Files
for i in splitData[1:]:
    handle_topic(i)