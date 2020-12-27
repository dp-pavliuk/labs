# Lab 4
## Хід роботи

1. Виконав команди: 
```
sudo docker -v
sudo docker -h
sudo docker run docker/whalesay cowsay Docker is fun
```
2. Виконав команди:
```
sudo docker pull python:3.8-slim
sudo docker images
sudo docker inspect python:3.8-slim
```
3. Скопіював та редагував файл 
*Dockerfile*
4. Створив репозиторій на DockerHub
5. Виконав команди:
```
sudo docker build -t dp-pavliuk/devops_course:django .
sudo docker images 
sudo docker push dp-pavliuk/devops_course:django
```
Посилання на [репозиторій](https://https://hub.docker.com/u/pavliukdanylo)

Посилання на [імейдж](https://hub.docker.com/layers/pavliukdanylo/devops_course/django/images/sha256-40c95d98f8fd87b6451b5797db2ba5b2f6bff1c3fc493bc15e2605b379da7320?context=explore)

6. Виконав команду
```
sudo docker run -it --rm -p 8000:8000 pavliukdanylo/devops_course:django
```
7. Створив файл *Dockerfile.monitoring*
8. Виконав білд імейджа:
```
sudo docker build -t pavliukdanylo/devops_course:monitoring .
sudo docker images
sudo docker push pavliukdanylo/devops_course:monitoring 
```
Посилання на [імейдж](https://hub.docker.com/layers/pavliukdanylo/devops_course/monitoring/images/sha256-2233844df39a01f2b02ced6ef4b8f579c0c83929248f7f5af4a0d401b87ccd5a?context=explore&tab=layers)

9. Запустив імейдж моніторингу в окремому терміналі після чого витягнув з контейнеру server.log