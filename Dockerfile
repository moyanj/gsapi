#使用python的slim镜像以减少大小
FROM python:3.10.3-slim
# 复制代码
COPY . /gsapi
#设置工作目录
WORKDIR /gsapi
#为python设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#新建用户并安装依赖包
RUN pip install --no-cache-dir --upgrade -r requirements.txt && adduser -u 1145 --disabled-password --gecos "" gsapi && chown -R gsapi /gsapi
#设置程序运行用户
USER gsapi
RUN flask init
#开放6475端口
EXPOSE 6475
#设置启动命令
CMD ["gunicorn","app:app"]