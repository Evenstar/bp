#coding:utf-8
import json
import sys
import thread
import time

def comb( ):
    k=0
    while True:
        line=sys.stdin.readline().strip()
        if not line:
            break
            k+=1
        if k%10000==0:
            sys.stderr.write(str(k)+'\n')
        try:
            line=line.decode('utf-8')
            json_data=json.loads(line)
        except:
            sys.stderr.write("Loading json data error.\n")
            continue
        line=''
        try:
            if json_data.has_key('k'):
                line=json_data['a']+'\t'+str(json_data['e'])+'\t'+json_data['k']+'\t'+json_data['i']+'\t'+json_data['b']+'\t'+json_data['j']
            elif json_data.has_key('i'):
                line=json_data['a']+'\t'+str(json_data['e'])+'\t'+' '+'\t'+json_data['i']+'\t'+json_data['b']+'\t'+json_data['j']
            else:
                line=json_data['a']+'\t'+str(json_data['e'])+'\t'+' '+'\t'+'0'+'\t'+json_data['b']+'\t'+json_data['b']
                line=line.encode('utf-8')
        except:
            sys.stderr.write('Wrong data\n')
            continue
        if not line=='':
            ofid.write(line.encode('utf-8')+'\n')
    ofid.close()

#def run(start,num):
#    for i in range(num):
#        print str(start+i)
#        thread.start_new_thread(comb, (str(start+i)+'.dat',) )



comb()
