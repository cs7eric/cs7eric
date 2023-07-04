import requests
from bs4 import BeautifulSoup

# 博客网站的 URL
url = "https://blog.cccs7.icu/"

# 发送 GET 请求获取 HTML 页面
response = requests.get(url)

# 使用 BeautifulSoup 解析 HTML 页面
soup = BeautifulSoup(response.text, "html.parser")

# 获取最新的7篇文章的标题和链接
articles = soup.find_all("h3", class_="home-article-title")[:7]
article_list = [f"- [{article.text.strip()}]({url + article.find('a', href=True)['href']})\n" for article in articles]

# 读取现有的README.md文件
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到要添加新文章的位置
start_index = 55
end_index = 60

# 将新的文章添加到指定位置
new_lines = lines[:start_index] + article_list + lines[end_index:]
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(new_lines)