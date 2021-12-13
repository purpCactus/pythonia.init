
address = input("enter your file address: ")
read = open("extfile.txt", "r")
write = open("product.txt", "w")
answer = []
# step 1: file ro khat be khat mikhonim
for line in read:
	# step 2: khat ro be 2bakhshe ghable comma va badesh taghsim mikonim
	# step 3: 2 bakhsho ba space split mikonim az avali akhari va az 2vomi avalin elementesho barmidarim.
	comma = line.index(",")
	str1 = line[:comma]
	temp = str1.split(" ")
	write.write(temp[-1])
	write.write(" ")
	str2 = line[comma+2:-1]
	temp = str2.split(" ")
	write.write(temp[0])
	write.write(" ")
	write.write("\n")
"""
ali hasan, mamad hossein
porteghal, sib holoo
amoo zanjir baff,"""


