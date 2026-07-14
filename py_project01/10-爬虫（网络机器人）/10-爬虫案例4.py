# 👉 案例：
# 获取 TMDB 高分电影榜单(Top100)数据，并保存在 CSV 文件中。
# 数据包括：电影名、年份、上映时间、类型、时长、评分、语言、导演、作者、主演、S1ogan、简介。
# https://www.themoviedb.org/movie/top-rated
#
# 实现功能：
#   - 获取电影高分网页的分页数据；
#   - 浏览器中检查网页得知：TMDB_TOP_URL 永远获取的是第一页数据，分页是通过调用 TMDB_PAGE_URL 接口实现的。


import requests
from lxml import html
import os
import csv

# 定义常量
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"   # 高分电影榜单的数据页面（第一页）
TMDB_PAGE_URL = "https://www.themoviedb.org/discover/movie/items"  # 高分电影榜单的分页数据页面（第二页、第三页...）
MOVIE_LIST_FILE = "movie_page5.csv"

def get_movie_info(url):
  """
  获取电影详情数据
  """
  # 🎃 1、发送请求，获取电影详情数据
  response = requests.get(url + '?language=zh-CN', timeout=60)
  print(f"---------- 发送请求: {url}，获取电影详情")
  html_content = response.text
  
  # 🎃 2、解析数据，获取电影详情
  doc_tree = html.fromstring(html_content)
  # 电影名
  movie_names = doc_tree.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')
  # print("电影名：", movie_names)
  # 年份
  movie_years = doc_tree.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()')
  # print("年份：", movie_years)
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
  movie_slogans = doc_tree.xpath('//*[@id="original_header"]/div[2]/section/div[3]/h3[@class]/text()')
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
    "时长": movie_durations[0].strip() if movie_durations else "",
    "评分": movie_ratings[0].strip() if movie_ratings else "",
    "语言": movie_languages[0].strip() if movie_languages else "",
    "导演": ", ".join(movie_directors) if movie_directors else "",
    "作者": ", ".join(movie_writers) if movie_writers else "",
    "slogan": movie_slogans[0].strip() if movie_slogans else "",
    "简介": movie_overviews[0].strip() if movie_overviews else ""
  }
  # print("电影详情数据：", movie_data)
  # 返回电影详情数据
  return movie_data


def get_file_path(fileName, subDir="csv_data"):
  """
  获取当前脚本的绝对路径下的文件路径
  """
  # 步骤1. 获取当前脚本的绝对路径
  script_dir = os.path.dirname(os.path.abspath(__file__))
  # 步骤2. 定义目标文件夹路径
  csv_dir = os.path.join(script_dir, subDir)
  # 步骤3. 如果文件夹不存在，则自动创建
  if not os.path.exists(csv_dir):
      os.makedirs(csv_dir)
  # 步骤4. 拼接完整的文件路径
  relative_path = os.path.join(csv_dir, fileName)
  return relative_path

def save_to_csv(data):
  """
  保存电影数据到 CSV 文件中
  """
  file_path = get_file_path(MOVIE_LIST_FILE)
  with open(file_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言', '导演', '作者', 'slogan', '简介'])
    writer.writeheader()
    writer.writerows(data)


def main():
  """
  主函数，定义核心逻辑：
  """

  # 前5页的电影数据，保存在 all_movies 列表中
  all_movies = []

  # 循环获取电影列表，第1页到第5页
  for page_num in range(1, 6):

    # 1、发送请求，获取高分电影榜单数据
    if page_num == 1:
      response = requests.get(TMDB_TOP_URL, timeout=60)
    else:
      # 🎃 发送 post 请求，获取第二页之后的数据
      response = requests.post(TMDB_PAGE_URL, 
                               data=f"air_date.gte=&air_date.lte=&certification=&certification_country=US&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-01-14&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=US&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400", 
                               timeout=60)
    print(f"************************* 发送请求，获取第{page_num}页的电影数据")
    html_content = response.text
    
    # 2、解析数据，获取电影列表
    doc_tree = html.fromstring(html_content)
    # 🎃 解析数据时，列表 div 的 id 是根据 page_num 动态生成的，所以需要动态拼接 xpath
    movie_list = doc_tree.xpath(f'//*[@id="page_{page_num}"]/div/div/div')

    # 3、遍历电影列表，获取电影详情
    
    for movie in movie_list:
      movie_urls = movie.xpath('./div/div/a/@href')
      if movie_urls:
        # 电影详情 url
        movie_info_url = TMDB_BASE_URL + movie_urls[0]
        # print("电影详情 url：", movie_info_url)

        # 发送请求，获取电影详情数据
        movie_data = get_movie_info(movie_info_url)
        all_movies.append(movie_data)
      
  # 4、保存电影数据到 CSV 文件中
  print("<-------------------> 获取到电影数据，开始保存到 csv 文件 <------------------->")
  if all_movies:
    save_to_csv(all_movies)

if __name__ == '__main__':
  main()