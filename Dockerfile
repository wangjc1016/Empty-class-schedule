# 使用轻量级 Python 运行时作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目所有文件到容器中
COPY . .

# 暴露 Flask 运行的端口
EXPOSE 5013

# 设置环境变量（可选）
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# 启动应用（此处直接运行 app.py 中的 app.run()）
CMD ["python", "app.py"]