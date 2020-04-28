import os, subprocess
import tempfile

path = '.'
	
def name_to_id(s):
	return s.replace(" ", "_").lower()

def props(s):
	s = name_to_id(s)
	return f':PROPERTIES:\n:CUSTOM_ID:{s}\n:END:\n'

def fix_link(line):
	link_pos = line.find("[[")
	while link_pos != -1:
		close_pos = line.find("]]", link_pos)
		line = line[:link_pos + 1] + '[' + name_to_id(line[link_pos+2:close_pos]) + ']' + line[link_pos+1:]
		link_pos = line.find("[[", close_pos)
	return line

def fix_todo(line):
	line = line.replace("{{[[DONE]]}}", "- [x]") #Done becomes a completed task
	line = line.replace("{{[[TODO]]}}", "- [ ]") #Todo becomes an incomplete task
	return line

def fix_tag(line):
	tag_pos = line.find("#")
	while tag_pos != -1:
		close_pos = line.find(" ", tag_pos)
		line = line[:tag_pos] + '[[' + name_to_id(line[tag_pos+1:close_pos]) + ']' +"[" + line[tag_pos+1:close_pos] + "]]"
		tag_pos = line.find("#", close_pos)
	return line

with os.scandir(path) as it:
	for file in it:
		filename = os.fsdecode(file)
		if '.md' not in filename:
			continue
		print(filename)
		subprocess.run(['pandoc', '-f', 'markdown', '-t', 'org', '-o', f'{filename[:-3]}.org', f'{filename}'])
		filename = filename.replace('.md', '.org')
		page_name = filename[2:-4]
		section_name = ''
		with tempfile.NamedTemporaryFile('w', delete=False) as outfile:
			outfile.write(props(page_name)) #Keep links to file working

			with open(filename, 'r+') as f:				
				for line in f:
					line = line.replace("- ", "", 1)	#removes Roam's - that are useless to orgmode
					line = line.replace('$$', '$') #fixes latex
					line = fix_link(line)
					line = fix_todo(line)
					line = fix_tag(line)
					outfile.write(line)
			os.rename(outfile.name, filename)
				