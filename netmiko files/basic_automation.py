#Import the ConnectHandler from netmiko library
from netmiko import ConnectHandler
#Import getpass to be used on password retrieval
from getpass import getpass
#Import necessary modules for password retrieval
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException



####DECLARE VARIABLES###

#Ask user for username and password
print("Please iput user credentials")
username = input("Username: ")
password = getpass()

'''These are the devices to be configured.
For device_type value, it can be found here: https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py#L70'''
R1 = { 
'device_type': 'cisco_ios', 
'host': '192.168.1.1', 
'username': username, 
'password': password,
}

R2 = { 
'device_type': 'cisco_ios', 
'host': '192.168.1.2', 
'username': username, 
'password': password,
}

'''Make a dictionary of configuration file and device to be configured.
Example:
'R1' => file name of configuration file
R2 => dictionary of the device stated on first part'''
devices = {'R1':R1,'R2':R2}






#Loop through the devices dictionary
for config,device in devices.items():

	#Handle exceptions
	try:
		net_connect = ConnectHandler(**device)
	except(AuthenticationException):
		print("Wrong username or password on " + device['host'] )
		continue
	except(SSHException):
		print("Failed to connect to " + device['host'])
		continue
	except (NetMikoTimeoutException):
		print ('Timeout to device: ' + device['host'])
		continue
	except Exception as unknown_error:
		print("Some other error: " + str(unknown_error))
		continue

	print("Connecting to "  + device['host'])
	print("Configuring " + device['host'] + " with configuration file " + config  )

	file = open(config)
	config = file.read().splitlines()
	output = net_connect.send_config_set(config)
	print(output)

print("Configuration of Devices Completed")
