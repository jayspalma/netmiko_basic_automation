#Import the ConnectHandler from netmiko library
from netmiko import ConnectHandler

'''These are the devices to be configured.
For device_type value, it can be found here: https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py#L70'''
R1 = { 
'device_type': 'cisco_ios', 
'host': '192.168.1.1', 
'username': 'cisco', 
'password': '12345678',
}

R2 = { 
'device_type': 'cisco_ios', 
'host': '192.168.1.2', 
'username': 'cisco', 
'password': '12345678',
}


'''Make a dictionary of configuration file and device to be configured.
Example:
'R1' => file name of configuration file
R2 => dictionary of the device stated on first part'''
devices = {'R1':R1,'R2':R2}

#Loop through the devices dictionary
for config,device in devices.items():
	print("Connecting to "  + device['host'])
	net_connect = ConnectHandler(**device)
	print("Configuring " + device['host'] + " with configuration file " + config  )

	file = open(config)
	config = file.read().splitlines()
	output = net_connect.send_config_set(config)
	print(output)

print("Configuration of Devices Completed")
