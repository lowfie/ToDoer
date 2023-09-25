import os
from dataclasses import dataclass

import yaml
from marshmallow_dataclass import class_schema


@dataclass
class JWTToken:
    access_token_lifetine: int
    refresh_token_lifetine: int


@dataclass
class Api:
    version: str
    secret_key: str


@dataclass
class Config:
    jwt: JWTToken
    api: Api


config_dir = os.path.dirname(__file__)
config_path = os.path.join(config_dir, "config.yaml")

with open(config_path) as f:
    config_data = yaml.safe_load(f)

config: Config = class_schema(Config)().load(config_data)
