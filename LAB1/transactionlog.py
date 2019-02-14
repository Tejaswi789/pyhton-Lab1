# computes net bank amount based on the input
# "D" for deposit, "W" for withdrawal
# define a variable for main amount
net_amount = 0
while True:
	str = input ("Enter transaction: ")
	transaction = str.split(" ")
	type = transaction [0]
	amount = int (transaction [1])

	if type=="Deposit" or type=="deposit":
		net_amount += amount
	elif type=="Withdraw" or type=="withdraw":
		net_amount -= amount
	else:
		pass

	#input choice
	str = input ("want to continue (Y for yes) : ")
	if not (str[0] =="Y" or str[0] =="y") :
		# break the loop
		break

# print the net amount
print("Net amount: ", net_amount)