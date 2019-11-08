import boto3
from flask import Flask

id = []
app = Flask(__name__)
ec2 = boto3.client('ec2')
response = ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name',
            'Values': [
                'pending','running',]
            }]
)

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        id.append(instance["InstanceId"])


@app.route('/delete_server')
def remove():
    global response, id
    if len(response["Reservations"]) > 0:
        for x in id:
            ec2.stop_instances(
                InstanceIds=[
                    x,
                ],
                DryRun=False,
                Force=True
)
            ec2.terminate_instances(
                InstanceIds=[
                    x,
                ],
                DryRun=False
            )
        return "Instance deleted."
    else:
        return "No instance to delete."


@app.route('/create_server')
def create():
    global response
    if len(id) == 0:
         return ec2.run_instances(ImageId='ami-0d5d9d301c853a04a',
                                    InstanceType='t2.micro',
                                    KeyName='Linux_Laptop',
                                    MinCount=1,
                                    MaxCount=1)
    else:
        return "Instance already exists."


app.run()
