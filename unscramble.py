
# Read the two text files

try:
	targetFile=open('unscramble_words.txt')
except IOError:
	print('It is a problem with %s' % targetFile)

try:
	wordlistFile=open('wordlist.txt')
except IOError:
	print('It is a problem with %s' % wordlistFile)


# Clean the unscrambled words

targetRaw=[]
for line in targetFile:
	line = line.rstrip()
	targetRaw.append(line)

while True:
  try:
    targetRaw.remove("")
  except ValueError:
    break

targetDone=[]
for line in range(len(targetRaw)):
	targetTemp=targetRaw[line]
	targetTemp=sorted(targetTemp)
	targetTemp=''.join(targetTemp)
	targetDone.append(targetTemp)



# Clean wordlist file

wordlistRaw=[]
for line in wordlistFile:
	line = line.rstrip()
	wordlistRaw.append(line)

while True:
  try:
    wordlistRaw.remove("")
  except ValueError:
    break


# Sort each individual word in alphabetical order

wordlistDone=[]
for line in range(len(wordlistRaw)):
	wordlistTemp=wordlistRaw[line]
	wordlistTemp=sorted(wordlistTemp)
	wordlistTemp=''.join(wordlistTemp)
	wordlistDone.append(wordlistTemp)



# Compare the two lists

result=[]
for x in range(len(targetDone)):
	for y in range(len(wordlistDone)):
		if(targetDone[x] == wordlistDone[y]):
			result.append(wordlistRaw[y])
			print(wordlistRaw[y]) 
