# Locust Stress tests 

## Introduction

[Locust](https://github.com/locustio/locust) is an open source load testing tool. From the original repo:
> Locust is an easy-to-use, distributed, user load testing tool. It is intended for load-testing web sites (or other systems) and figuring out how many concurrent users a system can handle. 

## Prerequisites

- Make sure you have python 3.7+ installed
- Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)

## Installation

- Create a virtual env with `mkvirtualenv locust-stress-tests`
- Install requirements with `pip install -r requirements`

## Running stress tests

#### Web interface:
```
locust --host=http://localhost:8001
```

![image](https://user-images.githubusercontent.com/9268203/67151850-4f442300-f2a2-11e9-9f1c-587bee1003a5.png)

![image](https://user-images.githubusercontent.com/9268203/67151626-0a6abd00-f29f-11e9-85fd-5204b9951c53.png)


#### Command line

```
locust --host=http://localhost:8001 --clients 100 --hatch-rate 2 --no-web
```
![image](https://user-images.githubusercontent.com/9268203/67151646-5e75a180-f29f-11e9-891e-ccdb2061cc92.png)

