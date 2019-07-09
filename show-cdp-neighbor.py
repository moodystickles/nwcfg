# output "sh cdp neighbor" command to console and write to txt file
# txt file saved to same directory as script

# import modules
from netmiko import ConnectHandler
import getpass
import subprocess

# prompt for hostname,user,pw
host = input('host:')
user1 = input('Username:')
p = getpass.getpass()

# create device object
R1 = {
    'host': host,
    'username': user1,
    'password': p,
    'device_type': 'cisco_ios',
}

# establish ssh connection to device
net_connect = ConnectHandler(**R1)

# define and open text file
file = open(host + '_sh-cdp-nei.txt', 'w')

# define command to send to device
command = 'show cdp neighbor'

# send command to device and disconnect
output = net_connect.send_command(command)

# disconnect ssh session
net_connect.disconnect()

# print output to console
print(output)
print()
print()
	
# Write output to file and close
file.write(output)
file.close()