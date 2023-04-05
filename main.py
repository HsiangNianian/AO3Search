import re
import random
import requests
import OlivOS


class Event(object):
    def private_message(plugin_event, Proc):
        unity_reply(plugin_event, Proc)
        # pass

    def group_message(plugin_event, Proc):
        unity_reply(plugin_event, Proc)
        # pass


def unity_reply(plugin_event, Proc):
    base_url = "https://nightalk.cc"
    url = f"{base_url}/users/woaicharen/pseuds/woaicharen/bookmarks"
    response = requests.get(url)

    if response.status_code == 200:  # 请求成功

        # 匹配标题
        title_pattern = re.compile(
            r'<h4 class="heading">.*?<a href=".*?">(.*?)</a>.*?</h4>', re.S)
        title_match = title_pattern.findall(response.text)

        # 匹配内容
        content_pattern = re.compile(
            r'<blockquote class="userstuff summary">\s*<p>(.*?)</p>', re.S)
        content_match = content_pattern.findall(response.text)

        # 提取链接
        link_pattern = re.compile(
            r'<h4 class="heading">\s*<a href="(.*?)">', re.S)
        link_match = link_pattern.findall(response.text)

        def remove_html_tags(text):
            # 去掉 <br> 标签
            text = re.sub(r'<br/?>', '', text)
            # 去掉其他标签及其内容
            text = re.sub(r'<.*?>', '', text)
            return text

        def map_remove_html_tags(lst):
            for i in range(len(lst)):
                lst[i] = remove_html_tags(lst[i])
            return lst

        def group_lists(*lists):
            # 将所有列表按照交叉排列合并
            merged_list = [item for sublist in zip(*lists) for item in sublist]
            # 将元素分组为三个一组
            grouped_list = [merged_list[i:i+3]
                            for i in range(0, len(merged_list), 3)]
            return grouped_list

        def get_random_items(data):
            # 随机选择一个子列表
            sublist = random.choice(data)
            # 取该子列表中的前三个元素
            items = sublist[:3]
            return items

        bookmarks = group_lists(map_remove_html_tags(title_match), map_remove_html_tags(
            content_match), map_remove_html_tags(link_match))

        result = get_random_items(bookmarks)
        plugin_event.reply('\n'.join(result))

    else:
        print(f"Failed to request {url}.")
        plugin_event.reply(f"Failed to request {url}.")
