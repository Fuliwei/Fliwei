#!/usr/bin/python
#coding:utf-8
import os
os.system('clear')
def getip(filename,mode):
	res_dict = {}
	log_f = open(filename,mode) #打开文件方式一,记得要关闭文件
	#with open("log1.log","r") as log_f #打开文件方式二，用完后文件自动关闭,可以同时打开多个文件
	#for line in log_f.readlines():
	for line in log_f:	#打开文件方式一
	#	print line 
		ip = line.strip().split(' ')[0]
		url = line.strip().split(' ')[6]
	#	print ip
		res_dict[(ip,url)] = res_dict.get((ip,url),0)+1 
	log_f.close()
#	print res_dict
#	print '-' * 50
	return res_dict


#将字典通过res_dict.items()转换为列表进行冒泡排序[('218.200.66.205', 1), ('218.200.66.204', 1)]格式大概所示
#冒泡排序对字典所转换的列表中的ip出现次数进行排序
#有可以提升的空间使用sort函数进行排序
def maopao_sort(arr,times):#此处传递字典参数时,只需要当成一个普通参数传递就行.
	res_list = arr.items()
#	print res_list
#	print '*' * 40
#	print arr
	for i in range(1,times+1):
		for x in range(len(res_list)-1) :
			if res_list[x][1] > res_list[x+1][1]:
				res_list[x] , res_list[x+1] = res_list[x+1] , res_list[x]
	#print res_list
	#print '-' * 40 
	#print   res_list[-5:]
	return  res_list[-times:]	#将统计出来最大的ip出现次数

def write_html(file,mode,result):
#	print result
#将上述排序结果写入到html页面中
	ip_html = open(file,mode)#"w"模式一打开文件就清空了
	html_str = "<table border='1px'>"
	count = 0
	for r in result[::-1]:#用列表切片以及步长设置为-1实现写入文件时从最大到最小
		count += 1
	#	print r 
		html_str += "<tr><td>No%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" %(count,r[0][0],r[0][1],r[1])
	html_str += "</table>"
	ip_html.write(html_str)
	ip_html.close()



def start():
	if __name__ == "__main__" :
#		print __name__
		res1 = getip(filename="log.log",mode='r')
		#print res1
		res2 = maopao_sort(res1,10)
		#print res2
		write_html("/var/www/html/hanshu_count_ip.html","w",res2)



start()
