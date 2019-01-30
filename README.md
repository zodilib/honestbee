#HonestBee Dir Structure 

.
├── GithubStats      ---> Assignment#1 "Github Stats"
│   ├── Dockerfile
│   ├── README.md
│   ├── example_list.txt
│   └── gitrepocheck.py
├── README.md
├── dockercompose     ---> Assignment#2 "Docker Nginx + Log Management"
│   ├── docker-compose.yml
│   ├── fluentd
│   │   ├── Dockerfile
│   │   └── conf
│   │       └── fluent.conf
│   └── nginx
│       ├── Dockerfile
│       └── index.html
└── iac                --->  Assignment#2 "Docker Nginx + Log Management"   IAC
    └── iac.json


#### Assignment#1 "Github Stats" - 
A seperate "README.md" is included under "GithubStats" directory. 


#### Assignment#2 "Docker Nginx + Log Management" - 
Docker compose file to create a NEFK ( Nginx, Elasticsearch, Fluentd and Kibana ) cluster.

Steps - 

1. Please clone the repo "https://github.com/zodilib/honestbee.git".
2. Under the directory "dockercompose" , run the command "docker-compose up"
    Requirement - a. Docker should be installed and running
                  b. Docker compose should be installed.



#### Assignment#2 "Docker Nginx + Log Management"   IAC
A cloudformation template is being provided to create the docker cluster of NEFK on a EC2 instance.

Steps - 
1. Please clone the repo "https://github.com/zodilib/honestbee.git".
2. Under the directory "iac", use the "iac.json" to create a stack on AWS Cloudformation.
   Requirement - a. User needs to have  access to create security group, create EC2 instances.
                 b. User needs to have an associated "ssh key" for a respective region. 

3. Output is provided in the Output section of the respective Stack.

    
NOTE - Please give 5 - 10 min for the docker-compose to finish. 


 

