# 标准库 使用文档

---

## 推送模块

推送模块包括一个`push`类

### 类 `Push`
#### 方法
- **`askForNotificationPermission()`**
  - 异步方法，请求浏览器的通知权限。
  - 返回值：`Promise<boolean>`，如果用户授予了权限则返回 `true`，否则返回 `false`。
  
- **`requestPermission()`**
  - 别名方法，调用 `askForNotificationPermission()`。
  - 返回值：`Promise<boolean>`，如果用户授予了权限则返回 `true`，否则返回 `false`。
  
- **`hasPermission()`**
  - 检查是否已有权限或请求权限。
  - 返回值：`Promise<boolean>`，如果有权限则返回 `true`，否则返回 `false`。
  
- **`_showNotification(text)`**
  - 内部方法，显示带有指定文本的通知。
  - 参数：
    - `text` (`string`)：通知的内容。
  
- **`showNotification(text)`**
  - 调用 `_showNotification(text)` 来显示通知。
  - 参数：
    - `text` (`string`)：通知的内容。
  
- **`closeNotification()`**
  - 关闭当前显示的通知。

---

## 加密模块

推送模块包括一个`BlockCipher`类

### 类 BlockCipher

#### 概述
`BlockCipher` 类提供了使用 AES-GCM 算法进行加密和解密的功能。AES-GCM 是一种对称加密算法，适用于需要认证的加密场景。

#### 方法

1. **generateKey**
   - 描述: 生成一个 256 位长度的 AES-GCM 密钥。
   - 返回值: Promise 对象，解析为 CryptoKey 对象。

2. **encryptString**
   - 描述: 使用给定的密钥加密字符串数据。
   - 参数:
     - `key`: 由 `generateKey` 方法生成的 CryptoKey 对象。
     - `data`: 需要加密的字符串。
   - 返回值: 包含初始化向量 (`iv`) 和密文 (`ciphertext`) 的对象。两者均为数组形式。

3. **decryptString**
   - 描述: 使用给定的密钥解密之前加密的数据。
   - 参数:
     - `key`: 由 `generateKey` 方法生成的 CryptoKey 对象。
     - `encryptedData`: 包含初始化向量 (`iv`) 和密文 (`ciphertext`) 的对象，与 `encryptString` 返回的对象格式一致。
   - 返回值: 解密后的原始字符串。

#### 示例代码

```javascript
const blockCipher = new BlockCipher();

async function runExample() {
    // 生成密钥
    const key = await blockCipher.generateKey();
    
    // 加密字符串
    const originalText = "Hello, World!";
    const encryptedData = await blockCipher.encryptString(key, originalText);
    console.log("Encrypted Data:", encryptedData);

    // 解密字符串
    const decryptedText = await blockCipher.decryptString(key, encryptedData);
    console.log("Decrypted Text:", decryptedText);
}

runExample().catch(console.error);
```

#### 注意事项
- 密钥应妥善保管，不应泄露给未经授权的实体。
- 初始化向量 (`iv`) 在每次加密操作中应该是唯一的，以确保安全性。上述实现中通过 `window.crypto.getRandomValues` 自动生成随机的 `iv` 值。

---

## 设备信息模块

### 类 RetrieveDeviceInformation

#### 概述

`RetrieveDeviceInformation` 类提供了获取设备信息的功能，包括操作系统、浏览器、屏幕分辨率等。

#### 方法

1. **getOS**
   - 描述: 获取操作系统信息。
     - 参数: 无。
   - 返回值: 系统名称。

2. **getBrowser**
   - 描述: 获取浏览器信息。
     - 参数: 无。
   - 返回值: 浏览器名称。

3. **getMemory**
   - 描述: 获取内存大小近似值(GB)。
     - 参数: 无。
   - 返回值: 内存大小近似值(GB，浮点数)。

4. **getPreferredColorScheme**
   - 描述: 获取深色模式配置。
     - 参数: 无。
   - 返回值: 布尔值，是否开启深色模式。

5. **getPreferredReducedMotion**
   - 描述: 获取是否减少动画的设置。
     - 参数: 无。
   - 返回值: 布尔值。

6. **getPreferredContrast**
   - 描述: 获取对比度设置。
     - 参数: 无。
   - 返回值: 布尔值，是否开启高对比度模式。

7. **getUserAgent**
   - 描述: 获取用户代理字符串。
     - 参数: 无。
   - 返回值: 用户代理字符串。

## 剪贴板模块

### 类 Clipboard

#### 概述

`Clipboard` 类提供了对剪贴板的访问功能，包括读取和写入文本。

### 方法

1. **setClipboard**
    - 描述: 将文本写入剪贴板。
    - 参数:
      - `text` (`string`): 要写入剪贴板的文本。
    - 返回值: 无

2. **resetClipboard**
    - 描述: 清空剪贴板内容。
    - 参数: 无。
    - 返回值: 无

3. **getLastPastedText**
    - 描述: 获取最近一次粘贴的文本。
    - 参数: 无。
    - 返回值: `string`，表示最近一次粘贴的文本。


