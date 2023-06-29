FROM python:3.10.3

COPY . /gsapi
WORKDIR /gsapi
#安装pip包
RUN pip install -r requirements.txt
#监听6745端口
EXPOSE 6745

ENTRYPOINT ["python"]
CMD ["app.py"]