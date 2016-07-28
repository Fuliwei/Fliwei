#!/usr/bin/python
#coding:utf-8
import os
os.system('clear')
def getip(filename,mode):
	res_dict = {}
	log_f = open(filename,mode) #打开文件方式一,记得要关闭文件
	#with open("log1.log","r") as log_f #打开文件方式二，用完后文件自动关闭,可以同时打开多个文件
	#for line in log_f.readlines():
	for line in log_f:
		tmp = line.strip().split(' ')
		ip ,url = tmp[0] ,tmp[6]
		res_dict[(ip,url)] = res_dict.get((ip,url),0)+1 
	log_f.close()
	return sorted(res_dict.items(),key=lambda x:x[1])
#res_dict.items()将字典转换为元组,key=lambda x:x[1] 之前前边转换的元组中索引为1的值进行排序.


#将字典通过res_dict.items()转换为列表进行冒泡排序[('218.200.66.205', 1), ('218.200.66.204', 1)]格式大概所示
#冒泡排序对字典所转换的列表中的ip出现次数进行排序
#有可以提升的空间使用sort函数进行排序
#def maopao_sort(arr,times):#此处传递字典参数时,只需要当成一个普通参数传递就行.
#	res_list = arr.items()
#	print res_list
#	print '*' * 40
#	print arr
#	for i in range(1,times+1):
#		for x in range(len(res_list)-1) :
#			if res_list[x][1] > res_list[x+1][1]:
#				res_list[x] , res_list[x+1] = res_list[x+1] , res_list[x]
#	#print res_list
#	#print '-' * 40 
#	#print   res_list[-5:]
#	return  res_list[-times:]	#将统计出来最大的ip出现次数
#===========================>用sorted()函数和lambda匿名函数用一行代码可以实现maopao_sort()函数的功能



def write_html(file,mode,result,times=10):
#将上述排序结果写入到html页面中
	ip_html = open(file,mode)#"w"模式一打开文件就清空了
	sentens = "<tr><td>No%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" #将html设为格式变量,方便后边调用 
	html_str = "<table border='1px'>" + sentens%(' ',"IP","URL","times")
#	count = 0
#	for r in result[::-1]:#用列表切片以及步长设置为-1实现写入文件时从最大到最小
#		count += 1
#		print r 
#		html_str += sentens %(count,r[0][0],r[0][1],r[1])
#用下边更为简单的方式替换实现
	for index ,r in enumerate(result[:-(times+1):-1]):#通过这种遍历,可以直接获取列表的索引值
		html_str += sentens %((index+1),r[0][0],r[0][1],r[1])
	html_str += "</table>"
	ip_html.write(html_str)
	ip_html.close()



def start():
	if __name__ == "__main__" :
		res1 = getip(filename="log.log",mode='r')
		#res2 = maopao_sort(res1,10)===>被替换为下边代码,在统计getip()函数中return返回中使用lambda搞定,如下:
														#return sorted(res_dict.items(),key=lambda x:x[1])
		write_html("/var/www/html/final_count_ip.html","w",res1)



start()
