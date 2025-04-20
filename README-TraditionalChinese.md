# OleanderTS 文件

實際上，本語言是 Oleander+JS+OleanderUI，但作者本來想用 Oleander+TS+OleanderUI。所以叫“OleanderTS”

[繁體中文](https://github.com/M720111120126/OleanderTS/blob/master/README-TraditionalChinese.md) [English](https://github.com/M720111120126/OleanderTS/blob/master/README-English.md)

---

## 語法

### Oleander 部分

Oleander 部分只為 OleanderTS 帶來了預處理和 JS 調用特性

#### 預處理

預處理指令以 `#` 開頭，在編譯時會進行展開。

##### `#include "file"`

```OleanderTS
#include preprocess_test.yh
// → 直接將文件內容複製到此處
```
注意：

1.此處的 file 為頁面代碼的相對目錄，如 ./entry/init.yh 使用 #include preprocess_test.yh 填充的是 ./entry/preprocess_test.yh

2.include 的所有東西，都必須在 app.json5 的 page 對應頁面的 dependencies 中寫好名稱 如：
```json5
{
  "page": [// 頁面表
    {
      "name": "init",// 頁面名稱
      "srcPath": "./entry",// 頁面位置（相對路徑）
      "dependencies": [
        "preprocess_test.yh"// 填入名稱
      ]// 依賴庫表
    }
  ]
}
```

##### `#define value key`

一個替換

```OleanderTS
# 例如這裡的代碼正常工作
#define + left

1 left 1
```

##### `# UI_start`

Oleander UI 部分的開啟標誌

```OleanderTS
#include ……
#define ……
一些JS代碼

# UI_start

這裡應該寫 Oleander UI 代碼了
```

#### JS 調用

見上面的 # UI_start 的示例，js 直接寫在 Oleander 部分 就可以執行了

### Oleander UI 部分

本文檔介紹了如何使用提供的 UI 組件，幫助你快速創建和渲染介面。文檔將通過詳細的示例，幫助你理解如何構建互動式和響應式 UI。

### 0. Oleander UI 語法

#### 佈局組件

使用 `佈局組件名稱() {}` 請注意，屬性（css 屬性）的設置需要尾隨逗號

```OleanderTS
佈局組件名稱() {
  屬性: 值,
  包含的組件
}
```

#### 基礎組件

使用 `基礎組件名稱(傳入的內容)` 或 `基礎組件名稱() {內容}`

##### `基礎組件名稱(傳入的內容)`

```OleanderTS
Button(1)
```

##### `基礎組件名稱() {內容}`

請注意尾隨逗號

`{}` 中使用 `data_` 前綴更改屬性，使用 `method_` 前綴調用方法

```OleanderTS
Button() {
  data_text : "1",
  method_set_on_click: "alert('按鈕1被點擊')",
  }
```

#### 條件渲染
```OleanderTS
if(條件) {
  條件渲染的組件
}
```

#### 循環渲染
```OleanderTS
x() {
  data_text : "${item}",
  method_for_render: "[1,2,3]"
}
```
這樣就會渲染三個“x”，並顯示為 1、2、3。任何需要調用 list（如這裡的 `[1,2,3]`）的內容的地方都可以使用 `${item}`

#### 示例：
```OleanderTS
Row() {
  "background" : "lightblue",
  "padding" : "20px",
  Column() {
    "margin" : "20px",
    "padding" : "10px",
    Button() {
      data_text : "1",
      data_on_click: "alert('按鈕1被點擊')",
    }
  }
  Column() {
    "margin" : "20px",
    "padding" : "10px",
    Button() {
      data_text : "3",
      data_on_click: "alert('按鈕3被點擊')",
    }
    if(isDaytime) {
      Button() {
        data_text : "2-白天才能看見的按鈕",
        data_on_click: "alert('按鈕2被點擊')"
      }
    }
    if(!isDaytime) {
      Button() {
        data_text : "2-晚上才能看見的按鈕",
        data_on_click: "alert('按鈕2被點擊')"
      }
    }
  }
}
```

### 1. 基礎組件

這些基礎組件是 UI 構建的核心，可以通過組合和定制這些組件來構建你的介面。

#### 1.1 `UIComponent` 類
所有 UI 組件都繼承自 `UIComponent` 類。該類包含常見的樣式和子組件管理功能。

##### 方法：
- `set_style(**kwargs)`：設置樣式，支持傳入多個 CSS 屬性和值。
- `render()`：渲染該組件並返回 HTML。

#### 1.2 `Button` 類

按鈕組件，允許用戶創建可點擊的按鈕。

##### 方法：
- `set_on_click(callback)`：設置按鈕的點擊事件，可以傳入 JavaScript 代碼或回調函數。（依賴於 on_click 屬性）

##### 屬性：
- `text`：顯示的文本
- `on_click`：設置按鈕的點擊事件，可以傳入 JavaScript 代碼或回調函數。

#### 1.3 `Radio` 類

單選框組件，允許用戶在多個選項中選擇一個。

##### 方法

- `set_checked(True)`：是否默認選中

#### 1.4 `Toggle` 類

切換按鈕組件，可以在兩種狀態（如開啟/關閉）之間切換。

##### 方法

- `set_checked(True)`：是否默認選中

##### 屬性

- `label_on`：開啟時顯示的文本
- `label_off`：關閉時顯示的文本

#### 1.5 `Progress` 類

進度條組件，用於顯示任務的完成進度。

##### 屬性

- `value`：進度

#### 1.6 `Image` 類

圖片組件，用於在介面中嵌入圖片。

##### 屬性

- `src`：圖片地址

### 2. 佈局組件

佈局組件用來控制多個子組件的排版。你可以使用 `Row` 或 `Column` 類來組織組件。

#### 2.1 `Row` 類

行佈局，子組件按水平方向排列。

#### 2.2 `Column` 類

列佈局，子組件按垂直方向排列。

### 3. 互動組件

互動組件如 `Dialog` 和 `Menu` 可以幫助你創建包含互動式內容的彈窗和導航菜單。

#### 3.1 `Dialog` 類

對話框組件，用於顯示消息或內容。

##### 屬性

- `title`：標題
- `content`：內容

#### 3.2 `Menu` 類

菜單組件，用於創建可點擊的列表項。

##### 方法

- `add_item`：添加列表項

### 4. 高級用法

#### 4.1 條件渲染（全部組件可使用的方法）

可以判斷條件並決定是否渲染

##### 示例
```OleanderTS
Button() {
  data_text : "2-白天才能看見的按鈕",
  data_on_click: "alert('按鈕2被點擊')",
  method_condition: "isDaytime"
}
```

注意：isDaytime 函數已經在 Oleander 部分使用 JS 定義過了，白天返回 true，晚上返回 false

白天能看見 button，晚上再打開就看不見了

#### 4.2 頁面調用

可以通過設置組件的屬性來嵌入其他的頁面

##### 屬性

- `src`：頁面名稱
- `width`：嵌入寬度
- `height`：嵌入高度

##### 示例：
```OleanderTS
iframe = Iframe(src="pay", width="800", height="600")
iframe.set_style(border="2px solid black")
html = button.render() + iframe.render() + auto_js_code
```

#### 4.3 組合複雜佈局

你可以通過將多個佈局組件（如 `Row` 和 `Column`）嵌套在一起，創建複雜的佈局。

##### 示例：
```OleanderTS
Row() {
  "background" : "lightblue",
  "padding" : "20px",
  Column() {
    "margin" : "20px",
    "padding" : "10px",
    Button() {
      data_text : "1",
      data_on_click: "alert('按鈕1被點擊')",
    }
  }
  Column() {
    "margin" : "20px",
    "padding" : "10px",
    Button() {
      data_text : "3",
      data_on_click: "alert('按鈕3被點擊')",
    }
    Button() {
      data_text : "2-白天才能看見的按鈕",
      data_on_click: "alert('按鈕2被點擊')",
      method_condition: "isDaytime"
    }
    Button() {
      data_text : "2-晚上才能看見的按鈕",
      data_on_click: "alert('按鈕2被點擊')",
      method_condition: "!isDaytime"
    }
  }
}
```

---

## 編譯

### 注意事項

請先安裝 json5 和 filetype 庫

### 文件結構

```file
└─ init
└─── init.yh
└─ app.json5
└─ build.json5
```

### app.json5

```json5
{
  "page": [// 頁面表
    {
      "name": "init",// 頁面名稱
      "srcPath": "./init",// 頁面位置（相對路徑）
      "dependencies": ["dependencies.yh"]// 依賴庫表
    }
  ],
  "APP_Scope": {// 軟件配置
    "icon": "$media: app_icon.png",// 圖標，位於 “APP_Scope/media/app_icon.png” $xx 就代表在 “APP_Scope/xx” 路徑下
    "name": "DEMO",// 名稱
    "lang":"zh_tw"
  }
}
```

### build.json5

```json5
{
  "Minimum-required-API-version": "0.6.3",// 最低兼容的 API 版本，必需
  "Target-API-version": "0.6.3",// 目標的 API 版本，必需
  "name": "demo",// 項目名及模塊 root 包名，必需
  "version": "1.0.0",// 模塊版本信息，必需
  "compile-option": {
    "version": true
  }// 額外編譯命令選項，非必需
}
```

### 編譯方式

額外編譯命令選項 :

```
“--fapi-version API版本” 或 “-fver API版本” 指定 API 版本
“--version” 或 “-v” 獲取 API 版本
“--skip-env-check” 或 “-e” 跳過環境檢查

也可以在 build.json5 中指定
"compile-option": {
  "version": true,// 獲取 API 版本，使用 true 或 false 控制
  "skip_env_check": true,// 跳過環境檢查，使用 true 或 false 控制
  "fapi_version": "beta"// 指定 API 版本，有 beta 和 alpha 兩個版本可選
}

```

先 `cd` 至您的項目資料夾

直接執行 main.py

將編譯爲 app.html

注意：
* 本教程適用於 OleanderTS-API V0.6.3 Gamma 版