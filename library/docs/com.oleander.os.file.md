# con.oleander.os.file 使用文档

`con.oleander.os.file`提供了一个叫做`OleanderFileSystem`的类

## 概述
`OleanderFileSystem` 是一个简单的静态类，用于管理浏览器的 `localStorage` 中的文件数据。该类提供了读取、写入和删除文件的方法。每个文件的数据存储在 `localStorage` 中，并且使用固定的命名空间 `"Oleander"` 以避免冲突。

## 方法说明

### 1. 读取文件
```javascript
OleanderFileSystem.read(name);
```
**作用**: 从 `localStorage` 中读取指定名称的文件内容。
**参数**:
- `name`: 字符串类型，要读取的文件名称，默认为空字符串。
**返回值**: 返回文件的内容，如果文件不存在则返回 `null`。

### 2. 写入文件
```javascript
OleanderFileSystem.write(name, value);
```
**作用**: 将指定内容写入到 `localStorage` 中的文件。
**参数**:
- `name`: 字符串类型，要写入的文件名称，默认为空字符串。
- `value`: 要写入文件的内容，默认为空字符串。
**返回值**: 返回成功写入的内容。

### 3. 删除文件
```javascript
OleanderFileSystem.delete(name);
```
**作用**: 从 `localStorage` 中删除指定名称的文件。
**参数**:
- `name`: 字符串类型，要删除的文件名称，默认为空字符串。

## 示例代码

以下是一个简单的示例，演示如何使用 `OleanderFileSystem` 进行基本的文件操作：

```javascript
// 写入文件
OleanderFileSystem.write("example.txt", "Hello, World!");
console.log(OleanderFileSystem.read("example.txt")); // 输出: Hello, World!

// 修改文件内容
OleanderFileSystem.write("example.txt", "Updated content");
console.log(OleanderFileSystem.read("example.txt")); // 输出: Updated content

// 删除文件
OleanderFileSystem.delete("example.txt");
console.log(OleanderFileSystem.read("example.txt")); // 输出: null
```

通过上述步骤，您可以方便地在 `localStorage` 中管理和操作文件数据。

## 注意事项
- `localStorage` 的容量有限（通常为 5MB），因此不适合存储大量数据。
- 存储在 `localStorage` 中的数据是明文形式，不建议存储敏感信息。
- 确保文件名中不包含特殊字符，以免导致存储或读取错误。