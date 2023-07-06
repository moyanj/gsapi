#!/bin/bash

# 拉取镜像
docker pull moyanjdc/gsapi:1.1.0

# 创建宿主机目录
mkdir -p /opt/gsapi/log
mkdir -p /opt/gsapi/cache

# 运行容器
docker run -d --name GSAPI -p 6475:8080 \
-v /opt/gsapi/log:/gsapi/log \
-v /opt/gsapi/cache:/gsapi/cache \
moyanjdc/gsapi:1.1.0

# 检查容器状态
container_status=$(docker ps -f "name=GSAPI" --format "{{.Status}}")

if [[ $container_status == *"Up"* ]]; then
    echo "容器已成功运行！"
else
    echo "容器运行失败，请检查日志信息。"
fi