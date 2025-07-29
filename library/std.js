/* jshint esversion: 8 */

let denied = false;
let notification = null;
class push {
    async askForNotificationPermission() {
        try {
            const allowedByBrowser = await Notification.requestPermission();
            if (!allowedByBrowser) {
                throw new Error('Denied by browser');
            }
            denied = false;
            return true;
        } catch (e) {
            denied = true;
            console.warn('Could not request notification permissions', e);
            return false;
        }
    }
    requestPermission() {
        return this.askForNotificationPermission();
    }

    hasPermission() {
        if (denied) {
            return false;
        }
        return this.askForNotificationPermission();
    }

    async _showNotification(text) {
        if (await this.hasPermission()) {
            notification = new Notification('Notification from project', {
                body: text
            });
        }
    }

    showNotification(text) {
        this._showNotification(text);
    }

    closeNotification() {
        if (notification) {
            notification.close();
        }
    }
}

class BlockCipher {
    async generateKey() {
        return window.crypto.subtle.generateKey(
            {
                name: "AES-GCM",
                length: 256,
            },
            true, // 是否可提取密钥材料
            ["encrypt", "decrypt"]
        );
    }

    async encryptString(key, data) {
        const encoder = new TextEncoder();
        const iv = window.crypto.getRandomValues(new Uint8Array(12)); // 初始化向量
        const ciphertext = await window.crypto.subtle.encrypt(
            {
                name: "AES-GCM",
                iv: iv,
            },
            key,
            encoder.encode(data)
        );
        return { iv: Array.from(iv), ciphertext: Array.from(new Uint8Array(ciphertext)) };
    }

    async decryptString(key, encryptedData) {
        const decoder = new TextDecoder();
        const iv = Uint8Array.from(encryptedData.iv);
        const ciphertext = Uint8Array.from(encryptedData.ciphertext);
        const decrypted = await window.crypto.subtle.decrypt(
            {
                name: "AES-GCM",
                iv: iv,
            },
            key,
            ciphertext
        );
        return decoder.decode(decrypted);
    }
}

class RetrieveDeviceInformation {
    getOS() {
      const userAgent = navigator.userAgent;
      if (userAgent.includes("Windows")) {
        return "Windows";
      } else if (userAgent.includes("Android")) {
        return "Android";
      } else if (
        userAgent.includes("iPhone") 
      ) {
        return "iPhone";
     } else if (
        userAgent.includes("iPod")
     ) {
        return "iPod";
     } else if (
        userAgent.includes("iPad")
     ) {
        return "iPad";
      } else if (userAgent.includes("Linux")) {
        return "Linux";
      } else if (userAgent.includes("CrOS")) {
        return "ChromeOS";
      } else if (userAgent.includes("Mac OS")) {
        return "macOS";
      }
      return "Other";
    }

    getBrowser() {
      const userAgent = navigator.userAgent;
      if (userAgent.includes("Chrome")) {
        return "Chrome";
      } else if (userAgent.includes("Firefox")) {
        return "Firefox";
      } else if (userAgent.includes("Safari")) {
        return "Safari";
      }
      return "Other";
    }

    getMemory() {
      if (navigator.deviceMemory == undefined) {
        return "Unsupported";
      } else {
        return navigator.deviceMemory;
      }
    }

    getPreferredColorScheme(args) {
      return !!window.matchMedia("(prefers-color-scheme: dark)").matches;
    }

    getPreferredReducedMotion() {
      return !!window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    }

    getPreferredContrast() {
      return !!window.matchMedia("(prefers-contrast: more)").matches;
    }

    getUserAgent() {
      return navigator.userAgent;
    }
}

class Clipboard {
    setClipboard(text) {
      navigator.clipboard.writeText(text);
    }

    resetClipboard() {
      navigator.clipboard.writeText("");
    }

    getLastPastedText() {
      return lastPastedText;
    }
}
