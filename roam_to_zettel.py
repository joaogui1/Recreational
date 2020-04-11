import os, tempfile

path = '.'

# folder = os.fsencode(path)

# for file in os.listdir(folder):
# 	filename = os.fsdecode(file)
	
with os.scandir(path) as it:
	for file in it:
		filename = os.fsdecode(file)
		if '.py' in filename:
			continue
		with tempfile.NamedTemporaryFile('w', delete=False) as outfile:
			outfile.write(f'# {filename[2:]}\n') #start the file with it's title like in Roam
				
			with open(filename, 'r+') as f:				
				for line in f:
					line = line.replace("- ", "", 1)	#removes Roam's - that break zettlr headgings
					line = line.replace('$$', '$') #fixes latex
					line = line.replace('#', '###', 1) #Zettlr's headgings are too big
					line = line.replace("{{[[DONE]]}}", "- [x]") #Done becomes a completed task
					line = line.replace("{{[[TODO]]}}", "- [ ]") #Todo becomes an incomplete task
					outfile.write(line)
			os.rename(outfile.name, filename)
				