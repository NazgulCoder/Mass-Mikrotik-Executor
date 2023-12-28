
import paramiko
import time
import os
import sys  # Importing sys to write to the CLI

# Function to log the result of an operation to a file and print it to the CLI
def log_result(file_name, message):
    with open(file_name, 'a') as file:
        file.write(message + "\n")
    print(message)  # Print to the CLI

# Prepare the log files
log_path = 'log'
success_log_path = os.path.join(log_path, 'success.txt')
fail_log_path = os.path.join(log_path, 'fail.txt')
command_log_path = os.path.join(log_path, 'command-logs.txt')

# Ensure log directory exists
if not os.path.exists(log_path):
    os.makedirs(log_path)

# Function to attempt SSH login and command execution
def ssh_login_execute(ip, users, passwords, ports, commands):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for user in users:
        for password in passwords:
            for port in ports:
                try:
                    ssh.connect(ip, port=int(port), username=user, password=password, timeout=10)
                    # If login is successful, log the success
                    log_result(success_log_path, f"{ip} connection success")
                    # Execute all commands
                    for cmd in commands:
                        if cmd.strip():  # This will ensure empty lines are ignored
                            _, stdout, stderr = ssh.exec_command(cmd)
                            # Wait for the command to execute and get the output
                            time.sleep(5)
                            output = stdout.read().decode('utf-8')
                            error = stderr.read().decode('utf-8')
                            if error:
                                log_result(command_log_path, f"{ip} after command '{cmd.strip()}' execution responded with error: {error}")
                            else:
                                log_result(command_log_path, f"{ip} after command '{cmd.strip()}' execution responded: {output}")
                    # Close the SSH connection
                    ssh.close()
                    return True
                except (paramiko.ssh_exception.NoValidConnectionsError, 
                        paramiko.ssh_exception.AuthenticationException, 
                        paramiko.ssh_exception.SSHException) as e:
                    # Log the exception but continue trying
                    log_result(command_log_path, f"{ip} encountered an error: {e}")
                except Exception as e:
                    # Log any other exception and move to the next IP
                    log_result(command_log_path, f"{ip} encountered an unexpected error: {e}")
                    continue
    # If login was not successful with any combination, log the failure
    log_result(fail_log_path, f"{ip} connection failed after all combos")
    return False

# Read the lists of IPs, usernames, passwords, ports, and commands from files
def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]  # Ignore empty lines

config_path = 'config'
mikrotik_ips = read_file_to_list(os.path.join(config_path, 'mikrotik.txt'))
passwords = read_file_to_list(os.path.join(config_path, 'password.txt'))
ports = read_file_to_list(os.path.join(config_path, 'port.txt'))
users = read_file_to_list(os.path.join(config_path, 'user.txt'))
commands = read_file_to_list(os.path.join(config_path, 'command.txt'))  # Now reading all commands

# Iterate over each IP and attempt to execute the command
for ip in mikrotik_ips:
    ssh_login_execute(ip, users, passwords, ports, commands)
