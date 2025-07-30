# data 库使用文档

data库内包括一个用于管理键值对（Key-Value）存储的静态类叫`KVManager`

## 概述
`KVManager` 是一个用于管理键值对（Key-Value）存储的静态类，利用浏览器的 `localStorage` 来持久化数据。该类提供了初始化、获取存储空间、读取、写入、删除和关闭/销毁存储空间的方法。

## 方法说明

### 1. 初始化
```javascript
KVManager.init();
```
**作用**: 初始化 `KVManager` 类，将当前操作的存储空间名称清空。
**参数**: 无

### 2. 获取存储空间
```javascript
KVManager.getKVStore(KVStorename, encrypt, key);
```
**作用**: 获取一个存储空间
**参数**:
- `KVStorename`: 字符串类型，指定存储空间的名称，默认为 `"test"`。
- `encrypt`: 布尔类型，是否启用加密，默认为 `false`。如需使用，请先导入 `std` 库以提供加密支持。
- `key`: 字符串类型，加密密钥，默认为空字符串。

### 3. 读取数据
```javascript
KVManager.get(key);
```
**作用**: 根据键名从当前存储空间中读取对应的值。
**参数**:
- `key`: 字符串类型，要读取的数据项的键名，默认为空字符串。
**返回值**: 返回对应键名的值，如果不存在则返回 `null`。

### 4. 写入数据
```javascript
KVManager.put(key, value);
```
**作用**: 将键值对保存到当前存储空间中。
**参数**:
- `key`: 字符串类型，要保存的数据项的键名，默认为空字符串。
- `value`: 要保存的数据项的值，默认为空字符串。
**返回值**: 返回成功写入的值。

### 5. 删除数据
```javascript
KVManager.delete(key);
```
**作用**: 根据键名从当前存储空间中删除对应的键值对。
**参数**:
- `key`: 字符串类型，要删除的数据项的键名，默认为空字符串。

### 6. 关闭存储空间
```javascript
KVManager.closeKVStore();
```
**作用**: 清除当前操作的存储空间名称及相关加密信息。
**参数**: 无

### 7. 删除存储空间
```javascript
KVManager.deleteKVStore();
```
**作用**: 删除整个存储空间及其所有键值对。
**参数**: 无

## 示例代码

以下是一个简单的示例，演示如何使用 `KVManager` 进行基本的操作：

```javascript
// 初始化 KVManager
KVManager.init();

// 设置存储空间名称
KVManager.getKVStore("myStore");

// 写入数据
KVManager.put("username", "Alice");
KVManager.put("age", "25");

// 读取数据
console.log(KVManager.get("username")); // 输出: Alice
console.log(KVManager.get("age"));      // 输出: 25

// 删除数据
KVManager.delete("age");
console.log(KVManager.get("age"));      // 输出: null

// 删除整个存储空间
KVManager.deleteKVStore();
console.log(KVManager.get("username")); // 输出: null
```
