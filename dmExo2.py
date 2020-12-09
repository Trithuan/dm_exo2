#  + -> ou
#  * -> et
#  # -> xor

combinaison = []
expr = 't#f*t+t*f'


def combis(done, notdone):
	global combinaison
	if notdone == []:
		combinaison.append(done)
	for i, o in enumerate(notdone):

		res = notdone.copy()
		# print(done+res.pop(i), res)
		res.pop(i)
		combis(done+o, res)

def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1 


#génère tout les index possible 
def combi_parenthese(expr):
	expr = Convert(expr)
	nb_operation = len(expr)//2
	nb_tree = nb_operation * nb_operation
	var_bools = []
	operators = []
	for i, e in enumerate(expr):
		if i % 2 == 0:
			var_bools += e
		else:
			operators += e
	# print(var_bools, operators)
	indexes = []
	for i, o in enumerate(operators):
		indexes.append(str(i))
	combis('',indexes)
	# print(combinaison)
	# print(len(combinaison))
	return combinaison


def TrueOrFalse(order, expr):
	if expr == 't':
		return True
	if expr == 'f':
		return False
	operation_index = int(order[0])
	operation_pos = (operation_index * 2) + 1
	operation = expr[operation_pos]
	# print(order, operation_index, operation_pos, operation, expr)
	# print("order : ",order)
	# print("op_index : ",operation_index)
	# print("order for left : ",[x for x in order if int(x) < operation_index])
	# print("order for right : ",[str(int(x) - operation_index) for x in order if int(x) - operation_index >= 0])
	# print("op_pos : ",operation_pos)
	# print("new_expr_left : ",expr[0:operation_pos])
	# print("new_expr_right : ",expr[operation_pos+1:len(expr)])
	# print("expr : ",expr)
	left = TrueOrFalse([x for x in order if int(x) < operation_index], expr[0:operation_pos])

	right = TrueOrFalse([str(int(x) - operation_index) for x in order if int(x) - operation_index >= 0], expr[operation_pos+1:len(expr)])



	if operation == '+':
		return left or right
	elif operation == '*':
		return left and right
	elif operation == '#':
		return left != right



# order = Convert(combi_parenthese(expr)[0])
# print(TrueOrFalse(order, expr))

def ParentheseRender(order, expr):
	if expr == 't':
		return 't'
	if expr == 'f':
		return 'f'
	operation_index = int(order[0])
	operation_pos = (operation_index * 2) + 1
	operation = expr[operation_pos]
	# print(order, operation_index, operation_pos, operation, expr)
	# print("order : ",order)
	# print("operation :", operation)
	# print("op_index : ",operation_index)
	# print("order for left : ",[x for x in order if int(x) < operation_index])
	# print("order for right : ",[str(int(x) - operation_index) for x in order if int(x) - operation_index >= 0])
	# print("op_pos : ",operation_pos)
	# print("new_expr_left : ",expr[0:operation_pos])
	# print("new_expr_right : ",expr[operation_pos+1:len(expr)])
	# print("expr : ",expr)
	left = ParentheseRender([x for x in order if int(x) < operation_index], expr[0:operation_pos])
	right = ParentheseRender([str(int(x) - operation_index-1) for x in order if int(x) - operation_index-1 >= 0], expr[operation_pos+1:len(expr)])
	renderleft = left
	# print("left :", left)
	# print("right :", right)
	if len(left) != 1:
		renderleft = '('+left+')'
	renderright = right
	if len(right) != 1:
		renderright = '('+right+')'

	return renderleft+operation+renderright

for order in combi_parenthese(expr):
	# print(order)
	# print(TrueOrFalse(Convert(order), expr))
	if TrueOrFalse(Convert(order), expr):
		print(order)
		print(ParentheseRender(order, expr))