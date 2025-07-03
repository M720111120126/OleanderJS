# 标准库 使用文档

---

## 推送模块

推送模块包括一个`push`类

### 类 `Push`
#### 方法
- **`askForNotificationPermission()`**
  - 异步方法，请求浏览器的通知权限。
  - 返回值：`Promise<boolean>`，如果用户授予了权限则返回 `true`，否则返回 `false`。
  
- **`requestPermission()`**
  - 别名方法，调用 `askForNotificationPermission()`。
  - 返回值：`Promise<boolean>`，如果用户授予了权限则返回 `true`，否则返回 `false`。
  
- **`hasPermission()`**
  - 检查是否已有权限或请求权限。
  - 返回值：`Promise<boolean>`，如果有权限则返回 `true`，否则返回 `false`。
  
- **`_showNotification(text)`**
  - 内部方法，显示带有指定文本的通知。
  - 参数：
    - `text` (`string`)：通知的内容。
  
- **`showNotification(text)`**
  - 调用 `_showNotification(text)` 来显示通知。
  - 参数：
    - `text` (`string`)：通知的内容。
  
- **`closeNotification()`**
  - 关闭当前显示的通知。

---


