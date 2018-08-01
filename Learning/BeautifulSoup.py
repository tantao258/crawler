"""
一个灵活又方便的网页解析库，处理高效，支持多种解析器。
利用它就不用编写正则表达式也能方便的实现网页信息的抓取
https://www.cnblogs.com/zhaof/p/6930955.html
"""

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p["class"])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id='link3'))

# for link in soup.find_all('a'):
#     print(link.get('href'), link.get("id"))
# print(soup.get_text()) # 获取标签中的text

# 基本使用
# soup.标签名 我们就可以获得这个标签的内容
# 这种方式获取标签，如果文档中有多个这样的标签，返回的结果是第一个标签的内容
# print(soup.title)
# print(soup.head)
# print(soup.p)

# 获取名称
# soup.title.name的时候就可以获得该title标签的名称
# 获取属性
# soup.p['name']
# 获取内容
# soup.p.string  # 结果就可以获取第一个p标签的内容
# 嵌套选择
# soup.head.title.string
# 子节点和子孙节点
# -------------------------------------------------------------------------------------
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
# soup = BeautifulSoup(html, 'lxml')
# contents以及children都是获取子节点
# print(soup.p.contents)
# print(soup.p.children)
# for i, child in enumerate(soup.p.children):
#     print(i, child)
# 获取子孙节点可以通过descendants
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)

# soup.a.parent就可以获取父节点的信息
# list(enumerate(soup.a.parents)) #可以获取祖先节点
# soup.a.next_siblings # 获取后面的兄弟节点
# soup.a.previous_siblings # 获取前面的兄弟节点
# soup.a.next_sibling # 获取下一个兄弟标签
# souo.a.previous_sinbling # 获取上一个兄弟标签
# ----------------------------------------------------------------------------------------

# ---------------------------------标准选择器-------------------------------------------------------
# find_all
# find_all(name,attrs,recursive,text,**kwargs)

# -------------------------------------name的用法-----------------------------------
# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# # print(soup.find_all('ul'))
# for ul in soup.find_all('ul'):
#     print(ul.find_all('li'))

# -----------------------------------attrs-----------------------------------
# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'name': 'elements'}))
# attrs可以传入字典的方式来查找标签，但是这里有个特殊的就是class,因为class在python中是特殊的字段，
# 所以如果想要查找class相关的可以更改attrs={'class_':'element'}

# ------------------------------------------text---------------------------------
# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text='Foo'))

# find
# find(name,attrs,recursive,text,**kwargs)
# find返回的匹配结果的第一个元素
#
# 其他一些类似的用法：
# find_parents()返回所有祖先节点，find_parent()返回直接父节点。
# find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。
# find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点。
# find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点
# find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点


# CSS选择器
# 通过select()直接传入CSS选择器就可以完成选择
# 熟悉前端的人对CSS可能更加了解，其实用法也是一样的
# .表示class #表示id
# 标签1，标签2 找到所有的标签1和标签2
# 标签1 标签2 找到标签1内部的所有的标签2
# [attr] 可以通过这种方法找到具有某个属性的所有标签
# [atrr=value] 例子[target=_blank]表示查找所有target=_blank的标签
#
# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.select('.panel .panel-heading'))  # 找到 class=panel标签中 class=panel-heading 的标签
# print("-----------------------------------------")
# print(soup.select('ul li'))              # 找到 ul标签下的li标签
# print("-----------------------------------------")
# print(soup.select('#list-2 .element'))   # 找到 id=list-2标签中 class=element 的标签
# print(soup.select('#list-2 ,.element'))  # 找到 id=list-2标签和 class=element 的标签
# print("-----------------------------------------")
# print(soup.select('ul')[0])

# 获取内容   通过get_text()就可以获取文本内容

# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# for li in soup.select('li'):
#     print(li.get_text())

# 获取标签属性

# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# for ul in soup.select('ul'):
#     print(ul['id'])
#     print(ul["class"])
#
# 推荐使用lxml解析库，必要时使用html.parser
# 标签选择筛选功能弱但是速度快
# 建议使用find()、find_all() 查询匹配单个结果或者多个结果
# 如果对CSS选择器熟悉建议使用select()
# # 记住常用的获取属性和文本值的方法



