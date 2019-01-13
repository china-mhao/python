#10-1练习题
filename = 'big.txt'

with open(filename) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

with open(filename) as file_object:
	new_contents = file_object.readlines()
	for content in new_contents:
		print(content)


with open(filename) as file_object:
	lines = file_object.readlines()

pi_big = ''
for line in lines:
	line.replace('python','java')
	pi_big += line


print(pi_big.replace('python','java'))
print(str(len(pi_big.strip())))


#10-4练习题
#file_name = 'guest.txt'

#with open(file_name,'w') as file_object:
#	while True:
#		message = '请输入名字，如果想退出请输入qute: '
#		guest_name = input(message)
#		if guest_name == 'qute':
#			break
#		else:
#			file_object.write('Hello,' + guest_name.title() + '\n')

#10-6/10-7练习题
#print('请输入两个整数：')
#print('如果想退出请输入qute.')

#while True:
#	first_number = input('第一个数:' )
#	if first_number == 'qute':
#		break
#	try:
#		first_number_int = int(first_number)
#	except ValueError:
#		print('请输入整数.')
#	
#	secend_number = input('第二个数:' )
#	if first_number == 'qute':
#		break
#	try:
#		secend_number_int = int(secend_number)
#	except ValueError:
#		print('请输入整数.')

#	try:	
#		sum_2 = first_number_int + secend_number_int
#	except NameError:
#		print('输入的不是数字：')
#	else:		
#		print(sum_2)

#10-8/10-9练习题

file_cats = 'cats.txt'
file_dogs = 'dogss.txt'
file_name_zoos = [file_cats,file_dogs]

for file_name_zoo in file_name_zoos:
	try:
		with open(file_name_zoo) as file_object:
			contents_cats = file_object.readlines()
	except FileNotFoundError:
 		pass
 		#print('无法找到名为' + file_name_zoo + '的文件.' )
	else:
		for contents_cat in contents_cats:
			print(contents_cat.strip())

#10-10练习题
file_58699 = '58669-0.txt'

with open(file_58699) as file_object:
	contents_5 = file_object.read()
	contents_6 = contents_5.split()
	contents_7 = len(contents_6)
	print(contents_7)
	contents_8 = contents_5.lower().count('the')
	print(contents_8)


#10-11练习题

import json

file_name_json = 'like_number.json'

try:
	with open(file_name_json) as file_object:
		likenumber = json.load(file_object)
except FileNotFoundError:		
	with open(file_name_json,'w') as file_object:
		like_number = input('请输入你喜欢的数字: ')
		json.dump(like_number,file_object)
		print('你输入的数字是' + str(like_number) + '.')	
else:
	print('你喜欢的数字是：' + str(likenumber) +'.')


