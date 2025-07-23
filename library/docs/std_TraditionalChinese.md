# 標準庫使用文檔

---

## 推送模組

推送模組包括一個 `push` 類

### 類 `Push`
#### 方法
- **`askForNotificationPermission()`**
  - 異步方法，請求瀏覽器的通知權限。
  - 返回值：`Promise<boolean>`，如果用戶授予了權限則返回 `true`，否則返回 `false`。
  
- **`requestPermission()`**
  - 別名方法，調用 `askForNotificationPermission()`。
  - 返回值：`Promise<boolean>`，如果用戶授予了權限則返回 `true`，否則返回 `false`。
  
- **`hasPermission()`**
  - 檢查是否已有權限或請求權限。
  - 返回值：`Promise<boolean>`，如果有權限則返回 `true`，否則返回 `false`。
  
- **`_showNotification(text)`**
  - 內部方法，顯示帶有指定文本的通知。
  - 參數：
    - `text` (`string`)：通知的內容。
  
- **`showNotification(text)`**
  - 調用 `_showNotification(text)` 來顯示通知。
  - 參數：
    - `text` (`string`)：通知的內容。
  
- **`closeNotification()`**
  - 關閉當前顯示的通知。

---

## 加密模組

推送模組包括一個 `BlockCipher` 類

### 類 BlockCipher

#### 概述
`BlockCipher` 類提供了使用 AES-GCM 算法進行加密和解密的功能。AES-GCM 是一種對稱加密算法，適用於需要認證的加密場景。

#### 方法

1. **generateKey**
   - 描述: 生成一個 256 位長度的 AES-GCM 密鑰。
   - 返回值: Promise 對象，解析為 CryptoKey 對象。

2. **encryptString**
   - 描述: 使用給定的密鑰加密字符串數據。
   - 參數:
     - `key`: 由 `generateKey` 方法生成的 CryptoKey 對象。
     - `data`: 需要加密的字符串。
   - 返回值: 包含初始化向量 (`iv`) 和密文 (`ciphertext`) 的對象。兩者均為陣列形式。

3. **decryptString**
   - 描述: 使用給定的密鑰解密之前加密的數據。
   - 參數:
     - `key`: 由 `generateKey` 方法生成的 CryptoKey 對象。
     - `encryptedData`: 包含初始化向量 (`iv`) 和密文 (`ciphertext`) 的對象，與 `encryptString` 返回的對象格式一致。
   - 返回值: 解密後的原始字符串。

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

#### 注意事項
- 密鑰應妥善保管，不應洩露給未經授權的實體。
- 初始化向量 (`iv`) 在每次加密操作中應該是唯一的，以確保安全性。上述實現中通過 `window.crypto.getRandomValues` 自動生成隨機的 `iv` 值。
