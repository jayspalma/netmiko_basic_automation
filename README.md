# Basic Network Automation using Netmiko in GNS3 #
This is a basic implementation of Netmiko that configures the interfaces and EIGRP process on a simple network.

Here is the network diagram of the project
![](gns3%20files/network_topology.png)

The project was implemented using the following:
* GNS3 2.2.7
* Python 3.8.1
* Netmiko 3.1.1
* Cisco IOSv 15.6(2)T

To recreate the project:
1. Create the network diagram using gns3.
2. Copy and paste the configuration files found on the gns3 directory to the devices.
    * Note: Files are commented that explains each command.
3. Copy or create the files found on the 'netmiko files' directory to the Netmiko Automation docker.
    * **__It is imperative that the filename of the R1 and R2 files should not be changed.__**
    * **__R1, R2 and basic_automation.py should be on the same directory .__**
4. Run the the basic_automation.py by using the command "python3 basic_automation.py"

## To test if the configuration is successful, PC1 should be able to ping PC2. ##
- ping 10.1.1.3
