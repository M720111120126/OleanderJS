# router 使用文档

## 概述
`router` 是一个简单的静态类，用于管理浏览器的导航操作。该类提供了两个方法：`pushUrl` 和 `back`，分别用于导航到新的 URL 和返回上一页或替换当前页面。

## 方法说明

### 1. 导航到新 URL
```javascript
router.pushUrl(url);
```
**作用**: 将浏览器导航到指定的 URL。
**参数**:
- `url`: 字符串类型，目标 URL 地址。

### 2. 返回上一页或替换当前页面
```javascript
router.back(url);
```
**作用**: 如果没有提供 URL，则返回浏览器历史记录中的上一页；如果提供了 URL，则用指定的 URL 替换当前页面。
**参数**:
- `url`: 字符串类型，可选参数，目标 URL 地址。如果不提供，则默认执行后退操作。

## 示例代码

以下是一个简单的示例，演示如何使用 `router` 进行基本的导航操作：

```javascript
// 导航到一个新的 URL
router.pushUrl("https://www.example.com");

// 返回上一页
router.back();

// 用指定的 URL 替换当前页面
router.back("https://www.another-example.com");
```

通过上述步骤，您可以方便地在浏览器中进行页面导航和替换操作。

## 注意事项
- 确保提供的 URL 是有效的，并且遵循同源策略（Same-Origin Policy）以避免跨域问题。
- 在某些情况下，浏览器的历史记录可能不足以支持后退操作（例如，直接打开的单页应用），此时调用 `router.back()` 可能不会产生预期的效果。