from typing import Optional

from pydantic import BaseSettings


class Config(BaseSettings):
    mqtt_topic: str = "testtopic/#"
    """
    MQTT 订阅 Topic
    """
    mqtt_client_id: str = "nb2_mqtt_client"
    """
    MQTT 订阅 Client ID
    """
    mqtt_host: str = "127.0.0.1"
    """
    MQTT Broker 主机
    """
    mqtt_port: int = 1883
    """
    MQTT Broker 端口
    """
    mqtt_user: Optional[str] = None
    """
    MQTT 验证用户名 可选
    """
    mqtt_password: Optional[str] = None
    """
    MQTT 验证密码 可选
    """

    class Config:
        extra = "ignore"
