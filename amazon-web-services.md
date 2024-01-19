## Amazon Web Services
***
- [Amazon S3](#amazon-s3)

**DISCLAIMER:** These are my notes after attending the course [[**AWS for Developers: S3**]()].

## Amazon S3
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
    Default region name [None]: eu-west-2
    Default output format [None]: json

Let's test the installation.

    $ aws ec3 describe-regions

You should see JSON dump on the console.

Time to create our first bucket.

    $ aws s3 mb s3://manwar-bucket-20240118-1
    make_bucket: manwar-bucket-20240118-1

Go to `AWS S3 Console` on the web and check if you have the bucket with the name as above.

Let's try delete the bucket as below:

    $ aws s3 rb s3://manwar-bucket-20240118-1
    remove_bucket: manwar-bucket-20240118-1

Go the console and referesh the page, there shouldn't be any bucket there.

To continue with rest of `CLI` commands we would need a bucket, so let's create the bucket again.

    $ aws s3 mb s3://manwar-bucket-20240118-1
    make_bucket: manwar-bucket-20240118-1

Refresh the console page and you should have a bucket now.

We would create a folder `s3` and in that we would then create two text files as below:

    $ mkdir s3
    $ cd s3
    $ echo "This is file 1." > file1.txt
    $ echo "This is file 2." > file2.txt
    
Now we will copy a local text to the bucket we created earlier.

    $ aws s3 cp file1.txt s3://manwar-bucket-20240118-1 
    upload: ./file1.txt to s3://manwar-bucket-20240118-1/file1.txt

Check the console, the file `file1.txt` should appear in the bucket.

Let's try moving file `file2.txt` to the bucket.

    $ ls
    file1.txt file2.txt
    $ aws s3 mv file2.txt s3://manwar-bucket-20240118-1 
    move: ./file2.txt to s3://manwar-bucket-20240118-1/file2.txt
    $ ls
    file1.txt

The file `file2.txt` should now be listed in the bucket on the console if you refresh.

What if I want to move file `file2.txt` from the bucket to local folder.

    $ aws s3 mv s3://manwar-bucket-20240118-1/file2.txt ./
    move: s3://manwar-bucket-20240118-1/file2.txt to ./file2.txt
    $ ls
    file1.txt file2.txt

We have 2 files again but on the console, there is just one file `file1.txt` listed.

Let's try to delete the file `file2.txt` from the bucket.

    $ aws s3 rm s3://manwar-bucket-20240118-1/file2.txt
    delete: s3://manwar-bucket-20240118-1/file2.txt

Now we have just one file `file2.txt` in the bucket on console.

Let's try to copy file to bucket with new name.

    $ aws s3 cp file1.txt s3://manwar-bucket-20240118-1/file1mod.txt
    upload: ./file1.txt to s3://manwar-bucket-20240118-1/file1mod.txt

As per the console, we now have two files, `file1.txt` and `file1mod.txt` in the bucket.

Let's empty the bucket in the console.

Now try to list the files in remote bucket.

    $ aws s3 ls s3://manwar-bucket-20240118-1
    $

We got nothing back i.e. the bucket is empty.

Let's try to sync the local directory to S3 bucket.

    $ ls
    file1.txt file2.txt
    $ aws s3 sync ./ s3://manwar-bucket-20240118-1
    upload: ./file1.txt to s3://manwar-bucket-20240118-1/file1.txt
    upload: ./file2.txt to s3://manwar-bucket-20240118-1/file2.txt

Let's create another file `file3.txt` locally.

    $ echo "This is file 3." > file3.txt

Now if sync the local folder again, it would only upload the new file as the other two files didn't change.

    $ ls
    file1.txt file2.txt file3.txt
    $ aws s3 sync ./ s3://manwar-bucket-20240118-1
    upload: ./file3.txt to s3://manwar-bucket-20240118-1/file3.txt

Let's edit the file `file3.txt` and add one more line to it

    $ echo "Adding new line to file 3." >> file3.txt

Let's sync the local folder again.

    $ aws s3 sync ./ s3://manwar-bucket-20240118-1
    upload: ./file3.txt to s3://manwar-bucket-20240118-1/file3.txt

If we now refresh the bucket on the console, we should see three files listed there.

Let's delete the file `file3.txt` from the bucket on the console.

Now let's sync from the bucket to the local folder.

    $ aws s3 sync s3://manwar-bucket-20240118-1 ./
    $ ls
    file1.txt file2.txt file3.txt
    
Nothing happened but why?

Because we have everything that the bucket has, it is safe.

Hoeever if we want sync to delete the file locally then we have explicitly mention it.

    $ aws s3 sync s3://manwar-bucket-20240118-1 ./ --delete
    delete: ./file3.txt
    $ ls
    file1.txt file2.txt

We now play with two buckets. For that we would now create one more bucket as below:

    $ aws s3 mb s3://manwar-bucket-20240119-1
    make_bucket: manwar-bucket-20240119-1
    
You should now see two buckets on the `S3` console.

Let's try to sync files from the bucket `manwar-bucket-20240118-1` to the bucket `manwar-bucket-20240119-1`.

    $ aws s3 sync s3://manwar-bucket-20240118-1 s3://manwar-bucket-20240119-1
    copy: s3://manwar-bucket-20240118-1/file1.txt to s3://manwar-bucket-20240119-1/file1.txt
    copy: s3://manwar-bucket-20240118-1/file2.txt to s3://manwar-bucket-20240119-1/file2.txt

If you now check both the buckets on the console, they should both have two files.

Let's try to empty the bucket `manwar-bucket-20240119-1`.

    $ aws s3 rm s3://manwar-bucket-20240119-1 --recursive
    delete: s3://manwar-bucket-20240119-1/file1.txt
    delete: s3://manwar-bucket-20240119-1/file2.txt
    
    
    
