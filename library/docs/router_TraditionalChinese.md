# router 使用說明文件

## 概述
`router` 是一個簡單的靜態類別，用於管理瀏覽器的導航操作。該類別提供了兩個方法：`pushUrl` 和 `back`，分別用於導航到新的 URL 和返回上一頁或替換當前頁面。

## 方法說明

### 1. 導航到新 URL
```javascript
router.pushUrl(url);
```
**作用**: 將瀏覽器導航到指定的 URL。
**參數**:
- `url`: 字串類型，目標 URL 地址。

### 2. 返回上一頁或替換當前頁面
```javascript
router.back(url);
```
**作用**: 如果沒有提供 URL，則返回瀏覽器歷史記錄中的上一頁；如果提供了 URL，則用指定的 URL 替換當前頁面。
**參數**:
- `url`: 字串類型，可選參數，目標 URL 地址。如果不提供，則預設執行後退操作。

## 示例程式碼

以下是一個簡單的示例，演示如何使用 `router` 進行基本的導航操作：

```javascript
// 導航到一個新的 URL
router.pushUrl("https://www.example.com");

// 返回上一頁
router.back();

// 用指定的 URL 替換當前頁面
router.back("https://www.another-example.com");
```

通過上述步驟，您可以方便地在瀏覽器中進行頁面導航和替換操作。

## 注意事項
- 確保提供的 URL 是有效的，並且遵循同源策略（Same-Origin Policy）以避免跨域問題。
- 在某些情況下，瀏覽器的歷史記錄可能不足以支持後退操作（例如，直接打開的單頁應用），此時調用 `router.back()` 可能不會產生預期的效果。
