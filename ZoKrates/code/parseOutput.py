import sys

if __name__ == "__main__":
	print("number args", len(sys.argv))
	print("arguments", str(sys.argv))
	user_input = []
	is_input = False
	if len(sys.argv) == 7:
		is_input = True
		user_input= '['
		for i in range(1,6):
			user_input += sys.argv[i]
			user_input += ', '
		user_input += '1]'

		print(user_input)
	else:
		print("bad input, will not be displayed")
	with open("output.txt", "r") as f:
		data = f.read()
		data = data.split('\n')
		res = ""
		result_list = []
		for line in data:
			#print("###")
			#print(line)
			#print(len(line))
			#print("###")
			if len(line) > 0: 
				ls = line.split('(')[-1].split(')')[0]
				#print(ls)
				if ls[0] == '0':
					ls = ls.split(', ')
					res = '["' + ls[0] + '", "' + ls[1] + '"]'
				else:
					res = ls
					res = res.replace('[', '')
					res = res.replace(']', '')
					res = res.replace(',', '')
					res = res.split(' ')
					res = '[["' + res[0] + '", "' + res[1] + '"], ["' + res[2] + '", "' + res[3] + '"]]'
					#print(res)
				result_list.append(res)
			#print(line)
		if is_input:
			result_list.append(user_input)
		print("### LIST ###")
		print(result_list)
		one_line = ','.join(result_list)
		print("### ONE LINE ###")
		print(one_line)
