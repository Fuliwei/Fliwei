#!/usr/bin/python
#coding:utf-8
import os
os.system('clear')

res_dict = {}
log_f = open("log1.log",'r') #打开文件方式一,记得要关闭文件
#with open("log1.log","r") as log_f #打开文件方式二，用完后文件自动关闭,可以同时打开多个文件
#for line in log_f.readlines():
for line in log_f:	#打开文件方式一
#	print line 
	ip = line.strip().split(' ')[0]
	url = line.strip().split(' ')[6]
#	print ip
	res_dict[(ip,url)] =res_dict.get((ip,url),0)+1 
log_f.close()
#print res_dict.items()

#print "\n"
#print '*' *40
#将字典通过res_dict.items()转换为列表进行冒泡排序[('218.200.66.205', 1), ('218.200.66.204', 1)]格式大概所示
#冒泡排序对字典所转换的列表中的ip出现次数进行排序
#有可以提升的空间使用sort函数进行排序
res_list = res_dict.items()
for i in range(1,6):
	for x in range(len(res_list)-1) :
		if res_list[x][1] > res_list[x+1][1]:
			res_list[x] , res_list[x+1] = res_list[x+1] , res_list[x]
#print res_list
#print '-' * 40 
print res_list[-5:]


#将上述排序结果写入到html页面中
ip_html = open("/var/www/html/count_ip2.html","w")#"w"模式一打开文件就清空了
html_str = "<table border='1px'>"
count = 0
for r in res_list[:-6:-1]:#用列表切片以及步长设置为-1实现写入文件时从最大到最小
	count += 1
#	print r 
	html_str += "<tr><td>No%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" %(count,r[0][0],r[0][1],r[1])
html_str += "</table>"
ip_html.write(html_str)
ip_html.close()
