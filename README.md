# Criando uma instância Amazon EC2 (AWS) via código

Script para subir uma instância EC2 e rodá-la na AWS, através de SDK para Python.

## Tecnologias Utilizadas

- Python
- Boto3: AWS SDK para Python para criar, configurar, e gerenciar serviços AWS
- AWS console
- IAM roles

## Para rodar o projeto

- Inicialmente, foi necessário baixar o lib boto3
```
pip install boto3
```
- Para configurar as credenciais AWS localmente, foi necessário instalar a AWS CLI
```
pip install awscli

```
E configurar as credenciais (Access Key ID, Secret Access Key, região padrão e formato de saída)
```
aws configure
```
- No console da AWS, foi criada uma IAM role para permitir o gerenciamento da instância EC2


## Configurações escolhidas para a instância

- AMI: Linux 2023
- Tipo: t2.micro
- Região: us-east-1 (North Virginia)
