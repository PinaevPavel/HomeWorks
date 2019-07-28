def adder(*a, glue = ':'):
	sum = ''
	for n in a:
		if len(n) > 3:
			sum += n + glue
	sum = sum[:-1]
	print(sum)
adder('qsd', 'qwrt', 'qwrqq', 'q', 'qwwqr')

#def glue_1()
#for x in l:
#	if len(x) > 3:
#		print(x)