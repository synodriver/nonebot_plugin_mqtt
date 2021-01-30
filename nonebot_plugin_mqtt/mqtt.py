# -*- coding: utf-8 -*-
from gmqtt import Client as MQTTClient
import nonebot

from nonebot.log import logger

driver = nonebot.get_driver()
config = driver.config


async def on_connect(client, flags, rc, properties):
    client.subscribe(config.mqtt_topic, qos=0)
    logger.info("connected")


async def on_message(client, topic, payload, qos, properties):
    logger.info('RECV MSG:', payload)


async def on_disconnect(client, packet, exc=None):
    logger.info('Disconnected')


async def on_subscribe(client, mid, qos, properties):
    logger.info('SUBSCRIBED')


@driver.on_startup
async def connect_and_subscribe():
    client = MQTTClient(config.mqtt_client_id)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe
    if config.mqtt_user:
        client.set_auth_credentials(config.mqtt_user, config.mqtt_password)
    await client.connect(config.mqtt_host, config.mqtt_port)
    nonebot.require("nonebot_plugin_mqtt").mqtt_client = client


@driver.on_shutdown()
async def disconnect():
    await nonebot.require("nonebot_plugin_mqtt").mqtt_client.disconnect()
