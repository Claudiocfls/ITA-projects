

def cleanword(word):
	new_word = ''
	for i in word:
		if (i >= 'a' and i <='z') or (i >= 'A' and i <= 'Z'):
			new_word += i
	return new_word

def has_dashdash(word):
	size = len(word)
	for i in range(0, size-1):
		if word[i] == '-' and word[i+1] == '-':
			return True
	return False 

def extract_words(sentence):
	sentence = sentence.replace('  ', ' ')
	sentence = sentence.replace('--', ' ')
	word_list = sentence.split(' ')
	new_list = []
	for word in word_list:
		new_word = cleanword(word)
		new_word = new_word.lower()
		new_list.append(new_word)
	return new_list

def wordcount(word, word_list):
	acc = 0
	for word_in_list in word_list:
		if word_in_list == word:
			acc += 1
	return acc
def wordset(word_list):
	new_list = list(set(word_list))
	new_list.sort()
	return new_list

def longestword(word_list):
	longest = 0
	for i in word_list:
		if len(i) > longest:
			longest = len(i)
	return longest