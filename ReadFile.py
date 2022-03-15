f = open("C:\\Users\maitr\OneDrive\Documents\Maitrayee\maitrayee.txt", "r")
print(f.read())
f.close()
user_name = input('Enter your place: ')
my_file_writing = open("C:\\Users\maitr\OneDrive\Documents\Maitrayee\maitrayee.txt", "w")

my_file_writing.write(user_name)
my_file_writing.close()