# con.oleander.os.file Documentation

`con.oleander.os.file` provides a class called `OleanderFileSystem`.

## Overview
`OleanderFileSystem` is a simple static class for managing file data in the browser's `localStorage`. This class provides methods for reading, writing, and deleting files. Each file's data is stored in `localStorage` and uses the fixed namespace `"Oleander"` to avoid conflicts.

## Method Descriptions

### 1. Read File
```javascript
OleanderFileSystem.read(name);
```
**Function**: Reads the content of a file with the specified name from `localStorage`.
**Parameters**:
- `name`: String type, the name of the file to read, defaults to an empty string.
**Return Value**: Returns the content of the file, or `null` if the file does not exist.

### 2. Write File
```javascript
OleanderFileSystem.write(name, value);
```
**Function**: Writes the specified content to a file in `localStorage`.
**Parameters**:
- `name`: String type, the name of the file to write, defaults to an empty string.
- `value`: The content to write to the file, defaults to an empty string.
**Return Value**: Returns the successfully written content.

### 3. Delete File
```javascript
OleanderFileSystem.delete(name);
```
**Function**: Deletes the file with the specified name from `localStorage`.
**Parameters**:
- `name`: String type, the name of the file to delete, defaults to an empty string.

## Example Code

The following is a simple example demonstrating how to use `OleanderFileSystem` for basic file operations:

```javascript
// Write file
OleanderFileSystem.write("example.txt", "Hello, World!");
console.log(OleanderFileSystem.read("example.txt")); // Output: Hello, World!

// Modify file content
OleanderFileSystem.write("example.txt", "Updated content");
console.log(OleanderFileSystem.read("example.txt")); // Output: Updated content

// Delete file
OleanderFileSystem.delete("example.txt");
console.log(OleanderFileSystem.read("example.txt")); // Output: null
```

Through the above steps, you can easily manage and manipulate file data in `localStorage`.

## Precautions
- `localStorage` has limited capacity (usually 5MB), so it is not suitable for storing large amounts of data.
- Data stored in `localStorage` is in plain text format, so it is not recommended to store sensitive information.
- Ensure that the file name does not contain special characters to avoid storage or reading errors.
