# data 庫使用文檔

data 庫內包括一個用於管理鍵值對（Key-Value）儲存的靜態類別叫 `KVManager`

## 概述
`KVManager` 是一個用於管理鍵值對（Key-Value）儲存的靜態類別，利用瀏覽器的 `localStorage` 來持久化資料。該類別提供了初始化、取得儲存空間、讀取、寫入、刪除和關閉/銷毀儲存空間的方法。

## 方法說明

### 1. 初始化
```javascript
KVManager.init();
```
**作用**: 初始化 `KVManager` 類別，將目前操作的儲存空間名稱清空。
**參數**: 無

### 2. 獲取存儲空間
```javascript
KVManager.getKVStore(KVStorename, encrypt, key);
```
**作用**: 獲取一個存儲空間
**參數**:
- `KVStorename`: 字符串類型，指定存儲空間的名稱，默認爲 `"test"`。
- `encrypt`: 布爾類型，是否啓用加密，默認爲 `false`。如需使用，請先導入 `std` 庫以提供加密支持。
- `key`: 字符串類型，加密密鑰，默認爲空字符串。

### 3. 讀取資料
```javascript
KVManager.get(key);
```
**作用**: 根據鍵名從目前儲存空間中讀取對應的值。
**參數**:
- `key`: 字串類型，要讀取的資料項的鍵名，預設為空字串。
**返回值**: 返回對應鍵名的值，如果不存在則返回 `null`。

### 4. 寫入資料
```javascript
KVManager.put(key, value);
```
**作用**: 將鍵值對保存到目前儲存空間中。
**參數**:
- `key`: 字串類型，要保存的資料項的鍵名，預設為空字串。
- `value`: 要保存的資料項的值，預設為空字串。
**返回值**: 返回成功寫入的值。

### 5. 刪除資料
```javascript
KVManager.delete(key);
```
**作用**: 根據鍵名從目前儲存空間中刪除對應的鍵值對。
**參數**:
- `key`: 字串類型，要刪除的資料項的鍵名，預設為空字串。

### 6. 關閉儲存空間
```javascript
KVManager.closeKVStore();
```
**作用**: 清除目前操作的儲存空間名稱及相關加密資訊。
**參數**: 無

### 7. 刪除儲存空間
```javascript
KVManager.deleteKVStore();
```
**作用**: 刪除整個儲存空間及其所有鍵值對。
**參數**: 無

## 示例代碼

以下是一個簡單的示例，演示如何使用 `KVManager` 進行基本的操作：

```javascript
// 初始化 KVManager
KVManager.init();

// 設定儲存空間名稱
KVManager.getKVStore("myStore");

// 寫入資料
KVManager.put("username", "Alice");
KVManager.put("age", "25");

// 讀取資料
console.log(KVManager.get("username")); // 輸出: Alice
console.log(KVManager.get("age"));      // 輸出: 25

// 刪除資料
KVManager.delete("age");
console.log(KVManager.get("age"));      // 輸出: null

// 刪除整個儲存空間
KVManager.deleteKVStore();
console.log(KVManager.get("username")); // 輸出: null
```
