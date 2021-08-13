selenium模块的基本使用

问题：selenium模块和爬虫之间具有怎样的关联
    - 便捷的获取网站中动态加载的数据
    - 便捷的实现模拟登录

什么是selenium模块？
    - 基于浏览器自动化的一个模块

selenium使用流程：
    - 环境安装：pip install selenium
    - 下载一个浏览器的驱动程序(Chrome)
        - 下载路径：http://chromedriver.storage.googleapis.com/index.html
        - 驱动程序和浏览器的映射关系：https://blog.csdn.net/huilan_same/article/details/51896672
    - 实例化一个浏览器对象
    - 编写基于浏览器自动化的操作代码