# Flexion CMS Project

## Introduction
This repository is for use for tech demos and illustrations of creator knowledge base. The tool I used to define my requirements and organize my work was Trello, located at the following URL: https://trello.com/b/wPVMt5sC/flexion-cms-coding-challenge

## Instructions
1. For the prospective user concerned with accessing this basic program, for security purposes, a set of 3 emails should have been sent to you containing the following:
* An email that contains the DNS name of the PROD Server containing the application, the username that has access, and a private ssh key ssh into the system
* An email that contains the URL of the Jenkins Server that deploys the the TEST and the PROD servers and an assigned username that has been created.
* An email that contains the password to unlock the encryption on the private key and for use with the Jenkins server

2. For the purposes of this tech demo, you need not run any new deployments on Jenkins. The production code in the master branch has already been deployed to the PROD server that you have been given access to. This Jenkins instance has been configured to continuously poll the repository for any changes and subsequently integrates and deploys to my servers. If you would like to run a deployment, you are free to. Simply follow the steps:
* From the Home page of Jenkins, click "Open Blue Ocean" in the side bar on the left side of the screen.
* Click on "Flexion Deployment Pipeline"
* Click on "Branches" 
* Click "master" which deploys to the PROD server
* Click the semi-circular toward the top of the page if you would like to "Re-run" the deployment

3. In order to access the program, please follow the given steps below: 
* Log into the given PROD server (in the email you should have received) via Bash, PuTTY, etc. 
* From the home directory, run the following command "cd APP"; this is where the program is hosted
* Once in the correct directory, run the following command: "python3.6 flexion.py"
* Enjoy using the program! Obey the initial prompt in the program for details on how to use it.


Please email me at wilson.d.bui@hotmail.com if you have any questions! Thanks.