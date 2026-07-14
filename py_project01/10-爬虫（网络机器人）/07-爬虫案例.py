# 👉 案例：
# 获取 TMDB 高分电影榜单(Top100)数据，并保存在 CSV 文件中。
# 数据包括：电影名、年份、上映时间、类型、时长、评分、语言、导演、作者、主演、S1ogan、简介。
# https://www.themoviedb.org/movie/top-rated
#
# 实现步骤：
#   1、明确 TMDB 网站的抓取规则：https://www.themoviedb.org/robots.txt
#   2、查看网页的结构，拆解具体的操作步骤，按如下步骤开发：
#     - 获取高分电影列表数据。https://www.themoviedb.org/movie/top-rated
#     - 遍历电影列表，获取每一部电影的详细信息，并提取电影的数据信息。电影列表中的a标签 href="/movie/278-the-shawshank-redemption" 存放电影详情地址。
#     - 将提取的数据保存到 CSV 文件中。

import requests
import os
import csv
from lxml import html

# 定义常量
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated" # 高分电影榜单的数据页面（第一页）


def get_movie_info(url):
  """
  获取电影详情数据
  """
  pass

def save_to_csv(data):
  """
  保存电影数据到 CSV 文件中
  """
  pass

def main():
  """
  主函数，定义核心逻辑：
  """
  # 1、发送请求，获取高分电影榜单数据
  response = requests.get(TMDB_TOP_URL, timeout=60)
  html_content = response.text
  
  # 2、解析数据，获取电影列表
  doc_tree = html.fromstring(html_content)
  movie_list = doc_tree.xpath('//*[@id="page_1"]/div/div/div')

  # 3、遍历电影列表，获取电影详情
  all_movies = []
  for movie in movie_list:
    movie_urls = movie.xpath('./div/div/a/@href')
    if movie_urls:
      # 电影详情 url
      movie_info_url = TMDB_BASE_URL + movie_urls[0]
      print("电影详情 url：", movie_info_url)
      
      # 发送请求，获取电影详情数据
      movie_data = get_movie_info(movie_info_url)
      all_movies.append(movie_data)
    
  # 4、保存电影数据到 CSV 文件中
  if all_movies:
    save_to_csv(all_movies)

if __name__ == '__main__':
  main()