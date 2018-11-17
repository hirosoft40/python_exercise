import dic_func

# # ===== Exe 1
phonebook_dict={
  'Alice': '703-493-1834',
	'Bob' : '857-384-1234',
	'Elizabeth': '484-584-2923'
}
# # 1 
print(phonebook_dict['Elizabeth'])
# # 2
phonebook_dict['Kareem'] = '938-489-1234'

# # 3
phonebook_dict.pop('Alice')

# # 4
phonebook_dict['Bob'] = '968-345-2345'

# #5 
for i in phonebook_dict:
	print (phonebook_dict[i])

# # ===== Exe 2
ramit = {
	'name' : 'Ramit',
	'email': 'ramit@gmail.com',
	'interests': ['movies', 'tennis'],
	'friends': [
		{
			'name': 'Jasmine',
			'email': 'jasmine@yahoo.com',
			'interests': ['photography', 'tennis']
		},
		{
			'name': 'Jan',
			'email': 'jan@hotmail.com',
			'interests' : ['movies', 'tv']
		}
	]
}

# # 1 ramit's email
print	("Ramit email is: ", ramit['email'])

# # 2
print ("Ramit's email: ", ramit['interests'][0])

# # 3
print ("Jasmine's email: ", ramit['friends'][0]['email'])

# # 4
print ("Jan's 2nd interest: ", ramit['friends'][1]['interests'][1])

# function wordCount: 
# arg1: message you want to count
# return: new list of dictionary with key and # of value
def wordCount(msg):
    if ' ' in msg: msg = msg.split(" ")
    newList = {}
    for x in msg:
	    newList[x] = msg.count(x)
    return newList

# # ==== Letter Summary
msg = input("Message please: ").lower() # change all letters to lower.
print (wordCount(msg))

# # ==== Word Summary
sentence = input("Type in sentance:").lower() # change all letters to lower.
print (wordCount(sentence))

# === Bonus challenge
anyWord = input("Any?:").lower() # change all letters to lower.
topList = wordCount(anyWord) 
print (sorted(topList, key=topList.get, reverse=True)[:3])
	
