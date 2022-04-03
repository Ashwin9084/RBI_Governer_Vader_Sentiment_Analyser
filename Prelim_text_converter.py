for i in range(96):
	lines=[]
	t=str(i+1)
	# if (i!=95):
	# 	continue
	a='Text_files//File '+t+'.txt'
	with open(a,'r') as f:
		for i in f.readlines():
			lines.append(i.lower())
	b='Prelimnary_text//File '+t+'.txt'
	with open(b ,'a') as f:
		for i in lines:
			f.write(i)
	f.close()