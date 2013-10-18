#coding:utf-8                                                                           
import json
import sys

k=0
dict={}
while True:
    line=sys.stdin.readline().strip()
    if not line:
        break
    k+=1
    if k%100000==0:
        sys.stderr.write(str(k)+'\n')
    try:
        line=line.decode('utf-8')
        json_data=json.loads(line)
    except:
        sys.stderr.write("Loading json data error.\n"+line)
        continue
    if json_data.has_key('j'):
        if not dict.has_key(json_data['j']):
            dict[json_data['j']]=0
        dict[json_data['j']]+=1
list=sorted(dict.iteritems(),key=lambda x: x[1], reverse=True)
for u,v in list:
    print str(u)+'\t'+str(v)
