scrapy框架

- 什么是框架？
    - 就是一个继承了很多功能，并且具有很强通用性的一个模板。
    
- 如何学习框架？
    - 专门学习框架封装的各种功能的详细用法。

- 什么是scrapy
    - 爬虫中封装好的一个*明星*框架。功能：高性能的持久化存储，异步的数据下载，高性能的数据解析，
        分布式
      
- scrapy框架的基本使用
    - 0.环境的安装：
        
    - 1.创建一个工程：scrapy startproject xxxPro
    - 2.cd xxxPro  
    - 3.在spiders子目录中创建一个爬虫文件
        - scrapy genspider spiderName www.xxx.cn
    - 4.执行工程：
        - scrapy crawl spiderName
        - scrapy crawl spiderName --nolog (可只看输出结果，但程序出错会有问题)
  