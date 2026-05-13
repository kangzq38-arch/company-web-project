# 使用官方 Nginx 镜像作为底子
FROM nginx:alpine
# 把电脑里这个文件夹的所有文件全部复制到箱子里的网页目录
COPY . /usr/share/nginx/html
# 声明箱子打开 80 号门
EXPOSE 80