#ssh client in python example
pip install paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(server,port,username,password)
dir = directory
command = command
#change directory to the location of where you want to run the command and 
#change command to the command you want to execute
client.exec_command(f'cd {dir}; {command}')
client.close()