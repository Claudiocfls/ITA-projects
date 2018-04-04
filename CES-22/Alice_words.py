text = " Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a stcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and was just in time to see it pop down a large rabbit-hole under the hedge"

text = text.split()
dic = {}

for word in text:
	if word in dic:
		dic[word] += 1
	else:
		dic[word] = 1
output = open('alice_words.txt','w')
output.write("Word              Count\n")
output.write("=======================\n")
for key in sorted(dic):
	output.write("%-12s:%d\n" % (key,dic[key]))