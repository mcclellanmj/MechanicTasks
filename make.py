import os
from string import Template

json_template = Template(open("template.json", "r").read())

def write(to_file, content):
	out_file = open(to_file, "w")
	out_file.write(content)
	out_file.close

for dir_part, dir_names, file_names in os.walk('.'):
	if not dir_part.startswith("./.git"):
		for dir_name in dir_names:
			if not dir_name.startswith(".git"):
				def mapper(filename):
					return '"' + dir_name + "/" + filename + '"'

				write(dir_name + ".json", json_template.substitute(
					directory=dir_name, paths=",".join(
					map(mapper, os.listdir(dir_name)))))