# elastalert-sms-plugin

参考:

- ElastAlert Docs: <https://elastalert.readthedocs.io/en/latest/recipes/adding_alerts.html>
- ElastAlert GitHub: <https://github.com/Yelp/elastalert/blob/master/elastalert/alerts.py>
- elastalert微信企业号报警插件: <https://github.com/anjia0532/elastalert-wechat-plugin>
- elastalert钉钉报警插件: <https://github.com/xuyaoqiang/elastalert-dingtalk-plugin>


<br/>

由于云平台短信服务无法直接使用`body`，所以需要手动匹配需要写入短信模板的值。


<br/>
<br/>


## 使用

在规则配置文件中(`xxx.yaml`)配置相关信息：

```
# 需要的配置信息
hw_url: xxx
hw_ak: xxx
hw_sk: xxx
# ali_url: xxx
# tencent_url: xxx

```


<br/>
<br/>


## Docker和K8s

有关容器化的配置请查看cicd目录下的`Dockerfile`, `k8s`文件。根据此文件自行定制和打包镜像。

