FROM python:3.12-slim
USER 1000
WORKDIR /tmp
ADD myapp.py /tmp/myapp.py
ENTRYPOINT ["python"]
CMD ["myapp.py"]
