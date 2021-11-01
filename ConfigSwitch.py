import getpass
import sys
import telnetlib

user = raw_input("Username: ")
password = getpass.getpass()
num = 0
#Write Configuration All Switch
def configWrite():
    tn.write("enable\n")
    tn.write("cisco\n")
    tn.write("wr\n")
    tn.write("exit\n")

# Create Multiple Vlan form "FOR" or "NUM++"
def configCreateVlan(parameter):
    tn.write("enable\n")
    tn.write("cisco\n")
    tn.write("conf t\n")
    tn.write("interface vlan " + str(parameter) + "\n")
    tn.write("ip address 10.100." +  str(parameter) + ".254 255.255.255.0\n")
    tn.write("end\n")
    tn.write("exit\n")s

# Change Multiple Switch Name form "FOR" or "NUM++"
def configHost(parameter):
    tn.write("enable\n")
    tn.write("cisco\n")
    tn.write("conf t\n")
    tn.write("hostname Switch" + str(parameter) +"\n")
    tn.write("end\n")
    tn.write("exit\n")

for n in range (201,207):
    HOST = "192.168.5." + str(n)
    tn = telnetlib.Telnet(HOST)
    num += 1

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    configHost(num)
    configWrite()

    print tn.read_all()