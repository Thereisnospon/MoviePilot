import re
import traceback
from pathlib import Path
from typing import Tuple, Optional, List, Union, Dict
from urllib.parse import unquote

from app.core.config import settings
from app.core.context import Context, TorrentInfo, MediaInfo
from app.core.metainfo import MetaInfo
from app.db.systemconfig_oper import SystemConfigOper
from app.log import logger
from app.utils.http import RequestUtils
from app.schemas.types import MediaType, SystemConfigKey
from app.utils.singleton import Singleton
from app.utils.string import StringUtils


class S_itesHelper(metaclass=Singleton):

    def __init__(self):
        self.site_all = {
            "mteam": {"private": 2, "id": 1, "domain": "kp.m-team.cc", "name": "mteam"}
        }
        self.auth_level = 9999

    def check_user(self):
        return "success", "hello"

    def get_indexer(self, domain):
        return self.site_all["mteam"]

    def get_indexers(self):
        return self.site_all.values()
