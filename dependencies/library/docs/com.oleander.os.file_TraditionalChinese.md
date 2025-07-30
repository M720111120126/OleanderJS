# con.oleander.os.file 使用說明文件

`con.oleander.os.file`提供了一個叫做`OleanderFileSystem`的類別

## 概述
`OleanderFileSystem` 是一個簡單的靜態類別，用於管理瀏覽器的 `localStorage` 中的檔案資料。該類別提供了讀取、寫入和刪除檔案的方法。每個檔案的資料儲存在 `localStorage` 中，並且使用固定的命名空間 `"Oleander"` 以避免衝突。

## 方法說明

### 1. 讀取檔案
```javascript
OleanderFileSystem.read(name);
```
**作用**: 從 `localStorage` 中讀取指定名稱的檔案內容。
**參數**:
- `name`: 字串類型，要讀取的檔案名稱，預設為空字串。
**返回值**: 返回檔案的內容，如果檔案不存在則返回 `null`。

### 2. 寫入檔案
```javascript
OleanderFileSystem.write(name, value);
```
**作用**: 將指定內容寫入到 `localStorage` 中的檔案。
**參數**:
- `name`: 字串類型，要寫入的檔案名稱，預設為空字串。
- `value`: 要寫入檔案的內容，預設為空字串。
**返回值**: 返回成功寫入的內容。

### 3. 刪除檔案
```javascript
OleanderFileSystem.delete(name);
```
**作用**: 從 `localStorage` 中刪除指定名稱的檔案。
**參數**:
- `name`: 字串類型，要刪除的檔案名稱，預設為空字串。

## 示例代碼

以下是一個簡單的示例，演示如何使用 `OleanderFileSystem` 進行基本的檔案操作：

```javascript
// 寫入檔案
OleanderFileSystem.write("example.txt", "Hello, World!");
console.log(OleanderFileSystem.read("example.txt")); // 輸出: Hello, World!

// 修改檔案內容
OleanderFileSystem.write("example.txt", "Updated content");
console.log(OleanderFileSystem.read("example.txt")); // 輸出: Updated content

// 刪除檔案
OleanderFileSystem.delete("example.txt");
console.log(OleanderFileSystem.read("example.txt")); // 輸出: null
```

通過上述步驟，您可以方便地在 `localStorage` 中管理和操作檔案資料。

## 注意事項
- `localStorage` 的容量有限（通常為 5MB），因此不適合儲存大量資料。
- 儲存在 `localStorage` 中的資料是明文形式，不建議儲存敏感資訊。
- 確保檔案名稱中不包含特殊字符，以免導致儲存或讀取錯誤。
