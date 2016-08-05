import boto3
import os

s3client = boto3.client('s3')

s3client.upload_file("message.txt", "test-charissa", "word1-word2-word3")

s3resource = boto3.resource('s3')

data = open('message.txt', 'r')
s3resource.Bucket('test-charissa').put_object(Key='word4-word5-word6', Body=data)

path = "../boop-bawp-beep"
bucketname = "test-charissa"

def uploadDirectory(path, bucketname):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            directory_name = os.path.join(root, dir) + "/"
            directory_name = directory_name.replace("../", "")
            s3client.put_object(
                Bucket='test-charissa',
                Body='',
                Key=directory_name
            )
        for file in files:
            filename = os.path.join(file)
            file_with_path = os.path.join(root, file)

            data = open(file_with_path, 'r')
            new_directory = file_with_path.replace("../", "")
            s3client.put_object(
                Bucket='test-charissa',
                Body=data,
                Key=new_directory
            )


# find names of directories in current path
s3client.list_objects(Bucket='test-charissa')
# find names of directories on s3
# if name in current path does not exist on s3, then upload that directory
uploadDirectory(path, bucketname)
