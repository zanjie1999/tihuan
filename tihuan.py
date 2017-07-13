# -*- encoding:utf-8 -*-

#批量修改程序
#版本 1.0

import os
import fnmatch
import time;

#查找要修改的文件
def SearchFile(path, fnexp):
	print"正在查找要修改的文件..."
	for root, dirs, files in os.walk(path):
		for filename in fnmatch.filter(files, fnexp):
			yield os.path.join(root, filename)

#替换了写到文件里
def gochange(name, change, changed, logFile):
	f = open(name,"r")
	tmp = f.read()
	if (change in tmp):
		tmp = tmp.replace(change,changed)
		changedFileText = "已替换: "+name
		print changedFileText
		logFile.write(changedFileText+"\n")
	f = open(name,"w")
	f.write(tmp)
	f.close()

if __name__ == '__main__':

	#原文
	change = '''la'''
	#替换后
	changed = '''lallalalalallalal'''
	#查找文件名
	filename = "asdfgh*"

	localtime = time.asctime( time.localtime(time.time()) )
	logFile = open("tihuan.log", "a") 
	startText = "开始 "+localtime
	print startText
	logFile.write(startText+"\n")
	for name in SearchFile(r"./", filename):
		gochange(name, change, changed, logFile)
	localtime = time.asctime( time.localtime(time.time()) )
	stopText = "完成 "+localtime
	print stopText
	logFile.write(stopText+"\n\n")
	logFile.close()

