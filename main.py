varis = {'eax':0, 'ebx':0, 'ecx':0, 'edx':0}
a = open('code.txt', 'r')
code = a.readline().replace('\n', '')
bit_limit = 2**32
word_limit = 2**64
retto = 'start'
exit_code = 0

def jump(label):
	a = open('code.txt', 'r')
	code = a.readline().replace('\n', '')
	while code != label + ':':
		code = a.readline().replace('\n', '')
	return a
while code != 'end':
	code = code.replace('\t', '') 
	code = code.replace('\n', '') 
	if code == '_regedit:':
		code = a.readline().replace('\n', '')
		while code[0] == '\t':
			parse = code.split(',')
			if parse[0] == 'bit_limit':
				bit_limit = 2**int(parse[1])
			if parse[0] == 'word_limit':
				word_limit = 2**int(parse[1])
			if parse[0] == 'global':
				retto = parse[1]
			code = a.readline().replace('\n', '')
	if code[0:2] == 'db':
		parse = code.split(',')
		if int(parse[1]) > bit_limit:
			break
		else:
			varis[parse[0][3:]] = int(parse[1])
	if code[0:2] == 'dw':
		parse = code.split(',')
		if int(parse[1]) > word_limit:
			break
		else:
			varis[parse[0][3:]] = int(parse[1])
		
	if code[0:2] == 'ds':
		code = code.replace('\"', '')
		parse = code.split(',')

		varis[parse[0][3:]] = parse[1]
	if code[0:3] == 'add':
		parse = code.split(',')
		varis[parse[0][4:]] = int(varis[parse[1]]) + int(varis[parse[2]])
	if code[0:3] == 'sub':
		parse = code.split(',')
		varis[parse[0][4:]] = int(varis[parse[1]]) - int(varis[parse[2]])
	if code[0:3] == 'mul':
		parse = code.split(',')
		varis[parse[0][4:]] = int(varis[parse[1]]) * int(varis[parse[2]])
	if code[0:4] == 'idiv':
		parse = code.split(',')
		varis[parse[0][5:]] = int(varis[parse[1]]) // int(varis[parse[2]])
	if code[0:3] == 'div':
		parse = code.split(',')

		varis[parse[0][4:]] = int(varis[parse[1]]) / int(varis[parse[2]])
	if code[0:5] == 'win \"':
		parse = code.split(',')
		varis[parse[1]] = input(parse[0][5:-1])
	elif code[0:3] == 'win':
		parse = code.split(',')
		varis[parse[1]] = input(varis[parse[0][5:-1]])
	if code[0:5] == 'bin \"':
		parse = code.split(',')
		varis[parse[1]] = int(input(varis.get(parse[0][5:-1],parse[0][5:-1])))
	elif code[0:3] == 'bin':
		parse = code.split(',')
		varis[parse[1]] = int(input(varis[parse[0][5:-1]]))
	if code[0:5] == 'msg \"' and code[-1] == '\"':
		print(code[5:-1])
	elif code[0:4] == 'msg ':
		print(varis.get(code[4:], code[4:]))
	if code[0:4] == 'jmp ':
		jump(code[4:])
	if code == 'ret':
		jump(retto)
	if code[0:3] == 'jl ':
		parse = code.split(',')
		if varis.get(parse[0][3:], int(parse[0][3:])) < varis.get(parse[1], int(parse[1])):
			a = jump(parse[2])
			code = code.replace('\n', '')
			code = code.replace('\t', '')
	if code[0:3] == 'jg ':
		parse = code.split(',')
		if varis.get(parse[0][3:], int(parse[0][3:])) > varis.get(parse[1], int(parse[1])):
			a = jump(parse[2])
			code = code.replace('\n', '')
			code = code.replace('\t', '')
	if code[0:3] == 'je ':
		parse = code.split(',')
		if varis.get(parse[0][3:], parse[0][3:]) == varis.get(parse[1], parse[1]):
			a = jump(parse[2])
			code = code.replace('\n', '')
			code = code.replace('\t', '')
	if code[0:4] == 'jge ':
		parse = code.split(',')
		if varis.get(parse[0][3:], int(parse[0][3:])) >= varis.get(parse[1], int(parse[1])):
			a = jump(parse[2])
			code = code.replace('\n', '')
			code = code.replace('\t', '')
	if code[0:4] == 'jle ':
		parse = code.split(',')
		if varis.get(parse[0][3:], int(parse[0][3:])) <= varis.get(parse[1], int(parse[1])):
			a = jump(parse[2])
			code = code.replace('\n', '')
			code = code.replace('\t', '')
	if code[0:4] == 'jne ':
		parse = code.split(',')
		if varis.get(parse[0][3:], parse[0][3:]) != varis.get(parse[1], parse[1]):
			a = jump(parse[2])
			code = code.replace('\n', '')
			code = code.replace('\t', '')
	code = a.readline().replace('\n', '')
	code = code.replace('\t', '') 
print(f'\n\n\033[31mcode compiled with exit code {exit_code}.\033[0m')