# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:59:48 2019

@author: orhun
"""

import boto3


awskeyfile = open("awskeys.txt","r")  #reads the AWS credentials from a file named awskeys 

awskeys = awskeyfile.read()

awskeysarray = awskeys.split('=')

awsaccessarray1 = awskeysarray[1].split('\n')
awsaccessarray2 = awskeysarray[2].split('\n')
awsaccessarray3 = awskeysarray[3].split('\n')

awsaccesskey = awsaccessarray1[0]
awssecretkey = awsaccessarray2[0]
awstoken = (awsaccessarray3[0] + "=")


awskeyfile.close()

file = open("cloudhw3.txt","w") #creates a text file locally to store the user's name
        
        
name = input ("Please Write Name: ") #prompts the user for his/her name
surname = input ("Please Write Surname: " ) #prompts the user for his/her name
print("\n")
       
        
file.writelines(name + ("\n")) 
file.writelines(surname)

file.close()

#reads the AWS credentials from a file named awskeys 
s3 = boto3.resource('s3',aws_access_key_id= awsaccesskey, 
                  aws_secret_access_key= awssecretkey,
                  aws_session_token= awstoken)

for bucket in s3.buckets.all():
    print("Bucket Name: ", bucket.name)
    
#uploads it to Amazon S3 
data = open('cloudhw3.txt','rb')
s3.Bucket('orhunvural').put_object(Key='cloudhw3.txt',Body=data) #upload



bucket = s3.Bucket('orhunvural')

for obj in bucket.objects.all():
    key = obj.key
    body = obj.get()['Body'].read()
    
print("File Content: ", body) #reads the file back and displays the name from the file 

print("File Name: ", key) #reads the file back and displays the name from the file 

obj.delete()

print("\n" + key + " successfully was deleted") #deletes the file from Amazon S3 storage.












