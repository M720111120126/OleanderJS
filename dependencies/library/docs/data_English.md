# data Library Usage Documentation

The data library includes a static class called `KVManager` for managing key-value pair storage.

## Overview
`KVManager` is a static class for managing key-value pair storage, utilizing the browser's `localStorage` to persist data. This class provides methods for initializing, getting storage space, reading, writing, deleting, and closing/destroying storage space.

## Method Descriptions

### 1. Initialization
```javascript
KVManager.init();
```
**Function**: Initializes the `KVManager` class, clearing the name of the currently operated storage space.
**Parameters**: None

### 2. Get storage space
```javascript
KVManager.getKVStore(KVStorename, encrypt, key);
```
**Function**: Get a storage space
**Parameter**:
- `KVStorename`: String type, specifying the name of the storage space, default is `"test"`.
- `encrypt`: Boolean type, whether encryption is enabled, default is `false`. To use, please first import the `std` library to provide encryption support.
- `key`: String type, encryption key, default to empty string.

### 3. Read Data
```javascript
KVManager.get(key);
```
**Function**: Reads the corresponding value from the current storage space based on the key name.
**Parameters**:
- `key`: String type, the key name of the data item to be read, defaults to an empty string.
**Return Value**: Returns the value of the corresponding key name, or `null` if it does not exist.

### 4. Write Data
```javascript
KVManager.put(key, value);
```
**Function**: Saves the key-value pair to the current storage space.
**Parameters**:
- `key`: String type, the key name of the data item to be saved, defaults to an empty string.
- `value`: The value of the data item to be saved, defaults to an empty string.
**Return Value**: Returns the successfully written value.

### 5. Delete Data
```javascript
KVManager.delete(key);
```
**Function**: Deletes the corresponding key-value pair from the current storage space based on the key name.
**Parameters**:
- `key`: String type, the key name of the data item to be deleted, defaults to an empty string.

### 6. Close Storage Space
```javascript
KVManager.closeKVStore();
```
**Function**: Clears the name of the currently operated storage space and related encryption information.
**Parameters**: None

### 7. Delete Storage Space
```javascript
KVManager.deleteKVStore();
```
**Function**: Deletes the entire storage space and all its key-value pairs.
**Parameters**: None

## Example Code

The following is a simple example demonstrating how to use `KVManager` for basic operations:

```javascript
// Initialize KVManager
KVManager.init();

// Set storage space name
KVManager.getKVStore("myStore");

// Write data
KVManager.put("username", "Alice");
KVManager.put("age", "25");

// Read data
console.log(KVManager.get("username")); // Output: Alice
console.log(KVManager.get("age"));      // Output: 25

// Delete data
KVManager.delete("age");
console.log(KVManager.get("age"));      // Output: null

// Delete the entire storage space
KVManager.deleteKVStore();
console.log(KVManager.get("username")); // Output: null
```
