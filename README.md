# Mass Mikrotik Executor
Mass Mikrotik Executor (also known as MME) is a very simple script written in Python ❤️ to connect and execute multiple commands on Mikrotik devices at once. It comes very useful when you have to handle hundreds or thousands of routers/switches. This tool is not limited to Mikrotik, but it can be used with any other networking device that support SSH.

With *MME* you can customize in `/config` the commands to be executed (one per line), the devices to connect to, the users, the passwords and the ports (in case they aren't all the same) to be used. *MME* will try for all the IPs all the combinations within Users, Passwords and Ports you have specified in the config files. Keep in mind this **is not a bruteforce tool** and should not be used for that purpose. Plus, modifying the speed of the tool's logic might result in malfunctioning of the tool itself.

<ins>*I am not responsible for any illegal use of my tool, use it always on devices you have permission to work on.*</ins>


<a href="https://github.com/NazgulCoder/Mass-Mikrotik-Executor/releases/" target="_blank">Download</a>

<a href="https://www.virustotal.com/gui/file/7d14b113fccd4143f356417ba7f66fe3d673b1dac6b6b1f707e62a8e6a9aab3b" target="_blank">VirusTotal</a>

For the compiled version I used auto-py-to-exe and might flag multiple false positives.

# Instructions
- Write the commands you wish to execute (one per line) in this file `/config/command.txt`

- Write the IPs of your Mikrotiks (one per line) in this file `/config/mikrotik.txt`

- Write the user (if among your devices you have used different users you can write multiple entries one per line) in this file `/config/user.txt`

- Write the password (if among your devices you have used different passwords you can write multiple entries one per line) in this file `/config/password.txt`

- Write the SSH port (if among your devices you have used different SSH ports you can write multiple entries one per line) in this file `/config/port.txt`


Then execute either the python version, or the compiled binary if you don't have Python installed. *MME* will try to connect to each device you specified the IP with the indicated user and passwords (if multiple entries have been specified in the config files then *MME* will try them all).

*MME* will save logs in `/log`


If you are a Mikrotik user you may want to check my other appreciated repo <a href="https://github.com/NazgulCoder/Mikrotik-IP-Firewall" target="_blank">Mikrotik IP Firewall</a> 



## LICENSE



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

MIT License

Copyright (c) [2023] [NazgulCoder]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
