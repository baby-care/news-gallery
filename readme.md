
## dependent
 - 依赖插件参考requirements.txt，部分重要资料如下
 
   ```
    http://www.django-rest-framework.org/
    https://django-allauth.readthedocs.io/en/latest/configuration.html
   ```
   
## 开发环境 & 线上环境
 - dev_manager.py  本地开发调试manager
 - online_manager.py 线上环境使用,主要用于同步数据库等管理的操作
 - wsgi, 线上环境的Django App入口
 
 - 本地开发默认使用sqlite, 使用前请先执行migrate同步数据库结构
