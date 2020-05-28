# 创建文件夹
# `mkdir -r /root/hzj/tmp/project/fastapi/`
work_dir="/root/hzj/tmp/project/fastapi/"

echo $work_dir

# 这里要判断一下有无python3.7的

# 安装Python3的包
yum install zlib-devel \ 
    bzip2-devel openssl-devel ncurses-devel \
    sqlite-devel readline-devel tk-devel gcc \ 
    make libffi-devel -y 

# 安装pip 
yum install epel-release -y
yum install python-pip

# 安装wget
yum install wget

# 安装3.7源码包
`mkdir -r /root/hzj/tmp/PreparePackage/`
cd /root/hzj/tmp/PreparePackage/
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

# 解压缩包
https://segmentfault.com/a/1190000015628625
