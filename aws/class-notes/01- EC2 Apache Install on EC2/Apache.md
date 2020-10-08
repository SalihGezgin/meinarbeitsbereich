Hands-on EC2-01 : How to Install Apache Web Server on EC2 Linux 2
Outline
Part 1 - Getting to know the Apache Web Server

Part 2 - Launching an Amazon Linux 2 EC2 instance and Connect with SSH

Part 3 - Installing and Configuring Apache Web Server to Run Hello World Page

Part 4 - Automation of Web Server Installation through Bash Script

Part 1 - Getting to know the Apache Web Server
Apache HTTP Server

The Apache HTTP Server, known as Apache, is a free and open-source cross-platform web server software, which is developed and maintained by an open community of developers under the auspices of the Apache Software Foundation.

Part 2 - Launching an Amazon Linux 2 EC2 instance and Connect with SSH
Launch an Amazon EC2 instance with AMI as Amazon Linux 2, instance type as t2.micro and default VPC security group which allows connections from anywhere and any port.

Connect to your instance with SSH.

ssh -i .....pem ec2-user@

Part 3 - Installing and Configuring Apache Web Server to Run Hello World Page
STEP_1
Update the installed packages and package cache on your instance.
sudo yum update -y

Install the Apache Web Server-default page
sudo yum install httpd -y

Start the Apache Web Server.
sudo systemctl start httpd

Check status of the Apache Web Server.
sudo systemctl status httpd

Enable the Apache Web Server to survive the restarts then Check from browser with DNS
sudo systemctl enable httpd #it keep the service start instance restart

Set permission of the files and folders under /var/www/html/ folder to everyone.
sudo chmod -R 777 /var/www/html

Go to the /var/www/html
cd /var/www/html

Create a custom index.html file under /var/www/html/ folder to be served on the Server.
echo "merhaba clarusway" > /var/www/html/index.html

check the index.html ls cat index.html

Restart the httpd server and check from browser

sudo systemctl restart httpd

STEP_2-HTML format
open index.html file with vim editor.
cd /var/www/html vim index.html

press I

clean the existing messsage then paste the html formatted code.
<title> My First Web Server</title>
Hello to Everyone from My First Web Server
Save and exit and show with cat command
ESC :wq cat index.html

Restart the Apache Web Server.
sudo systemctl restart httpd

Check if the Web Server is working properly from the browser.
Part 4 - Automation of Web Server Installation through Bash Script
Configure an Amazon EC2 instance with AMI as Amazon Linux 2, instance type as t2.micro, default VPC security group which allows connections from anywhere and any port.

Configure instance to automate web server installation with user data script.

#! /bin/bash
#update os
yum update -y
#install apache server
yum install -y httpd
# get date and time of server
DATE_TIME=`date`
# create a custom index.html file
echo "<html>
<head>
    <title> My First Web Server</title>
</head>
<body>
    <h1>Hello to Everyone from My First Web Server</h1>
    <p>This instance is created at <b>$DATE_TIME</b></p>
</body>
</html>" > /var/www/html/index.html
# start apache server
systemctl start httpd
systemctl enable httpd
Review and launch the EC2 Instance

Once Instance is on, check if the Apache Web Server is working from the web browser.

Connect the Apache Web Server from the local terminal with curl command.

curl http://ec2-3-15-183-78.us-east-2.compute.amazonaws.com8.us-east-2.compute.amazonaws.com