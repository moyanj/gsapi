from flask import Blueprint
from var import log
import os
import platform
import secrets
import json
import click
import sqlite3

# 连接到数据库
conn = sqlite3.connect('db/config.db')
cursor = conn.cursor()

bp = Blueprint('cli', __name__, cli_group=None)        
@bp.cli.command('conf')
@click.argument("key")
@click.argument("value")
def conf(key, value):
    cursor.execute('UPDATE config SET value = "{}" WHERE key = "{}";'.format(value,key))
    conn.commit()
    
@bp.cli.command('img')
@click.argument("type")
@click.argument("url")
def img(type, url):
    cursor.execute('INSERT INTO imageRes (type, url) VALUES ("{}", "{}");'.format(type, url))
    conn.commit()