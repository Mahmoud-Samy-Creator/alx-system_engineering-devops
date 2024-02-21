# Issue Summary:
The issue with An Apache server
duration of the outage: 2:00 AM to 4:00 AM
Impact: The user or admin tries to curl the port 8080 mapped to the Docker container port 80, it does not return a page but an error message. The user or an admin might also get the error message curl: (52) Empty reply from server.
The root cause: There was a mistake in the server configuration.

# Timeline
Issue detection time: 2:24 AM
The issue detection method: monitoring alerts & customer complaints.
Actions taken:
Checking that the server has a copy of   /etc/passwd file in /tmp
have a file named /tmp/isworking containing the string OK  
Make some server tests:
vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
vagrant@vagrant:~$ curl 0:8080
curl: (52) Empty reply from server
vagrant@vagrant:~$
Identify the goal to reach:
vagrant@vagrant:~$ curl 0:8080
Hello Holberton
vagrant@vagrant:~$
Team/individuals were the incident escalated to the System admin
how the incident was resolved
By restarting the Apache server

# Root cause and resolution must contain:
The Root cause of the issue is avoiding server refreshing
The issue was fixed by refreshing the server by restarting it, and making a bash script for future usage, this script ran a command for Apache server restarting.




# Corrective and preventative measures:
Set a period to improve the server performance
Refreshing server after a certain period.


