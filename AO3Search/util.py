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
import random


def is_string_endwith(str1, *substrings):
    tuple_substrings = tuple(sub.lower() for sub in substrings)
    return str1.lower().endswith(tuple_substrings)


def remove_html_tags(text):
    text = re.sub(r'<br/?>', '', text)
    text = re.sub(r'<.*?>', '', text)
    return text


def map_remove_html_tags(lst):
    for i in range(len(lst)):
        lst[i] = remove_html_tags(lst[i])
    return lst


def group_lists(*lists):
    # 将所有列表按照交叉排列合并
    merged_list = [item for sublist in zip(
        *lists) for item in sublist]
    # 将元素分组为三个一组
    grouped_list = [merged_list[i:i+3]
                    for i in range(0, len(merged_list), 3)]
    return grouped_list


def get_random_items(data):
    return random.choice(data)[:3]


base_url = "https://nightalk.cc"
user_id = "woaicharen"
pseud_id = "woaicharen"
settings = [
    f"/users/{user_id}/pseuds/{pseud_id}/bookmarks",
    f"/bookmarks?commit=Sort+and+Filter&bookmark_search%5Bsort_column%5D=created_at&include_bookmark_search%5Brating_ids%5D%5B%5D=12&bookmark_search%5Bother_tag_names%5D=&bookmark_search%5Bother_bookmark_tag_names%5D=&bookmark_search%5Bexcluded_tag_names%5D=&bookmark_search%5Bexcluded_bookmark_tag_names%5D=&bookmark_search%5Bbookmarkable_query%5D=&bookmark_search%5Bbookmark_query%5D=&bookmark_search%5Blanguage_id%5D=&bookmark_search%5Brec%5D=0&bookmark_search%5Bwith_notes%5D=0&pseud_id={pseud_id}&user_id={user_id}",
    f"/bookmarks?commit=Sort+and+Filter&bookmark_search%5Bsort_column%5D=created_at&include_bookmark_search%5Brating_ids%5D%5B%5D=13&bookmark_search%5Bother_tag_names%5D=&bookmark_search%5Bother_bookmark_tag_names%5D=&bookmark_search%5Bexcluded_tag_names%5D=&bookmark_search%5Bexcluded_bookmark_tag_names%5D=&bookmark_search%5Bbookmarkable_query%5D=&bookmark_search%5Bbookmark_query%5D=&bookmark_search%5Blanguage_id%5D=&bookmark_search%5Brec%5D=0&bookmark_search%5Bwith_notes%5D=0&pseud_id={pseud_id}&user_id={user_id}",
]
