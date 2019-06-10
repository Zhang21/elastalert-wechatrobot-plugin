#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
# Description: Send alert using HuaWeiCloud/ALiYun/TencentCloud SMS service
# Date: 2019-06-03
# License: MIT
"""

import requests
from elastalert.alerts import Alerter, BasicMatchString
from elatalert.util import elastalert_logger, EAException


# Send alert using HuwWeiCloud SMS service
class HuaWeiCloudAlerter(Alerter):
    """
    self.required_options:
    This is a set containing names of configuration options that must be present. ElastAlert will not instantiate the alert if any are missing.
    frozenset()不可变，而set()是可变的。
    """
    required_options = frozenset(['hw_url', 'hw_ak', 'hw_sk', 'hw_sender', 'hw_template_id', 'hw_signature', 'receiver'])

    def __init__(self, *args):
        super(HuaWeiCloudAlerter, self).__init__(*args)
        # 从规则配置文件(xxx.yaml)中读取相应的配置
        self.hw_url = self.rule.get('hw_url')
        self.hw_ak = self.rule.get('hw_ak')
        self.hw_sk = self.rule.get('hw_sk')
        self.hw_sender = self.rule.get('hw_sender')
        self.hw_template_id = self.rule.get('hw_template_id')
        self.hw_signature = self.rule.get('hw_signature')
        self.reciver = self.rule.get('receiver')
        # optional
        self.hw_statusballback = self.rule.get('hw_statusballback', '')
        self.hw_template_param = self.rule.get('hw_template_param', '')

    def create_default_title(self, matches):
        subject = 'ElastAlert: %s' % (self.rule['name'])
        return subject

    """
    The alerter class will be instantiated when ElastAlert starts, and be periodically passed matches through the alert method.
    ElastAlert will call this function to send an alert.
    matches is a list of dictionary objects with information about the match.
    You can get a nice string representation of the match by calling self.rule['type'].get_match_str(match, self.rule).
    If this method raises an exception, it will be caught by ElastAlert and the alert will be marked as unsent and saved for later.
    """
    def alert(self, matches):
        body = self.create_alert_body(matches)
        # 华为云短信服务暂不支持这样传递body
        '''
        # 所以不能直接使用body，要间接使用
        # 取单独的值，放入对应短信模板的变量值中。但我觉得没有钉钉这样好用了
        # 如
        sms_level = self.matches.get['level']
        sms_log_message = self.matches.get['log_message']
        # 然后将取的值传递到发送短信的程序中
        '''
        elastalert_logger.info('Sent HuaWeiCloud SMS notifacation.')

    """
    # ElastAlert also writes back info about the alert into Elasticsearch that it obtains through get_info.
    This function is called to get information about the alert to save back to Elasticsearch.
    It should return a dictionary, which is uploaded directly to Elasticsearch,
    and should contain useful information about the alert such as the type, recipients, parameters, etc.
    """
    def get_info(self):
        return {
            'type': 'HWCloudSmsAlerter'
        }


# Send alert using ALiYun SMS service
class ALiYunAlerter(Alerter):
    required_options = frozenset(['ali_ak', 'ali_sk', 'ali_xxx'])

    def __init__(self, *args):
        super(HuaWeiCloudAlerter, self).__init__(*args)
        self.ali_ak = self.rule.get('ali_ak')
        self.ali_sk = self.rule.get('ali_sk')
        self.ali_xxx = self.rule.get('ali_xxx')
        self.reciver = self.rule.get('receiver')

    def create_default_title(self, matches):
        subject = 'ElastAlert: %s' % (self.rule['name'])
        return subject

    def alert(self, matches):
        body = self.create_alert_body(matches)
        # Aliyun短信发送方式
        # xxxxxx
        elastalert_logger.info('Sent ALiYun SMS notifacation.')

    def get_info(self):
        return {
            'type': 'AliYunSmsAlerter'
        }


# Send alert using TencentCloud SMS service
class TencentCloudAlerter(Alerter):
    required_options = frozenset(['tencent_ak', 'tencent_sk', 'tencent_xxx'])

    def __init__(self, *args):
        super(HuaWeiCloudAlerter, self).__init__(*args)
        self.tencent_ak = self.rule.get('tencent_ak')
        self.tencent_sk = self.rule.get('tencent_sk')
        self.tencent_xxx = self.rule.get('tencent_xxx')
        self.reciver = self.rule.get('receiver')

    def create_default_title(self, matches):
        subject = 'ElastAlert: %s' % (self.rule['name'])
        return subject

    def alert(self, matches):
        body = self.create_alert_body(matches)
        # 腾讯云短信服务使用方法
        # xxxxx
        elastalert_logger.info('Sent TencentCloud SMS notifacation.')

    def get_info(self):
        return {
            'type': 'TencentCloudSmsAlerter'
        }
