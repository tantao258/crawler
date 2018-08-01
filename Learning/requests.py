import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


# methmod = "GET"
# if methmod == "POST":
#     response = requests.post('http://182.61.21.98/home/', data={"username": "tantao25wwwwwwwwwwww8",
#                                                          "email": "910806",
#                                                          "gender": "男",
#                                                          })
# else:
#     response = requests.get("https://www.zhihu.com", headers=headers)
#     if response.status_code == requests.codes.ok:
#         print("访问成功")

# print(response.text)
# print(type(response))
# print(response.status_code)
# print(response.cookies)
# print(response.content)
# print(response.content.decode("utf-8"))
# print(response.json())
# print(json.loads(response.text))

# POST 上传图片
# files = {"files": open("1.jpg", "rb")}
# response = requests.post("http://httpbin.org/post", files=files)
# if response.status_code == requests.codes.ok:
#     print("访问成功")
# print(response.text)

# print(response.cookies)
# for key, value in response.cookies.items():
#     print(key+"="+value)

# 会话维持
# cookie的一个作用就是可以用于模拟登陆，做会话维持
# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456")
# response = s.get("http://httpbin.org/cookies")
# print(response.text)

# 证书验证
# urllib3.disable_warnings()
# response = requests.get("https://www.12306.cn", verify=False)
# print(response.status_code)

# 代理设置
# proxies = {
#     "http": "http://127.0.0.1:9999",
#     "https": "http://127.0.0.1:8888"
# }
# response = requests.get("https://www.baidu.com", proxies=proxies)
# print(response.text)

# # 认证设置：如果碰到需要认证的网站可以通过requests.auth模块实现
# from requests.auth import HTTPBasicAuth
# response = requests.get("http://120.27.34.24:9001/",auth=HTTPBasicAuth("user", "123"))
# print(response.status_code)


# ==================================正则表达式   http://www.cnblogs.com/zhaof/p/6925674.html======================
# re.match()   尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配的话，match（）就会返回None
# re.search  扫描整个字符串返回第一个成功匹配的结果
# re.findall   搜索字符串，以列表的形式返回全部能匹配的子串
# re.sub       替换字符串中每一个匹配的子串后返回替换后的字符串

# ------------------------------------------------------------------------------------
# re.match()   尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配的话，match（）就会返回None
# 语法格式: re.match(pattern,string,flags=0)
# 1.最常规的匹配
# string = "hello 123 4567 World_This is a regex Demo"
# result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', string)
# print(result)
# print(result.group())  # result.group()获取匹配的结果
# print(result.span())   # result.span()获去匹配字符串的长度范围

# 2.泛匹配
# string = "hello 123 4567 World_This is a regex Demo"
# result = re.match("^hello.*Demo$", string)
# print(result)
# print(result.group())
# print(result.span())

# 3.匹配目标
# 如果为了匹配字符串中具体的目标，则需要通过（）括起来,如果正则表达式中有括号，则re.group(1)获取的就是第一个括号中匹配的结果

# string = "hello 1234567 World_This is a regex Demo"
# result = re.match('^hello\s(\d+)\sWorld.*(Demo)$', string)
# print(result)
# print(result.group())
# print(result.span())
#
# print(result.group(0))
# print(result.span(0))
#
# print(result.group(1))
# print(result.span(1))
# print(result.group(2))
# print(result.span(2))

# 4.贪婪匹配
# 从结果中可以看出只匹配到了7，并没有匹配到1234567，出现这种情况的原因是前面的.* 给匹配掉了，
# .*在这里会尽可能的匹配多的内容，也就是我们所说的贪婪匹配，
# string = "hello 1234567 World_This is a regex Demo"
# result = re.match(pattern='^hello.*(\d+).*Demo$', string=string)
# print(result)
# print(result.group())
# print(result.span())
# print(result.group(1))
# print(result.span(1))
# 如果我们想要匹配到1234567则需要将正则表达式改为：
# string = "hello 1234567 World_This is a regex Demo"
# result = re.match('^he.*?(\d+).*Demo', string)
# print(result)
# print(result.group())
# print(result.span())
# print(result.group(1))
# print(result.span(1))

# 5.匹配模式
# 很多时候匹配的内容是存在换行的问题的，这个时候的就需要用到匹配模式re.S来匹配换行的内容
# string = """hello 123456 world_this
# my name is zhaofan
# """
# result = re.match('^he.*?(\d+).*?zhaofan$', string, re.S)
# print(result)
# print(result.group())
# print(result.group(1))

# 6.转义
# 当我们要匹配的内容中存在特殊字符的时候，就需要用到转移符号\
# string = "price is $5.00"
# result = re.match(pattern='^price is (\$*)5\.00$', string=string)
# print(result)
# print(result.group())
# print(result.group(1))

# 总结: 尽量使用泛匹配，使用括号得到匹配目标，尽量使用非贪婪模式，有换行符就用re.S
#       强调re.match是从字符串的起始位置匹配一个模式

# ------------------------------------------------------------------------------------
# re.search  扫描整个字符串返回第一个成功匹配的结果
# string = "extra things hello 123455 world_this is a Re Extra things"
# result = re.search("hello.*?(\d+).*?Re", string)
# print(result)
# print(result.group())
# print(result.group(1))
# 注意：所以为了匹配方便，我们会更多的用search，不用match,match必须匹配头部，所以很多时候不是特别方便

# html = """<div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>
#         </li>
#         <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#         <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#         <li data-view="5">
#             <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
#         </li>
#     </ul>
# </div>"""
#
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(result)
# print(result.groups())
# print(result.group(1))
# print(result.group(2))

# -------------------------------------------------------------------------------------
# re.findall   搜索字符串，以列表的形式返回全部能匹配的子串
# 例子1
# html = '''<div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>
#         </li>
#         <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#         <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#         <li data-view="5">
#             <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
#         </li>
#     </ul>
# </div>'''
#
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)
# print(type(results))
# for result in results:
#     print(result)
#     print(result[0], result[1], result[2])

# 例子2
# html = '''<div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>
#         </li>
#         <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#         <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#         <li data-view="5">
#             <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
#         </li>
#     </ul>
# </div>'''
#
# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
# print(results)
# for result in results:
#     print(result[1])

# -------------------------------------------------------------------------
# re.sub    替换字符串中每一个匹配的子串后返回替换后的字符串
# re.sub(正则表达式，替换成的字符串，原字符串)
# string = "Extra things hello 123455 World_this is a regex Demo extra things"
# string = re.sub('\d+\s', '', string)
# print(string)

# 在替换字符的时候，还想获取我们匹配的字符串，然后在后面添加一些内容，可以通过下面方式实现：
# string = "Extra things hello 123455 World_this is a regex Demo extra things"
# string = re.sub('(\d+)', r'\1 7890', string)
# print(string)
# output: Extra things hello 123455 7890 World_this is a regex Demo extra things
# 这里需要注意的一个问题是\1是获取第一个匹配的结果，为了防止转义字符的问题，我们需要在前面加上r

# -------------------------------------------------------------
# re.compile   将正则表达式编译成正则表达式对象，方便复用该正则表达式
# content = """hello 12345 world_this
# 123 fan
# """
# pattern = re.compile("hello.*fan", re.S)
# result = re.match(pattern, content)
# print(result)
# print(result.group())

# 正则综合应用
response = requests.get('https://book.douban.com/')
if response.status_code == requests.codes.ok:
    print("访问成功")
else:
    print("访问失败")
content = response.text
print(content)
results = re.findall('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',content, re.S)
print(results)
for result in results:
    url, name, author, date = result
    author = re.sub('\s', '', author)
    date = re.sub('\s', '', date)
    print(url, name, author, date)





