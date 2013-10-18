#coding:utf-8
import json
import sys
import re
import cPickle as pickle
ptn=re.compile(r'\@(\S+)\s')



f=open('./idname.dump')
sys.stderr.write('Loading id-name dictionary.\n')
#dict=pickle.load(f)
dict={}
f.close()
sys.stderr.write('Loading finished.\n')
k=0
s=0
while True:
    line=sys.stdin.readline().strip()
    raw=line
    if not line:
        break
    k+=1
    if k%10000==0:
        sys.stderr.write(str(k)+'\n')
    line=line.decode('utf-8').split('\t')
    if not len(line)==6:
        continue
    else:
        s+=1
print s,k

        
