# nonebot_plugin_mqtt

[![pypi](https://img.shields.io/pypi/v/nonebot-plugin-mqtt.svg)](https://pypi.org/project/nonebot-plugin-mqtt/)
![python](https://img.shields.io/pypi/pyversions/nonebot-plugin-mqtt)
[![license](https://img.shields.io/github/license/synodriver/nonebot_plugin_mqtt.svg)](https://raw.githubusercontent.com/synodriver/nonebot_plugin_mqtt/main/LICENSE)

- 基于[nonebot2](https://github.com/nonebot/nonebot2) 和 [gmqtt](https://github.com/wialon/gmqtt)

## 功能

- 将 nonebot 接入 mqtt 网络

## 开始使用

- 使用 nb-cli 安装

```bash
nb plugin install nonebot-plugin-mqtt
```

- 参照下文在 nonebot2 项目的环境文件 .env.\* 中添加配置项

## 配置项

```text
MQTT_TOPIC          # MQTT 订阅 Topic
MQTT_CLIENT_ID      # MQTT 订阅 Client ID
MQTT_HOST           # MQTT Broker 地址
MQTT_PORT           # MQTT Broker 端口

MQTT_USER           # MQTT 可选验证项
MQTT_PASSWORD
```

## 在其他插件中使用

```python
from nonebot import require

require("nonebot_plugin_mqtt")
from nonebot_plugin_mqtt import mqtt_client

mqtt_client.publish(topic, payload=payload, qos=0, retain=False)
mqtt_client.subscribe(topic, qos=1)

# 自定义回调
mqtt_client.on_message = on_message
mqtt_client.on_connect = on_connect
```

## 特别感谢

- [Mrs4s/go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
- [nonebot/nonebot2](https://github.com/nonebot/nonebot2)

## 优化建议

可以来抓更多网站的接口 or 汇报 bug or pr
![](https://i.pixiv.cat/img-original/img/2019/09/01/05/00/42/76563606_p0.png "呐呐呐,来pr的话~就给大哥哥透噢")
