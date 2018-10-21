# Create a Jupyter Notebook with EC2 Backend

This provides a walkthrough of creating a Jupyter Notebook powered by EC2. This is a tangible takeaway from Big Data week: if you create a Jupyter Notebook with AWS backend, you can create an image of the environment and dial up its power. That way, when you're provided with a large dataset as a part of an interview, you will not have to spend the time setting this up, and can instead immediately begin your analysis.

This has been adapted from [here](https://gist.github.com/iamatypeofwalrus/5183133), which means as you run into errors along the way, noting what other Github users have done to overcome potential errors is useful. For example, previous DSI students have turned to this [gist](https://gist.github.com/theredpea/23362010903f501ee120) for some fixes.


# What
Roll your own iPython Notebook server with Amazon Web Services (EC2) using their Free Tier.

# What are we using? What do you need?
- An active AWS account. First time sign-ups are eligible for the [free tier](http://aws.amazon.com/free/) for a year
- One Micro Tier EC2 Instance
- With AWS we will use the stock Ubuntu Server AMI and customize it.
- [Anaconda](https://store.continuum.io/cshop/anaconda) for Python.

# Why?
I had been looking for complete tutorials on setting up my own iPython Notebook on EC2 from scratch and I couldn't quite find what I was looking for. I hope someone finds this useful!

# How
## AWS Console and EC2 Instance Launch.
- Head over to the [AWS Console](http://aws.amazon.com/console/) and log in.
- We're going to _Launch an Instance_. If this is your first time at the Rodeo you won't have any instances listed.

![Launch Instance](http://dl.dropbox.com/u/550268/iPython%20Gist/LaunchInstance.png)

- We're going to use the _Classic Wizard_ for the Instance Creation

![Classic Wizard](http://dl.dropbox.com/u/550268/iPython%20Gist/Instance_Creation_Wizard.png)

- There are many OS's to choose from. All the eligble OS's eligible for the Free Tier are marked by big, bold stars. We're going to use _Ubuntu Server 12.04.1 LTS_.

![Ubuntu](http://dl.dropbox.com/u/550268/iPython%20Gist/Ubuntu.png)

- The free tier is only eligible for the _T1 Micro_. I will use all defaults here.

![Instance Type](https://dl.dropbox.com/u/550268/iPython%20Gist/InstanceType.png)

- Again in the Advanced Instaces options I leave all options at their _default_ settings.

![Advanced Instance Questions](https://dl.dropbox.com/u/550268/iPython%20Gist/AdvancedInstanceQuestions.png)

- You can create tags for machines. I haven't found the need to yet. _Defaults!_

![Tags](https://dl.dropbox.com/u/550268/iPython%20Gist/Tags.png)

- The Wizard is going to ask you to create a public key (or use an existing one if this isn't your first time). Create and download that key and save it in a nifty (read: memorable) spot.

- The _Security Group_ step is a very important step. This step can only be configured when you launch the instance! Under the Create New Security Group.

![Security Groups](https://dl.dropbox.com/u/550268/iPython%20Gist/SecurityGroupsInstance.png)

- You should have rules for SSH(22): 0.0.0.0/0, HTTPS(443): 0.0.0.0/0, and 8888: 0.0.0.0/0. Where 0.0.0.0/0 means access from *ANY* outside I.P. address. We will use port 8888 for our iPython Notebook server. Your rules should look like the right hand size of the photo below.

![SecurityGroup](https://dl.dropbox.com/u/550268/iPython%20Gist/SecurityGroup.png)

- This is the last page of the Wizard! Review the options you set and if they look good the you're all set.

![Instance Details Complete](https://dl.dropbox.com/u/550268/iPython%20Gist/InstanceDetailsComplete.png)

## SSH-ing into your Instance
- I'm going to assume you're using the Terminal in Mac OS X (or something vaguely Unix-y).
- _Right-Click_ on the instance you just created from the Instances panel then click _Connect_

![Connect with SSH Client](https://dl.dropbox.com/u/550268/iPython%20Gist/ConnectWithSSHClient.png)

- The _Connect_ diaglog box will give you some code you can use to log in to your instance. In your terminal Navigate to where you saved your PEM key and run the command from there. **WATCH OUT #1:** If you haven't changed the permissions on your key then the server is going to reject the connection. CHMOD 400 (your PEM). **WATCH OUT #2:** Ubuntu wants you to login as ubuntu rather than root. Change that.
- Here's an example of my terminal ouput with both of those "gotcha's" happening.

![Unprotected PEM](https://dl.dropbox.com/u/550268/iPython%20Gist/UnprotectedPem.png)
![CHMOD Pem](https://dl.dropbox.com/u/550268/iPython%20Gist/CHMODPem.png)

- If all goes well then you're logged in!

## Setting up your Python Environment
- Now it's time to set up your python environment with [Anaconda](http://continuum.io/downloads.html). Use wget to download the Anaconda installer to your server

![Get Anaconda](https://dl.dropbox.com/u/550268/iPython%20Gist/GetAnaconda.png)

- Run the Bash script. I've will leave everything with its default setting. Anaconda will install everthing in an folder in your home directory.

![Run Anaconda](https://dl.dropbox.com/u/550268/iPython%20Gist/RunAnaconda.png)

- After a few minutes the install will finish and tell you to put the folder that was just created at the top of your $PATH. Modify your .bashrc.

![Modify Bash](https://dl.dropbox.com/u/550268/iPython%20Gist/ModifyBash.png)

![Add Path to Bash](https://dl.dropbox.com/u/550268/iPython%20Gist/AddPathToBash.png)

- Make sure to reload your .bashrc with the source command. You can double check which Python you are using by calling: $ which python

![Reload source](https://dl.dropbox.com/u/550268/iPython%20Gist/source.png)

- Say whaaaat? Now you've got a pretty good base to do all your Scientific Computing in Python.

## Setting up iPython Notebook
- We're almost there. I can feel it. We've got a few more steps: Create a iPython Profile for our server; Create a password for our notebook log in; Create a self-signed SSL certificate for HTTPS access; and finally modify our ipython_notebook_configuration.py file. **Much of (if not all) of this code follows the iPython Notebook doc very closely**.

- From anywhere type:
    $ ipython profile create nbserver

- Next, we're going to create a password for your notebook server. I'm going to do everything from within iPython right now. You can access the shell commands by prepending your commands with "!". Some commands like "cd" and "ls" don't need an "!" in front. It's pretty awesome. See "Magic Functions" in the resources section.
- The output of passwd() is going to be used in the notebook configuration file later. So save/remember it!

![Make Password](https://dl.dropbox.com/u/550268/iPython%20Gist/MakePassword.png)

- Up next we're going to create a directory in our home folder called "certificates". In this folder we're going to save a self signed SSL certificate. Complete the questions as best you can.

![Create SSL Certificate](https://dl.dropbox.com/u/550268/iPython%20Gist/CreateSSLCert.png)

- We're going to need the name of the certifcate and the absoulte path for the notebook configuration file.

![Cert](https://dl.dropbox.com/u/550268/iPython%20Gist/SSLCertPath.png)

- Last, but not least, it's time to modify our ipython_notebook_config.py file.
- Cruise over to ~/.ipython/profile_nbserver/ (or whatever you decided to call your profile) and open up the ipython_notebook_config.py file.

![Notebook Config](https://dl.dropbox.com/u/550268/iPython%20Gist/ModifyConfig.png)

- You can either go through the config file and uncomment each of these one by one, or just use the [iPython HTML Notebook](http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html) docs and copy the code to the top of the file like I did. You'll need to change "certfile" and "password" to the values you just got from the previous steps. Change the "port" to 8888.
- Save!

## Launching you iPython Notebook
- From anywhere run the following: `$ ipython notebook inline --profile=nbserver`

![Server up](https://dl.dropbox.com/u/550268/iPython%20Gist/ServerUp.png)

- If you're successful you should have output like the above! **WATCH OUT:** make sure your server is running at "all ip addresses on your system" rather than just 127.0.0.1 (or something like that). You WILL have a bad time.

## Logging in to your Notebook from the Browser
- In order to log in via the browser we need the Public DNS for our sever. Cruise over to your AWS Console and select your instance from the Instances page. Under description you should find this:

![Public DNS](https://dl.dropbox.com/u/550268/iPython%20Gist/AmazonPublicDNS.png)

- Using your public DNS go to your fav browser and type:
    https://your-Instance's-public-DNS:8888

- If successfull you'll get a warning about the self signed certificate. It's ok! Click _Continue_.

![Chrome Warning](https://dl.dropbox.com/u/550268/iPython%20Gist/ChromeSSLWarning.png)
![Safari Warning](https://dl.dropbox.com/u/550268/iPython%20Gist/SafariSSLWarning.png)

- You're in! Enter your password, create a notebook, and start doing...stuff!

![In!](https://dl.dropbox.com/u/550268/iPython%20Gist/in%21.png)

## What next?
A few things:
- Why not associate an [Elastic IP](http://aws.amazon.com/articles/1346) to your instance(s)? Now you've got a static ip no matter what kind of instance you start.
- Use your Elastic IP and set up forwarding from a domain that you own. Instead of having a random IP address (albeit static) you can access your notebook via a memorable domain name. E.g. https://theres_always_money_in_the_banana_stand.com/notebook
- Create a Snapshot of your AMI. Now you can use this AMI on ANY instance type you like.
- Create an EBS volume to store all your data/work. Use your newly created Python AMI and run a massive instance for a few hours. Your setup Python setup will be the same but your hardware will be pretty beefy.
- Dive in to the .ipython folder in your home directory (or where you installed it) and modify your ipython_configuration.py. There are lots of options for configuring what packages are imported and what they are called at startup.

## Resources and Further Reading
1. [iPython HTML Notebok Documentation](http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html)
2. [iPython on EC2 Screen Cast](http://www.youtube.com/watch?v=HaS4NXxL5Qc)
4. [EC2 Screencast on YouTube](http://www.youtube.com/watch?v=HaS4NXxL5Qc)
4. [Contiuum.io Anaconda Download](http://continuum.io/downloads.html)
5. [Anaconda Package Index](http://docs.continuum.io/anaconda/1.4/pkgs.html)
6. [iPython Tutorial -> Magic Functions](http://ipython.org/ipython-doc/dev/interactive/tutorial.html)