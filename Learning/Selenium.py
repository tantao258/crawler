"""
selenium 是一套完整的web应用程序测试系统
elenium可以模拟真实浏览器
Selenium所有的api文档：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
"""
from selenium import webdriver

# 一、基本使用
# python写爬虫的时候，主要用的是selenium的Webdriver

# help(webdriver)
# 支持的浏览器
# android(package)
# blackberry(package)
# chrome(package)
# common(package)
# edge(package)
# firefox(package)
# ie(package)
# opera(package)
# phantomjs(package)
# remote(package)
# safari(package)
# support(package)
# webkitgtk(package)

# # 声明浏览器
# browser = webdriver.Chrome()
# # 访问页面
# browser.get("http://www.baidu.com")
# print(browser.page_source)
# # 关闭浏览器
# browser.close()

# 查找元素
# 单个元素查找
# browser = webdriver.Chrome()
# browser.get("http://www.taobao.com")
# input_first = browser.find_element_by_id("q")
# input_second = browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# # 通过三种不同的方式去获取响应的元素，第一种是通过id的方式，第二个中是CSS选择器，第三种是xpath选择器，结果都是相同的。
# print(input_first)
# print(input_second)
# print(input_third)
# browser.close()

# 这里列举一下常用的查找元素方法：
# find_element_by_name
# find_element_by_id
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector

# 下面这种方式是比较通用的一种方式：
# from selenium.webdriver.common.by import By
# browser = webdriver.Chrome()
# browser.get("http://www.taobao.com")
# input_first = browser.find_element(By.ID,"q")
# print(input_first)
# browser.close()

# 多个元素查找
# browser = webdriver.Chrome()
# browser.get("http://www.taobao.com")
# lis = browser.find_elements_by_css_selector('.service-bd li')
# # 或者 lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
# print(lis)
# browser.close()


# 元素交互
# import time
# browser = webdriver.Chrome()
# browser.get("http://www.taobao.com")
# input_str = browser.find_element_by_id('q')
# input_str.send_keys("ipad")
# time.sleep(1)
# input_str.clear()
# input_str.send_keys("MakBook pro")
# button = browser.find_element_by_class_name('btn-search')
# button.click()

# 交互动作
# from selenium.webdriver import ActionChains
# browser = webdriver.Chrome()
# browser.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# 执行JavaScript
# 这是一个非常有用的方法，这里就可以直接调用js方法来实现一些操作，
# 下面的例子是通过登录知乎然后通过js翻到页面底部，并弹框提示
# browser = webdriver.Chrome()
# browser.get("http://www.zhihu.com/explore")
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

# 获取元素属性  get_attribute('class')
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))

# 获取文本值 text
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)

# 获取ID，位置，标签名
# id
# location
# tag_name
# size

# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

# Frame
# 在很多网页中都是有Frame标签，所以我们爬取数据的时候就涉及到切入到frame中以及切出来的问题，通过下面的例子演示
# 这里常用的是switch_to.from()和switch_to.parent_frame()

# 浏览器的前进和后退
    # back()
    # forward()
# import time
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://http://docs.python-requests.org/zh_CN/latest/user/quickstart.html')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()


# cookie操作
# get_cookies()
# delete_all_cookes()
# add_cookie()

# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'zhaofan'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

# 选项卡管理
# 通过执行js命令实现新开选项卡window.open()
# 不同的选项卡是存在列表里browser.window_handles
# 通过browser.window_handles[0]就可以操作第一个选项卡
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')