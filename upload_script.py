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
    new_upload = False
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            directory_name = os.path.join(root, dir) + "/"
            directory_name = directory_name.replace("../", "")
            root_folder_name = directory_name.split('/')
            root_folder_name = root_folder_name[0]
            if root_folder_name not in existing_folders:
                new_upload = True
                s3client.put_object(
                    Bucket='test-charissa',
                    Body='',
                    Key=directory_name
                )
        # if new_upload:
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
            new_upload = False

# find names of directories in current path
folders = s3client.list_objects(Bucket='test-charissa')

existing_folders = set([])

for thing in s3resource.Bucket('test-charissa').objects.all():
    location = thing.key.split('/')
    location = location[0]
    existing_folders.add(location)

print existing_folders



# find names of directories on s3
# if name in current path does not exist on s3, then upload that directory
uploadDirectory(path, bucketname)
