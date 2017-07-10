#!/usr/bin/python

import socket,os,sys,commands,time

ser=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ser.bind(("",2345))
ser_ip="192.168.10.149"
ser_port=2345
status1="done"

while True:
	data=ser.recvfrom(50)
	drive_name=data[0]
	data1=ser.recvfrom(50)
	drive_size=data1[0]
	client_ip=data[1][0]
	os.system('fallocate -l '+drive_size+'M '+drive_name+'.txt')
	os.system('mkfs.fat '+drive_name+'.txt')
	os.system('mkdir /media/'+drive_name)
	os.system('mount '+drive_name+'.txt /media/'+drive_name)
	#os.system('yum install nfs-utils -y')
	os.system('setenforce 0')
	os.system('iptables -F')
	os.system('systemctl stop firewalld')
	os.system('systemctl restart nfs')
	exports_data="/media/"+drive_name+" "+client_ip+"(rw,no_root_squash)"
	f=open('/etc/exports','a')
	f.write(exports_data)
	f.write("\n")
	f.close()
	os.system('exportfs -r')
	os.system('systemctl restart nfs')
	print "Successfully Done :---!!!!"
	time.sleep(5)
	os.system('exit')	
