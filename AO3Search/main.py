# -*- encoding: utf-8 -*-
'''
     ██╗██╗   ██╗██╗   ██╗███╗   ██╗██╗  ██╗ ██████╗ 
     ██║╚██╗ ██╔╝██║   ██║████╗  ██║██║ ██╔╝██╔═══██╗
     ██║ ╚████╔╝ ██║   ██║██╔██╗ ██║█████╔╝ ██║   ██║
██   ██║  ╚██╔╝  ██║   ██║██║╚██╗██║██╔═██╗ ██║   ██║
╚█████╔╝   ██║   ╚██████╔╝██║ ╚████║██║  ██╗╚██████╔╝
 ╚════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ 
                                                     
    Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    https://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import re
import requests
import random
import OlivOS
import AO3Search  # type: ignore
from AO3Search.util import (  # type: ignore
    base_url,
    group_lists,
    get_random_items,
    is_string_endwith,
    map_remove_html_tags,
    settings,
)


class Event(object):
    def private_message(plugin_event, Proc):
        unity_reply(plugin_event, Proc)

    def group_message(plugin_event, Proc):
        unity_reply(plugin_event, Proc)


def unity_reply(plugin_event, Proc):
    def proc(url):
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to request {url}.")
            plugin_event.reply(f"Failed to request {url}.")
            return

        title_pattern = re.compile(
            r'<h4 class="heading">.*?<a href=".*?">(.*?)</a>.*?</h4>', re.S
        )
        
        author_pattern = re.compile(
            r'<a rel="author" href="/users/.*?>(.*?)</a>', re.S
        )
        
        content_pattern = re.compile(
            r'<blockquote class="userstuff summary">\s*<p>(.*?)</p>', re.S
        )
        link_pattern = re.compile(
            r'<h4 class="heading">\s*<a href="(.*?)">', re.S
        )

        bookmarks = group_lists(
            map_remove_html_tags(title_pattern.findall(response.text)),
            map_remove_html_tags([f"by {author}" for author in author_pattern.findall(
                response.text)]),
            map_remove_html_tags(content_pattern.findall(response.text)),
            map_remove_html_tags([f"{base_url}{link}" for link in link_pattern.findall(
                response.text)]),
        )

        result = get_random_items(bookmarks)
        plugin_event.reply("\n".join(result))
        
    help_doc = """\
AO3Search help
这是一个基于镜像站"nightalk.cc"随机推文的AO3插件

指令(大小写不敏感)
来篇海维文[-h|-help|-E|-Explicit|-M|-Mature]
or 来篇海维黄文

-h|-help //获取该帮助信息
-E|-Explicit //设置返回Explicit分级内容
-M|-Mature //设置返回Mature分级内容
"""
    if plugin_event.data.message.startswith("来篇海维文"):
        url = f"{base_url}{settings[0]}"
        if is_string_endwith(plugin_event.data.message, "-M", "-Mature"):
            url = f"{base_url}{settings[1]}"
        if is_string_endwith(plugin_event.data.message, "-E", "-Explicit"):
            url = f"{base_url}{settings[2]}"
        if is_string_endwith(plugin_event.data.message, "-H", "-Help"):
            plugin_event.reply(help_doc)
            return
        proc(url=url)
    elif plugin_event.data.message == "来篇海维黄文":
        url = f"{base_url}{settings[random.randint(1, 2)]}"
        proc(url=url)