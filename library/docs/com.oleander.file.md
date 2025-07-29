# com.oleander.file 使用文档

`com.oleander.file`提供了一个叫做`FileSystem`的类

## 概述
`FileSystem` 是一个简单的静态类，用于管理浏览器的 `localStorage` 中的文件数据。该类提供了读取、写入和删除文件的方法。每个文件的数据存储在 `localStorage` 中，并且使用项目名称（`ProjectName`）作为命名空间以避免冲突。

## 方法说明

### 1. 读取文件
```javascript
FileSystem.read(name);
```
**作用**: 从 `localStorage` 中读取指定名称的文件内容。
**参数**:
- `name`: 字符串类型，要读取的文件名称，默认为空字符串。
**返回值**: 返回文件的内容，如果文件不存在则返回 `null`。

### 2. 写入文件
```javascript
FileSystem.write(name, value);
```
**作用**: 将指定内容写入到 `localStorage` 中的文件。
**参数**:
- `name`: 字符串类型，要写入的文件名称，默认为空字符串。
- `value`: 要写入文件的内容，默认为空字符串。
**返回值**: 返回成功写入的内容。

### 3. 删除文件
```javascript
FileSystem.delete(name);
```
**作用**: 从 `localStorage` 中删除指定名称的文件。
**参数**:
- `name`: 字符串类型，要删除的文件名称，默认为空字符串。

## 示例代码

以下是一个简单的示例，演示如何使用 `FileSystem` 进行基本的文件操作：

```javascript
// 写入文件
FileSystem.write("example.txt", "Hello, World!");
console.log(FileSystem.read("example.txt")); // 输出: Hello, World!

// 修改文件内容
FileSystem.write("example.txt", "Updated content");
console.log(FileSystem.read("example.txt")); // 输出: Updated content

// 删除文件
FileSystem.delete("example.txt");
console.log(FileSystem.read("example.txt")); // 输出: null
```

通过上述步骤，您可以方便地在 `localStorage` 中管理和操作文件数据。

## 注意事项
- 确保 `ProjectName` 在使用 `FileSystem` 类之前已经被正确设置，否则会导致文件名冲突或无法找到文件。
- `localStorage` 的容量有限（通常为 5MB），因此不适合存储大量数据。
- 存储在 `localStorage` 中的数据是明文形式，不建议存储敏感信息。