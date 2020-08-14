encrypted_text = open("encrypted_text.txt","r")
percentage_doc = open("percentage of leters.txt","w")
all_used_words = open("leters.txt","w")
text = encrypted_text.read()
size = len(text)
saved_characters = []
character_count = []
percentage = []
count = 0
for x in text:
	if x not in saved_characters:
		saved_characters.append(x)
		character_count.append(1)
	else:
		character_count[saved_characters.index(x)] = character_count[saved_characters.index(x)] + 1
for i in character_count:
	percent = i/size
	percent = percent*100
	percentage_doc.write(saved_characters[count]+" = %.3f"%percent+"%\n")
	count = count +1
for j in saved_characters:
	all_used_words.write("\""+j+"\",")
print(character_count)

	

