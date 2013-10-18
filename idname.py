#coding:utf-8
import sys
import cPickle as pickle
dict={}
idlist=[]
namelist=[]

with open('../../data/weibo_id0706') as f:
    for item in f:
        idlist.append(item.strip())
with open('../../data/weibo_name0706') as f:
    for item in f:
        namelist.append(item.strip())
for i in xrange(len(idlist)):
    dict[namelist[i]]=idlist[i]
f=open('idname.dump','w')
pickle.dump(dict,f)
f.close()
