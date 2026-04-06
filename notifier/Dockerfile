FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY notifier.py ./
EXPOSE 5001
CMD python notifier.py