#!/bin/bash


# 查看版本
cat /etc/redhat-release

# 安装supervisor
# 这里其实要先查看有没有安装python3 pip3 
# 再看有没有安装supervisor 
# 如果都没有 在继续安装
pip install supervisor

# 创建文件夹
mkdir /etc/supervisor/
echo_supervisord_conf > /etc/supervisor/supervisord.conf
mkdir /etc/supervisor.d/

# 安装python httpserver
pip install httpserver



# 移动配置文件夹
cat ./supervisord.conf > /etc/supervisor/supervisord.conf
cp ./*.conf /etc/supervisor.d/


# 启动程序
supervisorctl -c /etc/supervisor/supervisord.conf
