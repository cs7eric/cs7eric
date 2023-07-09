import requests
from bs4 import BeautifulSoup




# 将 55-60 替换为 <br>
# 读取现有的 README.md 文件
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()



# 将指定行替换为 <br>
# new_lines = lines[:start_index_new] + ["\n"] + lines[end_index_new+1:]

# 将新的 README.md 文件内容写回到文件中
# with open("README.md", "w", encoding="utf-8") as f:
#     f.writelines(new_lines)
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
end_index = 61

# 将新的文章添加到指定位置
new_lines = lines[:start_index] + article_list + lines[end_index+1:]

# 在 61-66 行插入空白占位符
# new_lines.insert(62, "\n")
# new_lines.insert(63, "\n")
# new_lines.insert(64, "\n")
# new_lines.insert(65, "\n")
# new_lines.insert(66, "\n")
# new_lines.insert(67, "\n")


with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(new_lines)