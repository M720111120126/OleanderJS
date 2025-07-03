# com.oleander.file Usage Documentation

`com.oleander.file` provides a class called `FileSystem`

## Overview
`FileSystem` is a simple static class for managing file data in the browser's `localStorage`. This class provides methods for reading, writing, and deleting files. Each file's data is stored in `localStorage`, and the project name (`ProjectName`) is used as a namespace to avoid conflicts.

## Method Descriptions

### 1. Read File
```javascript
FileSystem.read(name);
```
**Function**: Reads the content of a file with the specified name from `localStorage`.
**Parameters**:
- `name`: String type, the name of the file to read, defaults to an empty string.
**Return Value**: Returns the content of the file, or `null` if the file does not exist.

### 2. Write File
```javascript
FileSystem.write(name, value);
```
**Function**: Writes the specified content to a file in `localStorage`.
**Parameters**:
- `name`: String type, the name of the file to write, defaults to an empty string.
- `value`: The content to write to the file, defaults to an empty string.
**Return Value**: Returns the content that was successfully written.

### 3. Delete File
```javascript
FileSystem.delete(name);
```
**Function**: Deletes a file with the specified name from `localStorage`.
**Parameters**:
- `name`: String type, the name of the file to delete, defaults to an empty string.

## Example Code

The following is a simple example demonstrating how to use `FileSystem` for basic file operations:

```javascript
// Assume ProjectName is already defined
const ProjectName = "myProject";

// Write file
FileSystem.write("example.txt", "Hello, World!");
console.log(FileSystem.read("example.txt")); // Output: Hello, World!

// Modify file content
FileSystem.write("example.txt", "Updated content");
console.log(FileSystem.read("example.txt")); // Output: Updated content

// Delete file
FileSystem.delete("example.txt");
console.log(FileSystem.read("example.txt")); // Output: null
```

Through the above steps, you can easily manage and manipulate file data in `localStorage`.

## Precautions
- Ensure that `ProjectName` is correctly set before using the `FileSystem` class, otherwise it may cause file name conflicts or failure to find the file.
- `localStorage` has limited capacity (usually 5MB), so it is not suitable for storing large amounts of data.
- Data stored in `localStorage` is in plain text format, so it is not recommended to store sensitive information.
