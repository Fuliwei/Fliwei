#!/usr/bin/python
#coding:utf-8

import os 
os.system('clear')
res = {}
f = open("access.log",'r')
for line in f :
#	print '*'*40
#	print line 
	ip = line.split(' ')[0]
	url = line.split(' ')[6]
	code = line.split(' ')[8]
#	k = ip + ' '+ url  #此处可以替换为元组,元组来作为字典的key，来实现统计日志中的多个维度
#	print k
	res[(ip,url,code)] = res.get((ip,url,code),0)+1	#避免了代码冗余,一行代码完成if else的功能
#	break
f.close()
#print res

#print '*'*40
x = res.items()
#print x[0][0], x[0][1]
num = len(x)
#print num
for i in range(0,num - 1):
#	tmp = x[i][1]
	for j in range(0,num -1 - i):
		if x[j][1] > x[j+1][1]:
			x[j],x[j+1] = x[j+1],x[j]
		else :
			pass
#print x

html_f = open('/var/www/html/ip.html','w')
#for i in range(10):
#	print "No%s  , ip is %s ,the url is %s ,the code is %s ,count is %s" %((i+1),x[-i-1][0][0],x[-i-1][0][1],x[-i-1][0][2],x[-i-1][1])
i = 0
html_str = '<table border="1px">'
for r in x[:-11:-1]:
	i = i + 1
	html_str += '<tr><td>No%s</td><td>ip %s</td><td>url %s</td><td>code %s</td><td>count %s</td>' %(i,r[0][0],r[0][1],r[0][2],r[1])
html_str += '</table>'
html_f.write(html_str)
html_f.close()

