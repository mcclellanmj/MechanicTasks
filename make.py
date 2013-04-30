import os
import distutils.core
from string import Template

json_template = Template(open("template.json", "r").read())

def write(to_file, content):
	out_file = open(to_file, "w")
	out_file.write(content)
	out_file.close

if not os.path.exists("target"):
	os.makedirs("target")

for dir_part, dir_names, file_names in os.walk('.', topdown=True):
	dir_names[:] = [d for d in dir_names if d not in [".git", "target"]]

	for dir_name in dir_names:
		def mapper(filename):
			return '"' + dir_name + "/" + filename + '"'

		write("target/" + dir_name + ".json", json_template.substitute(
			directory=dir_name, paths=",".join(
			map(mapper, os.listdir(dir_name)))))

		distutils.dir_util.copy_tree(dir_name, "target/" + dir_name)

print "Finished execution with no errors"