#!/usr/bin/env python
# -*- coding:utf8 -*-
import configparser
from boto3.session import Session
from os.path import expanduser

# This class depends on AWS CLI.
class AwsAuth:
    HOME_DIR = expanduser("~")

    # section ex) default, dev, prod
    def __init__(self, section='default'):
        self.section = section
        self.__sign_in()

    def __set_accounts(self):
        config = configparser.SafeConfigParser()

        # config
        config.read('{0}/.aws/config'.format(self.HOME_DIR))
        region = config.get(self.section, 'region')

        # credentials
        config.read('{0}/.aws/credentials'.format(self.HOME_DIR))
        access_key = config.get(self.section, 'aws_access_key_id')
        secret_key = config.get(self.section, 'aws_secret_access_key')

        self.__region = region
        self.__access_key = access_key
        self.__secret_key = secret_key

    def __create_session(self):
        return Session(
            aws_access_key_id=self.__access_key,
            aws_secret_access_key=self.__secret_key,
            region_name=self.__region
        )

    def __sign_in(self):
        try:
            self.__set_accounts()
            self.__signin_session = self.__create_session()
        except Exception as e:
            raise e

    def session(self, api_name):
        return self.__signin_session.client(api_name)

