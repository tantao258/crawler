"""
如果你有前端开发经验的，都应该接触过jQuery,那么PyQuery就是你非常绝佳的选择，
PyQuery 是 Python 仿照 jQuery 的严格实现。语法与 jQuery 几乎完全相同
"""
from pyquery import PyQuery as pq

# 初始化:
# 有三种传入方式：传入字符串，传入url,传入文件

# 字符串初始化
# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
# </div>
# '''
# doc = pq(html)
# print(doc)
# print(doc('li'))        # 获取li标签
# print(doc('.item-0'))   # 获取class=item-0的标签
# print(doc('# xx'))      # 获取id=xx的标签

# URL初始化
# doc = pq(url="http://www.baidu.com", encoding='utf-8')
# print(doc('head'))

# 文件初始化
# 在pq()传入文件参数，这里的文件通常是一个html文件，例如：pq(filename='index.html')

# CSS选择器
# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# doc = pq(html)
# print(doc('#container .list li'))   # 找到id=container的标签下class=list的标签下li标签
# print(type(doc('#container .list li')))
# print("-------------------")
# print(doc('#container .list li')[0].text)  # 获取标签内容

# 查找元素

# 子元素
# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# lis = items.find('li')
# print(type(lis))
# print(lis)
# pyquery找到结果其实还是一个pyquery对象，可以继续查找，
# 上述中的代码中的items.find('li') 则表示查找ul里的所有的li标签
# 通过children可以实现同样的效果,通过.children方法得到的结果也是一个pyquery对象
# li = items.children()
# print(type(li))
# print(li)

# 父元素: parent,parents方法
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
# doc = pq(html)                 # <class 'pyquery.pyquery.PyQuery'>
# items = doc('.list')           # <class 'pyquery.pyquery.PyQuery'>
# # container = items.parent()   # <class 'pyquery.pyquery.PyQuery'>
# # print(container)
# print(items(".item-0"))


# 通过.parents就可以找到祖先节点的内容
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# doc = pq(html)
# items = doc('.list')
# parents = items.parents()
# print(parents)

# 兄弟元素 siblings
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# doc = pq(html)
# li = doc('.list .item-0.active')  # doc('.list .item-0.active') 中的.tem-0和.active是紧挨着的，所以表示是并的关系
# print(li)
# print("========================")
# print(li.siblings())    # 不包含自己
# print("--------------------------")
# print(li.siblings(".item-1.active"))              # 在.siblings()里也是可以通过CSS选择器进行筛选

# 遍历:  单个元素
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
# </div>
# '''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# print("-----------------------")
# lis = doc('li').items()
# for li in lis:
#     print(li)

# 获取信息
# 获取属性
# pyquery对象.attr.属性名
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# doc = pq(html)                     # pyquery对象
# a = doc('.item-0.active a')
# print(a)
# print(a.attr.href)

# 获取文本
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.text())

# 获取html
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# print(li.html())

# DOM操作
# addClass、removeClass
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)

# attr,css
# 同样的我们可以通过attr给标签添加和修改属性，
# 如果之前没有该属性则是添加，如果有则是修改
# 我们也可以通过css添加一些css属性，这个时候，标签的属性里会多一个style属性
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.attr('name', 'link')
# print(li)
# li.css('font-size', '14px')
# print(li)

# remove
# 有时候我们获取文本信息的时候可能并列的会有一些其他标签干扰，
# 这个时候通过remove就可以将无用的或者干扰的标签直接删除，从而方便操作
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
</div>
'''
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print("--------------------")
print(wrap.text())

