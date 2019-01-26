# snapshotalyzer-30000
Demo project to manage AWS snapshots

## About
This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses the configuration file created by the AWS CLI. e.g.

`aws configure --profile <username>`

##Running
`pipenv run python shotty/shotty.py <command> <subcommand> <--project=PROJECT>"`

*command* is instances, volumes, or snapshots
*subcommand* depends on command
*project* is optional
`
