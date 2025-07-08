# com.oleander.os.jms 使用文档

`com.oleander.os.jms`提供了一个叫做`OleanderFileSystem`的类

## 概述
`jms` 是一个简单的静态类，用于管理JZH统一用户的用户数据。该类提供了获取的方法。

## 方法说明

### 1. 请求获取用户数据
```javascript
jms.request();
```
**作用**: 请求从JMS读取JZH统一用户的用户数据

### 2. 获取状态
```javascript
jms.state();
```
**作用**: 查看获取的状态
**返回值**: 
* 0：未开始获取
* 1：等待用户授权
* 2：已经获取

### 3. 获取用户数据
```javascript
jms.get();
```
**作用**: 从浏览器读取JZH统一用户的用户数据
**返回值**: 一个Object，包含了`name`和`email`两个值

通过上述步骤，您可以方便地在应用中集成账号。
