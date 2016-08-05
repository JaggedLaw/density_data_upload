import boto3

s3client = boto3.client('s3')

s3client.upload_file("message.txt", "test-charissa", "word1-word2-word3")

s3resource = boto3.resource('s3')

data = open('message.txt', 'r')
s3resource.Bucket('test-charissa').put_object(Key='word4-word5-word6', Body=data)

# for bucket in s3resource.buckets.all():
    # print(bucket.name)
