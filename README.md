# AwsAuth
A python library to sign in to aws

## System Requirements
- python 2.7.x or 3.x.x
- boto3
- awscli

## Installation

```
$ pip install -r requirements.txt
$ aws configure
```

## Usage
A example to get snapshots

```py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import aws_auth

session = aws_auth.AwsAuth().session('ec2')

filters = [
    {'Name': 'volume-id', 'Values': [volume_id]}
]
snapshots = session.describe_snapshots(
    Filters=filters
)

print(snapshots)
```
