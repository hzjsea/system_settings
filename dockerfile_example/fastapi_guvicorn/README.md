
# 做个笔记
直接在容器里面起一个python的文件，无非就是在最原始的镜像上搭建了一个Python的环境，可以运行
![2020-04-27-17-50-56](http://img.noback.top/2020-04-27-17-50-56.png)

这里有很多版本的python 也就是python的环境+linux最小的系统

## 
```bash
WORKDIR /root/code
# 如果root下面没有这个code的工作目录，直接定义workdir也会创建这个code的文件夹
```
