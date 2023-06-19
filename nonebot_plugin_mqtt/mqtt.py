from typing import Any, Dict, Tuple
from gmqtt import Client
import nonebot

from nonebot.log import logger
from .config import Config

driver = nonebot.get_driver()
global_config = driver.config
plugin_config = Config(**global_config.dict())


mqtt_client = Client(plugin_config.mqtt_client_id)
"""
MQTT 客户端

- 发布 `mqtt_client.publish(topic, payload=payload, qos=0, retain=False)`
- 订阅 `mqtt_client.subscribe(topic, qos=1)`
- 自定义回调
    - `mqtt_client.on_connect = on_connect`
    - `mqtt_client.on_message = on_message`
    - `mqtt_client.on_disconnect = on_disconnect`
    - `mqtt_client.on_subscribe = on_subscribe`
"""


def on_connect(client: Client, flags: int, rc: int, properties: Dict[str, Any]):
    client.subscribe(plugin_config.mqtt_topic, qos=0)
    logger.info("MQTT Connected")
    detail = {
        "client": client._client_id,
        "flags": flags,
        "rc": rc,
        "properties": properties,
    }
    logger.debug(f"MQTT Connected Detail: {detail}")


def on_message(
    client: Client, topic: str, payload: bytes, qos: int, properties: Dict[str, Any]
):
    logger.info(f"MQTT Received: {payload}")
    detail = {
        "client": client._client_id,
        "topic": topic,
        "payload": payload,
        "qos": qos,
        "properties": properties,
    }
    logger.debug(f"MQTT Received Detail: {detail}")


def on_disconnect(client: Client, packet: bytes, exc=None):
    logger.info("MQTT Disconnected")
    detail = {"client": client._client_id, "packet": packet, "exc": exc}
    logger.debug(f"MQTT Disconnected Detail: {detail}")


def on_subscribe(client: Client, mid: int, qos: Tuple[int], properties: Dict[str, Any]):
    logger.info("MQTT Subscribed")
    detail = {
        "client": client._client_id,
        "mid": mid,
        "qos": qos,
        "properties": properties,
    }
    logger.debug(f"MQTT Subscribed Detail: {detail}")


@driver.on_startup
async def connect_and_subscribe():
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.on_disconnect = on_disconnect
    mqtt_client.on_subscribe = on_subscribe
    if plugin_config.mqtt_user:
        mqtt_client.set_auth_credentials(
            plugin_config.mqtt_user, plugin_config.mqtt_password
        )
    try:
        await mqtt_client.connect(plugin_config.mqtt_host, plugin_config.mqtt_port)
    except Exception as e:
        logger.error(f"MQTT Connect Error: {e}")


@driver.on_shutdown
async def disconnect():
    await mqtt_client.disconnect()
