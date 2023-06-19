from nonebot.plugin import PluginMetadata

from .config import Config
from .mqtt import *


__plugin_meta__ = PluginMetadata(
    name="MQTT",
    description="Nonebot2 MQTT 插件",
    usage="",
    type="library",
    homepage="https://github.com/synodriver/nonebot_plugin_mqtt",
    config=Config,
    supported_adapters=None,
)
