import boto3
no_of_vm = int(input("Please Enter the number of VMs you want to deploy between 1 to 3:"))
ec2client = boto3.clinet('ec2',region_name='ap-south-1')
sg= ''
subnets=[]
userdata=  '''#!/bin/bash
# Your user data script here
'''
for i in range(no_of_vm):
  create_ec2_instances = ec2client.run_instances(
  ImageId="",
  MinCount=1,
  MaxCount=1,
  InstacneType="t2.micro",
  KeyValue="",
  SubnetId=subnets[i],
  UserData=userdata,
  SecurityGroupIds=[
      sg,
   ],
TagSpecifications=[
   {
     'ResourceType' : 'instance',
                       'Tags': [
          {
               'Key' : 'Name',
               'Value' : 'RKE-MASTER-'+str(i+1)
           },
           {
                'Key' : 'Env',
                'Value' : 'Development',
           },
         ]
      },
   ]
  )