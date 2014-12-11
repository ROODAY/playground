running = True

class Room(object):
	first = None
	second = None
	description = None
	isend = False
	visited = 1

	def __init__(self, desc, isend):
		self.desc = desc
		self.isend = isend

	def setConnects(self, first, second):
		self.first = first
		self.second = second

	def checkend(self):
		if self.isend:
			return True

	def enter(self):
		if self.visited == 1:
			if not self.isend:
				print("This is your first time in this room.")
		else:
			print("You have been in this room %i times." % self.visited)

		print(self.desc)
		self.visited += 1

room1 = Room("This room is dark and scary.", False)
room2 = Room("This room is light and scary.", False)
room3 = Room("This room is light and happy.", False)
room4 = Room("This room is dark and happy.", False)
room5 = Room("Yay, you won!", True)

room1.setConnects(room4, room3)
room2.setConnects(room3, room1)
room3.setConnects(room2, room1)
room4.setConnects(room1, room5)

currentroom = room1
while running:
	currentroom.enter()
	if currentroom.checkend():
		inputting = False
		running = False
	else:
		inputting = True
	while inputting:
		ans = input("Do you want to go to the first (1) or second (2) connecting room? ")
		if ans == "1":
			inputting = False
			currentroom = currentroom.first
		elif ans == "2":	
			inputting = False	
			currentroom = currentroom.second
		else:
			print("That is not an option!")