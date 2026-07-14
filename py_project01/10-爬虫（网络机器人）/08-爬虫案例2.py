# 👉 案例：
# 获取 TMDB 高分电影榜单(Top100)数据，并保存在 CSV 文件中。
# 数据包括：电影名、年份、上映时间、类型、时长、评分、语言、导演、作者、主演、S1ogan、简介。
# https://www.themoviedb.org/movie/top-rated
#
# 实现功能：
#   - 使用 requests 库 发送请求获取电影详情数据；
#   - 使用 lxml 库基于 Xpath 语法解析 html 数据；
#   - 组装并返回电影详情数据；

import requests
from lxml import html
import os
import csv

# 定义常量
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"


def get_movie_info(url):
  """
  获取电影详情数据
  """
  # 🎃 1、发送请求，获取电影详情数据
  response = requests.get(url + '?language=zh-CN', timeout=60)
  html_content = response.text
  
  # 🎃 2、解析数据，获取电影详情
  doc_tree = html.fromstring(html_content)
  # 电影名
  movie_names = doc_tree.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')
  # print("电影名：", movie_names)
  # 年份
  movie_years = doc_tree.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()')
  print("年份：", movie_years)
  # 上映时间
  movie_release_dates = doc_tree.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[2]/text()')
  # print("上映时间：", movie_release_dates)
  # 类型
  movie_genres = doc_tree.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[3]/a/text()')
  # print("类型：", movie_genres)
  # 时长
  movie_durations = doc_tree.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[4]/text()')
  # print("时长：", movie_durations)
  # 评分
  movie_ratings = doc_tree.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')
  # print("评分：", movie_ratings)
  # 语言
  movie_languages = doc_tree.xpath('//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')
  # print("语言：", movie_languages)
  # 导演
  movie_directors = doc_tree.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()')
  # print("导演：", movie_directors)
  # 作者
  movie_writers = doc_tree.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()')
  # print("作者：", movie_writers)
  # slogan
  movie_slogans = doc_tree.xpath('//*[@id="original_header"]/div[2]/section/div[3]/h3[1]/text()')
  # print("slogan：", movie_slogans)
  # 简介
  movie_overviews = doc_tree.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')
  # print("简介：", movie_overviews)

  # 🎃 3、组装并返回电影详情数据
  movie_data = {
    "电影名": movie_names[0].strip() if movie_names else "",
    "年份": movie_years[0].strip() if movie_years else "",
    "上映时间": movie_release_dates[0].strip() if movie_release_dates else "",
    "类型": ", ".join(movie_genres) if movie_genres else "", # ⚠️ 有多个类型，用逗号分隔
    "时长": movie_durations[0].split(" ")[1] if movie_durations else "",
    "评分": movie_ratings[0].strip() if movie_ratings else "",
    "语言": movie_languages[0].strip() if movie_languages else "",
    "导演": ", ".join(movie_directors) if movie_directors else "",
    "作者": ", ".join(movie_writers) if movie_writers else "",
    "slogan": movie_slogans[0].strip() if movie_slogans else "",
    "简介": movie_overviews[0].strip() if movie_overviews else ""
  }
  print("电影详情数据：", movie_data)
  # 返回电影详情数据
  return movie_data


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