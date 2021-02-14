# nonebot_plugin_mqtt
[![pypi](https://img.shields.io/pypi/v/nonebot-plugin-mqtt.svg)](https://pypi.org/project/nonebot-plugin-mqtt/)
![implementation](https://img.shields.io/pypi/implementation/nonebot-plugin-mqtt)
![wheel](https://img.shields.io/pypi/wheel/nonebot-plugin-mqtt)
![python](https://img.shields.io/pypi/pyversions/nonebot-plugin-mqtt)
[![license](https://img.shields.io/github/license/synodriver/nonebot_plugin_mqtt.svg)](https://raw.githubusercontent.com/synodriver/nonebot_plugin_mqtt/main/LICENSE)

- 基于[nonebot2](https://github.com/nonebot/nonebot2) 和 [gmqtt](https://github.com/wialon/gmqtt)

## 功能

- 将nonebot接入mqtt网络

## 开始使用

使用 pip

- 通过 pip 从 [PyPI](https://pypi.org/project/nonebot_plugin_mqtt/) 安装

``` {.sourceCode .bash}
pip install nonebot-plugin-mqtt
```

- 在 nonebot2 项目中设置 load_plugin()

``` {.sourceCode .python}
nonebot.load_plugin('nonebot_plugin_mqtt')
```

- 参照下文在 nonebot2 项目的环境文件 .env.\* 中添加配置项

## 配置项
``` {.sourceCode .python}
MQTT_TOPIC   # mqtt订阅topic
MQTT_CLIENT_ID # mqtt订阅clientid
MQTT_HOST # mqtt broker地址
MQTT_PORT # mqtt broker端口

MQTT_USER # mqtt 可选验证项
MQTT_PASSWORD
```

## 导出给其他插件

```{.sourceCode .python}
export = nonebot.require("nonebot_plugin_mqtt")
export.mqtt_client.publish(topic,msg)
export.mqtt_client.subscribe(TOPIC, qos=1)

# 自定义回调
export.mqtt_client.on_message = on_message
export.mqtt_client.on_connect = on_connect
```

## 特别感谢

- [Mrs4s / go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
- [nonebot / nonebot2](https://github.com/nonebot/nonebot2)

## 优化建议

可以来抓更多网站的接口or汇报bug or pr 
![](https://i.pixiv.cat/img-original/img/2019/09/01/05/00/42/76563606_p0.png "呐呐呐,来pr的话~就给大哥哥透噢")