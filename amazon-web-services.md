## Amazon Web Services
***
- [Simple Storage Services](#simple-storage-services)

**DISCLAIMER:** These are my notes after attending the course [[**AWS for Developers: S3**]()].

## Simple Storage Services
***

First we need to install the `AWS CLI` if not already installed using `sudo apt install awscli`.

I encountered few issues on my ubuntu environment and I solved it doing this:

    py -m pip install --upgrade requests
    py -m pip install requests "urllib3<2"
  
Setting up `Amazon CLI`.

    1) Goto Amazon S3 console.
    2) Click your "username" on the top right corner and select `Security credentials`.
    3) In the `Access Keys` section, click the button named, `Create access key`. 
    
You should now have `Access key` and `Secret access key`.

Now open up a terminal and do the followings:

    $ aws configure
    AWS Access Key ID [None]:
    AWS Secret Access Key [None]:
    Default region name [None]:
    Default output format [None]:

