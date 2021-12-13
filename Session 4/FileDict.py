import pickle
# we need this for cheking directory paths
import os.path


# creates a dictionary and save the data on a .pkl file
class FileDict:

	# runs whenever we create an object of this class
	def __init__(self, dictionary):
		# i need the name for saving
		self.dict_name = dictionary
		# checks if we have that dictionary already
		if os.path.isfile(self.dict_name+'.pkl'):
			# if True : then load the data
			file = open(self.dict_name+'.pkl', 'rb')
			self.dictionary = pickle.load(file)
		else:
			# if False : then create a new one
			self.dictionary = dict()

	# runs whenever the object is destroyed
	def __del__(self):
		# save the data on a .pkl file
		file = open(self.dict_name+'.pkl', 'wb')
		pickle.dump(self.dictionary, file)

	# item assignment
	def __setitem__(self, key, value):
		self.dictionary[key] = value

	# prints the dictionary
	def __str__(self):
		return str(self.dictionary)

	# gives data from dictionary
	def __getitem__(self, item):
		return self.dictionary.get(item)
