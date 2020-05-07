# -*- coding: utf-8 -*-


"""A plugin of ElastAlert for inotify to wechat group robot.

@reference: https://github.com/xuyaoqiang/elastalert-dingtalk-plugin
@wechat_robot: https://work.weixin.qq.com/help?doc_id=13376
@date: 2020-04-30
@author: Zhang
@python: v3.6
@license: MIT
"""


import json
import requests
from elastalert.alerts import Alerter, DateTimeEncoder
from requests.exceptions import RequestException
from elastalert.util import EAException


class WechatRobotAlerter(Alerter):
    """params

    :param wechat_robot_webhook: webhook of wechat group robot.
    :param wechat_robot_msgtype: message type of wechat group robot.
    :param wechat_robot_mentioned_list: mentioned_list of wechat group members.
    """
    required_options = frozenset(['wechat_robot_webhook', 'wechat_robot_msgtype'])

    def __init__(self, rule):
        super(WechatRobotAlerter, self).__init__(rule)
        self.wechat_robot_webhook = self.rule['wechat_robot_webhook']
        self.wechat_robot_msgtype = self.rule.get('wechat_robot_msgtype', 'text')
        self.wechat_robot_mentioned_list = self.rule.get('wechat_robot_mentioned_list', [])

    def format_body(self, body):
        return body.encode('utf8')

    def alert(self, matches):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json;charset=utf-8"
        }
        body = self.create_alert_body(matches)
        payload = {
            "msgtype": self.wechat_robot_msgtype,
            "text": {
                "content": body,
                "mentioned_list": self.wechat_robot_mentioned_list
            }
        }
        try:
            response = requests.post(self.wechat_robot_webhook,
                                     data=json.dumps(payload, cls=DateTimeEncoder),
                                     headers=headers)
            response.raise_for_status()
        except RequestException as e:
            raise EAException("Error request to wechat_robot: {0}".format(str(e)))

    def get_info(self):
        return {
            "type": "wechat_robot",
            "wechat_robot_webhook": self.wechat_robot_webhook
        }
        pass
