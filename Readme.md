/*
##Fuliwei
#####
需求:分析access.log的Nginx日志,对ip进行统计后打印出前十访问量的ip。

###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
思路:

1.读取日志文件对每行进行strip()和split(' ')操作

2.对操作后的数据列表取出第1列即访问的ip

		高逼格代码,用get()可以最优统计出ip的个数

		d[ip] = d.get(ip,0)+1	===>高逼格代码来统计ip次数，避免了代码冗余,一行代码完成if else的功能

3.将ip已经访问的次数统计出来存在字典中,以ip为key，次数为value

4.将步骤三中的字典翻转过来,变成以访问次数为key,将统计出来的ip追加到访问次数中

	注意此处可以装逼:

		翻转前字典:before_dict = {}

		翻转后字典:after_dict = {}

				for key,value in before_dict.items():

					after_dict.setdefault(value,[])

					after_dict[value].append(key)

		======> 得到最终的翻转后字典after_dict

5.打开一个文件,命名为*.html , result_f = open("*.html",'a+')

依次写入*.html文件中

result_f.write("<html><table style='border:solid 1px'>") #注此处为数字1字母px,html语言中定义字体的

result_f.write("<th style='border:solid 1px'>顺序</th><th style='border:solid 1px'>次数</th><th style='border:solid 1px'>ip地址</th>")

key = max(after_dict.keys()) ===> 注意字典是无序的,用max方法找出key中出现最大的次数

for i in after_dict[key]:

	result_f.write("<tr><td style='border:solid 1px'>%d</td><td style='border:solid 1px'>%s</td><td style='border:solid 1px'>%s</td></tr>" %(count,key,i))

after_dict.pop(key)  ===>每取完一次最大值就从字典中删除对应的key,value对。以保证上边每次去的都是最大值

result_f.write("</table></html>")

result_f.close()  ===>打开文件后就要关闭文件

6.蜗牛进阶：用冒泡排序实现最大次数筛选,具体脚本见count_ip.py
	
	知识点:1.用元组作为字典的key可以实现多维度的统计，如统计url、ip两个维度如何实现(见脚本count_ip2.py)

		   即实现真正的访问同一条url的ip才算是相同的访问记录
		   
           多维度的赋值:

				常见赋值:
					for line in log_f:   

   						ip = line.strip().split(' ')[0]===>可以优化为如下:tmp = line.strip().split(' ')

    					url = line.strip().split(' ')[6]===============> ip , url = tmp[0] ,tmp[6]

    					res_dict[(ip,url)] =res_dict.get((ip,url),0)+1
	
				简化赋值:

					变量1 , 变量2 ...  = value1 ,value2 ...			

		   2.打开文件操作为了避免忘记关闭文件可以使用with,还可以一次打开多个文件

			with open("文件名","模式") as f:

			with open("文件名1"，"模式") as  f1 ,open("文件名2"，"模式") as  f2 ,open("文件名3"，"模式") as  f3  ...

			更加优雅的语法:

			from contextlib improt ExitStack

			with ExitStack() as stack:
  		 		
			files = [stack.enter_context(open(fname)) for fname in [filename1, filename2, filename3]]
    		
				for i, j, k in zip(files[0], files[1], files[2]):
        		
					print(i, j, k)
			
		  3.用简单的函数进行改造,实现统计数据的功能.见(hanshu_countip.py)文件
			
			注意:需要传参时:参数类型为字典或者列表时,这两种数据类型为一个整体,直接当变量就行;
				
				当要传参数不确定时,使用*来获取,收到的为元组数据;当要传参数为关键字参数时,使用**来获取
		
			*********************************************************************
			def show(name):
				print name

			show([1,2,3,4])		=====>[1,2,3,4]
			show({"name":"liwei","age":12})			====>{"name":"liwei","age"=12}
			***********************************************************************
			-----------------------------------------------------------------------------------------------------------------	
			#def show(*name)
			#	print name
			#show([1,2,3,4],{"name":"liwei","age":12})	=====>	([1, 2, 3, 4], {'age': 24, 'name': 'xiaowei'}) ==><type 'tuple'>
			-----------------------------------------------------------------------------------------------------------------
			
		4.python自带的sorted()函数和lambda匿名函数

			lambda匿名函数:1.特别简单的没有名字的函数,只有return语句的函数

						   2.格式:lamda 参数：返回值			##多个参数，逗号间隔

						   3.小例子：>>> hello = lambda x:x[1]		>>> print hello([1,2,3])====>2
			
			sorted()函数：1.格式   sorted('待排序的list'，key='要排序的值')
		
						  2.sorted()结合lambda函数使用来简化代码

							print sorted(arr_dict,key=lambda x:x["times"])	#日志中统计ip后通过这条语句可以找到前几的ip以及次数

*/
