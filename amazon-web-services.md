## Amazon Web Services
***
- [AWS S3 CLI](#aws-s3-cli)
- [AWS SDK for Python](#aws-sdk-for-python)

**DISCLAIMER:** These are my notes after attending the course [[**AWS for Developers: S3**]()].

## AWS S3 CLI
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
    
Finally we will remove the bucket too.

    $ aws s3 rb s3://manwar-bucket-20240119-1
    remove_bucket: manwar-bucket-20240119-1

Presign URLS, gives access to object for a limited time.    

Let's create presign urls giving access to the file `file1.txt` for `30 seconds`.

    $ aws s3 presign s3://manwar-bucket-20240118-1/file1.txt --expires-in 30
    https://manwar-bucket-20240118-1.s3.amazonaws.com/file1.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAU6GDZVJ6J7FOVW55%2F20240119%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240119T004746Z&X-Amz-Expires=30&X-Amz-SignedHeaders=host&X-Amz-Signature=1dda38022e06f7912e0947d8c7649531a5a7431672a1834b402d33afdb56e202

Now copy the url and opens it in a browser, you should see the contents of file `file1.txt`.

Wait for `30 seconds` and try to access it again.

We got the error as expected.

## AWS SDK for Python
*** 

Let's create a folder `pys3` and under that folder create file called `pys3.py`.

    #!/usr/bin/env python3

    """A python script for working with amazon S3."""

    def main():
        """ entry point """

    if __name__ == "__main__":
        main()

Now we want `boto3` which is an `Amazon SDK`. We can install it using command `py -m pip install boto3`.

Let's edit the python file `pys3.py`.

Don't forget to create the download dir `/home/manwar/practice-aws/s3alt`.

    #!/usr/bin/env python3

    """A python script for working with amazon S3."""
    import os
    import boto3
    from botocore.exceptions import ClientError
    
    ACCESS_KEY = 'AWS_ACCESS_KEY_ID'
    SECRET_KEY = 'AWS_SECRET_ACCESS_KEY'
    PRIMARY_BUCKET_NAME = 'manwar-bucket-20240118-1'
    TRANSIENT_BUCKET_NAME = 'manwar-bucket-20240119-1'
    F1 = 'file1.txt'
    F2 = 'file2.txt'
    F3 = 'file3.txt'
    DIR = '/home/manwar/practice-aws/s3'
    DOWN_DIR = '/home/manwar/practice-aws/s3alt'
    REGION = 'eu-west-2'

    def create_bucket(name, s3):
        try:
            s3.create_bucket(
                Bucket=name,
                CreateBucketConfiguration={'LocationConstraint': REGION})
        except ClientError as ce:
            print("ERROR: ", ce)

    def main():
        access = os.getenv(ACCESS_KEY)
        secret = os.getenv(SECRET_KEY)
        s3 = boto3.resource("s3", aws_access_key_id=access, aws_secret_access_key=secret)

        create_bucket(TRANSIENT_BUCKET_NAME, s3)

    if __name__ == "__main__":
        main()

We would need to set two environment keys `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` before we can run the script.

Now run the script like `py pys3.py` should create the bucket. Refresh the S3 console.

We can now delete the newly created bucket from the console.

Let's add function `upload_file()` to the file.

    def upload_file(bucket, directory, file, s3, s3path=None):
        file_path = directory + '/' + file
        remote_path = s3path
        if remote_path is None:
            remote_path = file
        try:
            s3.Bucket(bucket).upload_file(file_path, remote_path)
        except ClientError as ce:
            print("ERROR: ", ce)

Also add function `download_file()` as below:

    def download_file(bucket, directory, local_name, key_name, s3):
        file_path = directory + '/' + local_name
        try:
            s3.Bucket(bucket).download_file(key_name, file_path)
        except ClientError as ce:
            print("ERROR: ", ce)

Finally we will add function `delete_files()` like this:

    def delete_files(bucket, keys, s3):
        objects = []
        for key in keys:
            objects.append({"Key": key})
        try:
            s3.Bucket(bucket).delete_objects(Delete={'Objects': objects})
        except ClientError as ce:
            print("ERROR: ", ce)

Now let's upload the local file to the bucket.

    def main():
        access = os.getenv(ACCESS_KEY)
        secret = os.getenv(SECRET_KEY)
        s3 = boto3.resource("s3", aws_access_key_id=access, aws_secret_access_key=secret)

        upload_file(PRIMARY_BUCKET_NAME, DIR, F1, s3)    
        upload_file(PRIMARY_BUCKET_NAME, DIR, F2, s3)
        upload_file(PRIMARY_BUCKET_NAME, DIR, F3, s3)

After the run, check the console and you should see the three files in the bucket.

Now we will download the file `file3.txt` from the bucket.

    def main():
        access = os.getenv(ACCESS_KEY)
        secret = os.getenv(SECRET_KEY)
        s3 = boto3.resource("s3", aws_access_key_id=access, aws_secret_access_key=secret)

        download_file(PRIMARY_BUCKET_NAME, DOWN_DIR, F3, F3, s3)

After the run, you should check the DOWN_DIR locally and see `file3.txt` in it.

Finally let's delete all three files from the bucket.

    def main():
        access = os.getenv(ACCESS_KEY)
        secret = os.getenv(SECRET_KEY)
        s3 = boto3.resource("s3", aws_access_key_id=access, aws_secret_access_key=secret)

        delete_files(PRIMARY_BUCKET_NAME, [F1, F2, F3], s3)       

After the run, check the console and there shouldn't be any files in the bucket.

Let's add function `list_objects()` like below:

    def list_objects(bucket, s3):
        try:
            response = s3.meta.client.list_objects(Bucket=bucket)
            objects = []
            for content in response['Contents']:
                objects.append(content['Key'])
            print(bucket, 'contains', len(objects), 'files')
            return objects
        except ClientError as ce:
            print("ERROR: ", ce)

We will also add another function `copy_file()` like this:

    def copy_file(source_bucket, destination_bucket, source_key, destination_key, s3):
        try:
            source = {
                'Bucket': source_bucket,
                'Key': source_key
            }
            s3.Bucket(destination_bucket).copy(source, destination_key)
        except ClientError as ce:
            print("ERROR: ", ce)

Let's update function `main()` like below:

    def main():
        access = os.getenv(ACCESS_KEY)
        secret = os.getenv(SECRET_KEY)
        s3 = boto3.resource("s3", aws_access_key_id=access, aws_secret_access_key=secret)

        upload_file(PRIMARY_BUCKET_NAME, DIR, F1, s3)    
        upload_file(PRIMARY_BUCKET_NAME, DIR, F2, s3)
        upload_file(PRIMARY_BUCKET_NAME, DIR, F3, s3)

        create_bucket(TRANSIENT_BUCKET_NAME, s3)
            
        copy_file(PRIMARY_BUCKET_NAME, TRANSIENT_BUCKET_NAME, F2, F2, s3

        list_objects(TRANSIENT_BUCKET_NAME, s3)

We will now add another function `prevent_public_access()` as below:

    def prevent_public_access(bucket, s3):
        try:
            s3.meta.client.put_public_access_block(
                Bucket=bucket,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': True,
                    'IgnorePublicAcls': True,
                    'BlockPublicPolicy': True,
                    'RestrictPublicBuckets': True
                })
        except ClientError as ce:
            print("ERROR: ", ce)

Let's also update the function `create_bucket()` that we created earlier.

    def create_bucket(name, s3, secure=False):
        try:
            s3.create_bucket(
                Bucket=name,
                CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})
            if secure:
                prevent_public_access(name, s3)
        except ClientError as ce:
            print("ERROR: ", ce)

Now we will create a bucket with no public access as below:

    def main():
        access = os.getenv(ACCESS_KEY)
        secret = os.getenv(SECRET_KEY)
        s3 = boto3.resource("s3", aws_access_key_id=access, aws_secret_access_key=secret)

        create_bucket(TRANSIENT_BUCKET_NAME, s3, True)
        
Let's add function `generate_download_link()` like below:

    def generate_download_link(bucket, key, expiration_seconds, s3):
        try:
            response = s3.meta.client.generate_presigned_url('get_object', Params={
                'Bucket': bucket,
                'Key': key
            }, ExpiresIn=expiration_seconds)
            print(response)
        except ClientError as ce:
            print("ERROR: ", ce)

Now we will update function `main()` to generate download link:

    def main():
        access = os.getenv(ACCESS_KEY)
        secret = os.getenv(SECRET_KEY)
        s3 = boto3.resource("s3", aws_access_key_id=access, aws_secret_access_key=secret)

        generate_download_link(PRIMARY_BUCKET_NAME, F3, 30, s3)

Finally add function to delete a bucket.

    def delete_bucket(bucket, s3):
        try:
            s3.Bucket(bucket).delete()
        except ClientError as ce:
            print("ERROR: ", ce)

Now update function `main()` to test the delete bucket function.

    def main():
        access = os.getenv(ACCESS_KEY)
        secret = os.getenv(SECRET_KEY)
        s3 = boto3.resource("s3", aws_access_key_id=access, aws_secret_access_key=secret)

        create_bucket(TRANSIENT_BUCKET_NAME, s3)
        delete_bucket(TRANSIENT_BUCKET_NAME, s3)
