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
s1=0
s2=0
s3=0
s4=0
while True:
    line=sys.stdin.readline().strip()
    if not line:
        break
    raw=line
    k+=1
    if k%10000==0:
        sys.stderr.write(str(k)+'\n')
    line=line.decode('utf-8').split('\t')
    if not len(line)==6:
        print line
        continue
    S=''
    try:
        if line[3]=='0':
            s1+=1
            S=line[0]+'\t'+line[1]+'\t'+'0'+'\t'+line[4]+'\t'+line[5]
            print S.encode('utf-8')
            continue
    except:
        sys.stderr.write('Wrong data.'+raw)
        continue

    match=ptn.search(line[2])
    if match==None:
        s2+=1
        S= line[0]+'\t'+line[1]+'\t'+line[3]+'\t'+line[4]+'\t'+line[5]
    else:
        name=match.group(1)
        if dict.has_key(name):
            s3+=1
            S= line[0]+'\t'+line[1]+'\t'+dict[name]+'\t'+line[4]+'\t'+line[5]
        else:
            s4+=1
            S= line[0]+'\t'+line[1]+'\t'+'-1'+'\t'+line[4]+'\t'+line[5]
    if not S=='':
        print S.encode('utf-8')
sys.stderr.write(str(s1)+' '+str(s2)+' '+str(s3)+' '+str(s4)+'\n')

        
