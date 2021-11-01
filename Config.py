import getpass
import sys
import telnetlib

HOST = "192.168.5.201"
user = raw_input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
    
tn.write("enable\n")
tn.write("cisco\n")
#tn.write("wr\n")
#tn.write("conf t\n")
tn.write("interface vlan 10\n")
tn.write("ip address 10.10.10.1 255.255.255.0\n")

#tn.write("end\n")
tn.write("exit\n")

print tn.read_all()