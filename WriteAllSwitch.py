import getpass
import sys
import telnetlib

def configWrite():
    tn.write("enable\n")
    tn.write("cisco\n")
    tn.write("wr\n")
    #tn.write("conf t\n")
    #tn.write("hostname SW" + str(n) +"\n")
    #tn.write("ip address 10.10.10.1 255.255.255.0\n")

    #tn.write("end\n")
    tn.write("exit\n")

user = raw_input("Username: ")
password = getpass.getpass()

for n in range (1,8):
    HOST = "10.99." + str(n) + ".1"
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    configWrite()

    print tn.read_all()