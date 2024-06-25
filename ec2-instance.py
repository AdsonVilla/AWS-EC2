import boto3 # type: ignore


def create_ec2_instance():
    
    session = boto3.Session(region_name='us-east-1')  
    
    ec2 = session.resource('ec2')

    instance = ec2.create_instances(
        ImageId='ami-01b799c439fd5516a',  # AMI Linux 2023
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',  # tipo de instância desejado
        KeyName='Chave2AWSEC2',  # nome da sua chave EC2
        IamInstanceProfile={
            'Name': 'Admin-role-for-ec2'
        }
    )

    print("Instância criada com ID:", instance[0].id)

if __name__ == "__main__":
    create_ec2_instance()
