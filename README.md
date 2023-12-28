# Mass Mikrotik Executor
Mass Mikrotik Executor (also known as MME) is a very simple script written in Python ❤️ to connect and execute multiple commands on Mikrotik devices at once. It comes very useful when you have to handle hundreds or thousands of routers/switches. This tool is not limited to Mikrotik, but it can be used with any other networking device that support SSH.

With *MME* you can customize in `/config` the commands to be executed (one per line), the devices to connect to, the users, the passwords and the ports (in case they aren't all the same) to be used. *MME* will try for all the IPs all the combinations within Users, Passwords and Ports you have specified in the config files. Keep in mind this **is not a bruteforce tool** and should not be used for that purpose. Plus, modifying the speed of the tool's logic might result in malfunctioning of the tool itself.

I am not responsible for any illegal use of my tool, use it always on devices you have permission to work on.


<a href="https://github.com/NazgulCoder/Mass-Mikrotik-Executor/releases/" target="_blank">Download</a>

<a href="https://www.virustotal.com/gui/file/7d14b113fccd4143f356417ba7f66fe3d673b1dac6b6b1f707e62a8e6a9aab3b" target="_blank">VirusTotal</a>

For the compiled version I used auto-py-to-exe and might flag multiple false positives.


# Donations
- ![image](https://github.com/NazgulCoder/NazgulCoder/assets/85739956/bfb37ab3-5245-4b98-bd9f-08813b262117) bc1qvcr8nv6la58jp5y29s28dkrnr8v3ukn9tgztea
- ![image](https://github.com/NazgulCoder/NazgulCoder/assets/85739956/de324b88-2251-4371-81cc-0aecbd5e7272) 0xca834fbF25B32fB887aeb88FD28567c26e268200
- ![image](https://github.com/NazgulCoder/NazgulCoder/assets/85739956/4af1b069-e320-4727-85e1-94a3755f554f) LKbqJPJeUHcWVPYkLGb14QsUm1ZvBvfzsM


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
