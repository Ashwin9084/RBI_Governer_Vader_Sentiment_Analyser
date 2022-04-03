import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
R=[]
for i in range(96):
	t=str(i+1)
	s=''
	a='Prelimnary_text//File '+t+'.txt'
	with open(a,'r') as f:
		for i in f.readlines():
			if (i=='\n'):
				continue
			if 'ANNEXURE' in i:
				break
			i=i.replace('\n',' ')
			s+=str(i)
	l=s.split('.')
	M=[]
	for i in l:
		sent=SentimentIntensityAnalyzer()
		M.append(sent.polarity_scores(i)['compound'])
	R.append(np.mean(np.array(M)))
a=0
with open('Result.txt','a') as f:
	for i in R:
		t=str(a+1)
		f.write('The Result of File '+t+' is :		'+str(i)+'\n')
		a+=1