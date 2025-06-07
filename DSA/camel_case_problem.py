# Given a sentence having lowercase characters, the task is to convert it to Camel Case. 
# In Camel Case, words are joined without spaces, the first word keeps its original case, 
# and each subsequent word starts with an uppercase letter.

def convertToCamelCase(s):
	res = []
	capitalise_signal = False
	for i in range(len(s)):
		if s[i] == " ":
			capitalise_signal = True
		elif capitalise_signal:
			res.append(s[i].upper())
			capitalise_signal = False
		else:
			res.append(s[i])
	
	return "".join(res)

if __name__ == "__main__":
	s = "i got intern at geeksforgeeks"
	print(convertToCamelCase(s))