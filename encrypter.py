import re
from heapq import * 

priorityqueue = []
huffmancodes = {}
inputs = [
	["a", 8.55],
	["b", 1.60],
	["c", 3.16],
	["d", 3.87],
	["e", 12.10],
	["f", 2.18],
	["g", 2.09],
	["h", 4.96],
	["i", 7.33],
	["j", 0.22],
	["k", 0.81],
	["l", 4.21],
	["m", 2.53],
	["n", 7.17],
	["o", 7.47],
	["p", 2.07],
	["q", 0.10],
	["r", 6.33],
	["s", 6.73],
	["t", 8.94],
	["u", 2.68],
	["v", 1.06],
	["w", 1.83],
	["x", 0.19],
	["y", 1.72],
	["z", 0.11],
]

class BinaryNode(object):
	leftnode = None
	rightnode = None
	character = None
	weight = 0

	def __init__(self, character, weight):
		self.character = character
		self.weight = weight

	def setChildren(self, left, right):
		self.leftnode = left
		self.rightnode = right

	def __lt__(self, other):
		return self.weight < other.weight

def huffman(string, node):
	if node.character:
		if not string:
			huffmancodes[node.character] = "0"
		else:
			huffmancodes[node.character] = string
	else:
		huffman(string + "0", node.leftnode)
		huffman(string + "1", node.rightnode)
		
for letter, weight in inputs:
	priorityqueue.append(BinaryNode(letter, weight))

heapify(priorityqueue)
while len(priorityqueue) > 1:
	leftnode, rightnode = heappop(priorityqueue), heappop(priorityqueue)
	combinednode = BinaryNode(None, rightnode.weight + leftnode.weight)
	combinednode.setChildren(leftnode, rightnode)
	heappush(priorityqueue, combinednode)

huffman("", priorityqueue[0])

inversecodes = {}
for key in huffmancodes:
	inversecodes[huffmancodes[key]] = key

def encode(string, shift, key):
	keylist = {}
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	alphabet2 = key + re.sub('[' + key + ']', '', alphabet)
	counter = 0
	while counter < 26:
		keylist[alphabet2[counter]] = alphabet[counter]
		counter += 1
	keylist[" "] = " "
	encoded = ""
	string = string[::-1]
	final = ""
	for char in string:
		try:
			final += keylist[char]
		except KeyError:
			pass
			final += char
	final = final[::-1]
	for char in final:
		encoded += "+" * (ord(char) + shift)
		encoded += ".>"
	encoded += "\n" + "{0:b}".format(shift) + "x"
	for char in key:
		encoded += huffmancodes[char]
	return encoded

def decode(string, key):
	keys = key.split("x")
	shift = int(keys[0], 2)
	keystring = keys[1]
	key = ""
	counter = 0
	while counter < len(keystring) and len(keystring) > 0:
		counter2 = 0
		code = ""
		while counter2 <= counter:
			code += keystring[counter2]
			counter2 += 1

		try:
			if inversecodes[code]:
				key += inversecodes[code]
				counter3 = len(code)
				while counter3 > 0:
					keystring = keystring[1:]
					counter3 -= 1 
				counter = 0
		except KeyError:
			pass
			counter += 1

	for char in keystring:
		key += inversecodes[char]

	keylist = {}
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	alphabet2 = key + re.sub('[' + key + ']', '', alphabet)
	counter = 0
	while counter < 26:
		keylist[alphabet[counter]] = alphabet2[counter]
		counter += 1
	keylist[" "] = " "
	decoded = ""
	value = 0
	for char in string:
		if char == "+":
			value += 1
		elif char == ">":
			decoded += chr(value - shift)
			value = 0
	decoded = decoded[::-1]
	reverse = ""
	for char in decoded:
		try:
			reverse += keylist[char]
		except KeyError:
			pass
			reverse += char
	reverse = reverse[::-1]
	return reverse

running = True
while running:
	command = input("Encode (1) Decode (2) Quit (3): ")
	if command == "1":
		string = input("Type the string to be encoded: ")
		shift = int(input("Type the shift used: "))
		key = input("Type the keyword: ")
		print("Output:", encode(string, shift, key))
	elif command == "2":
		string = input("Type the string to be decode: ")
		key = input("Type the key that was used: ")
		print("Output:", decode(string, key))
	elif command == "3":
		running = False
	else:
		print("That is not an option.")