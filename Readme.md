#Writing Test Functions
Created a Python Project on PyCharm named (Adv_581_Revision)

Create a class (MathUtils)that performs four operations:add,subtract,multiply and divide

Create a Python test file named test_math_utils.py to test the methods of the MathUtils class.

Write test cases for each of the methods in the MathUtils class using pytest

Just typed the command (pytest) on command line to see the test results on Pycharm

Created a git repository on the local system using (git init) to initialise a repository.

Created a new repository on github 

Established connection of local repository to github using the command:(git remote add origin <repository_url>)
Verify if the connection is established:(git remote -v)
Then we do a command process to  push the files into github after every change in files:
(git add .)
(git commit -m "message to be written")
(git push )

git branch (To view which branch we are currently on)
git checkout <branch_name> (to shift branch) 


#Installation of Jenkins
First Check for the availability of JDK,if not,install Jdk version as per the requirements.(JDK 11,17 0r 21)
Then Install Jenkins from (https://www.jenkins.io/download/),Install an LTS(Long term Support )version.
Then Install the package and follow the instructions
Logon Type:Select Run service as LocalSystem
Setup local host:I chose local host 8081(Test port after it has been assigned)
Set the JDK path
Click Next
Then Finish all the processes
Unlock Jenkins By the Administrator Password,Copy the password from the file location
Install Suggested Plugins
Configure Username,Password and Email address
Set Instance Congifuration,i.e,Jenkins URL ,Start Jenkins at :(https://localhost:8081/)
Jenkins is all SetUp.
#EXECUTION ON JENKINS

Create a new Item
Choose anyone(freestyle,pipeline) 
