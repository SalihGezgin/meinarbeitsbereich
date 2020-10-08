Hands-on EC2-06 : Working with Application Load Balancer (ALB) using a Launch Template
Purpose of this hands-on training is to learn Application Load Balancer (ALB) working process. Especially, we’ll cover the details of the AWS solution suite and walk through how to set up a basic ALB.

Learning Outcomes
At the end of the this hands-on training, students will be able to;

create security group.

create a target group.

create Application Load Balancer.

attach target group to ALB.

Outline
Part 1 - Creating a Security Group

Part 2 - Launch Instances with Launch Template

Part 3 - Creating a Target Group

Part 4 - Creating Application Load Balancer together with Target Group

Part 1 - Creating a Security Group
Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

Choose Security Groups on the left-hand menu,

Click the "Create Security Group" tab.

Security Group Name  : ALBSecGroup
Description         : ALB Security Group
VPC                 : Default VPC
Inbound Rules:
    - Type: SSH----> Source: Anywhere
    - Type: HTTP ---> Source: Anywhere
Outbound Rules: Keep it as it is
Tag:
    - Key   : Name
      Value : ALB SEC Group
Click "Create Security Group" button.
Part 2 - Launch Two Instance Using the Launch Template
Step 1 - Launch Template Configuration
5 Launch Template Name

Launch template name            : ALBtemplate
Template version description    : ALBtemplate
Amazon Machine Image (AMI)
Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type, (us-east-1)
Instance Type
t2.micro
Key Pair
Please select your key pair (pem key) that is created before
Example: clarusway.pem
Network settings
Network Platform : Virtual Private Cloud (VPC)
Security groups
Please select security group named ALBSecGroup
Storage (volumes)
keep it as default (Volume 1 (AMI Root) (8 GiB, EBS, General purpose SSD (gp2)))
Resource tags # bu templateden oluşacak instancelara verilecek isim
Key             : Name
Value           : ALBInstance
Resource type   : Instance
Network interfaces
Keep it as it is
Within Advanced details section, we will just use user data settings. Please paste the script below into the user data field.
#!/bin/bash

#update os yum update -y #install apache server yum install -y httpd

get private ip address of ec2 instance using instance metadata
TOKEN=curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"
&& PRIVATE_IP=curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/local-ipv4

get public ip address of ec2 instance using instance metadata
TOKEN=curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"
&& PUBLIC_IP=curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4

get date and time of server
DATE_TIME=date

set all permissions
chmod -R 777 /var/www/html cd /var/www/html wget https://raw.githubusercontent.com/awsdevopsteam/ngniex/master/ryu.jpg

create a custom index.html file
echo "

<title> Congratulations! You have created an instance from Launch Template</title>
This web server is launched from launch template by AWSDevOps Team
This instance is created at $DATE_TIME

Private IP address of this instance is $PRIVATE_IP

Public IP address of this instance is $PUBLIC_IP

Oz Hakiki Cikolata Deryasi

" > /var/www/html/index.html # start apache server systemctl start httpd systemctl enable httpd
Step-2: Launch Two Instances Using the Launch Template
Go to Launch Templates section on left-hand menu on AWS EC2 Dashboard.

Select the launch template named ALBtemplate.

Click Actions >> Launch instance from template interface.

Number of instances  : 3
Click "Launch Instance from Template"

Go to the instance page from the left-hand menu . Show the differences of newly created instances on the browser (IP and dates) via entering public IP addresses.

Part 3 - Create a target group
Go to Target Groups section under the Load Balancing part on left-hand side and click it.

Click Create Target Group button.

Basic configuration.

Choose a target type    : Instances
Give Target Groups Name : MyFirstTargetGroup
Protocol                : HTTP
Port                    : 80
VPC                     : Default
Health checks
Health check protocol   : HTTP
Health check path       : /
Advance Health check settings.
Port                    : Traffic port
Healthy treshold        : 5
Unhealthy treshold      : 2
Timeout                 : 5 seconds
Interval                : 10 seconds
Succes codes            : 200
Tags
Key                     : Name
Value                   : Target
Click next.

Select two instances that is created from Launch Template before and add to them to the target group.

Ports for the selected instances : 80
Click Include as pending below button.

Show that two instances are added to the target group.

Click Create target group button.

Part 4 - Creating Application Load Balancer together with Target Group
Go to the Load Balancing section on left-hand menu and click Load Balancers.

Tap Create Load Balancer button.

Click Create button inside the Application Load Balancer section.

Step 1 - Configure Load Balancer
Name            : MyFirstALB

Listeners       : A listener is a process that checks for connection requests,
using the protocol and port that you configured.

Load Balancer Protocol      : HTTP
Load Balancer Port          : 80
Availability Zones          : Choose all AZ's

Add-on services             : Keep it as it is
Tags                        :
    - Key   : Name
    - Value : MyFirstALB
Step 2 - Configure Security Settings
You'll see the warning page;

!!! Improve your load balancer security. Your load balancer is not using any secure listener.!!!

This comes because of we didn't choose https for listener ports. We can leave it as it is and click the Next button
Step 3 - Configure Security Groups
Select an existing group.
Name :  ALBSecGroup
Click Next: Configure Routing
Step 4 - Configure Routing
Target group        : Existing target group
Name                : Target
When we select target group it is not necessary to adjust the rest of the settings, since we set all parts while creating Target Group

Click Next: Register Targets
They have also determined by target group named Turgut too. 
Click next button

Review if everything is ok, and then click the Create button

Successfully created load balancer!
Click Close tab

Please wait for State to turn into active from provisioning.

Show on the browser that how the requests are routed to different instance with the help of the ALB.


42. Select Load Balancer named MyFirstALB

43. Copy the ALB's DNS name. It should be something like `MyFirstALB-1185163036.us-east-1.elb.amazonaws.com`

44. Paste is on browser and refresh it

45. Show the changing Public and Private IP addresses and time that the instances was created


46. Explain the monitoring dashboard of ALB.

47. Stop one of the instance from teminal

   sudo systemctl stop httpd

48. Show the health check status of instance from target group

49. Then start the httpd and show the healthcheck status: health

   sudo systemctl start httpd

50. Show Attributes----> Load balancing algorithm------>Round robin

51. Change the "Roud robin" to "Least outstanding requests"