# OleanderJS文檔

[简体中文](https://github.com/M720111120126/OleanderJS/blob/master/README.md) [English](https://github.com/M720111120126/OleanderJS/blob/master/README-English.md)

---

## 語法

### Oleander 部分

Oleander 部分只為 OleanderJS 帶來了預處理和 JS 調用特性

#### 注意事項

##### 變數

變數必須以字母開頭，只能有字母和底線。

#### 預處理

預處理指令以 `#` 開頭，在編譯時會進行展開。

##### `#include file`

```OleanderJS
#include preprocess_test.yh
// → 直接將檔案內容複製到此處
```
注意：

1. 此處的 file 為頁面程式碼的相對目錄，如 ./entry/init.yh 使用 #include preprocess_test.yh 填充的是 ./entry/preprocess_test.yh

2. include 的所有東西，都必須在 app.json5 的 page 對應頁面的 dependencies 中寫好名稱 如：
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

##### `#include 依賴庫`

可用的標準庫

* [data](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/data_TraditionalChinese.md)
* [router](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/router_TraditionalChinese.md)
* [std](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/std_TraditionalChinese.md)

##### `#define value key`

一個替換

```OleanderJS
# 例如這裡的程式碼正常工作
#define + left

1 left 1
```

##### `# UI_start`

Oleander UI 部分的開啟標誌

```OleanderJS
#include ……
#define ……
一些JS程式碼

# UI_start

這裡應該寫 Oleander UI 程式碼了
```

#### JS 調用

見上面的 # UI_start 的示例，js 直接寫在 Oleander 部分 就可以執行了

#### 權限管理

##### 權限列表

* [`com.oleander.file` 獲取一個屬於該 app 的檔案空間](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/com.oleander.file_TraditionalChinese.md)
* [`con.oleander.os.file` 獲取所有 OleanderAPP 共用的檔案空間](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/com.oleander.os.file_TraditionalChinese.md)

請注意：請求權限失敗不會拋出異常，在獲取權限後應當檢查 `rights_name_json` 這個 list 內有沒有請求的權限

##### 權限獲取方式-靜態獲取

這將會在 app 啟動的時候向用戶請求權限。

在 `app.json5` 中定義。

```json5
{
  ...
  "APP_Scope": {// 軟體配置
    ...
    "require":[// APP 需要調用的權限
      "com.oleander.file"
    ]
  }
}
```

##### 權限獲取方式-動態獲取

這將會在 app 運行至導入的地方的時候向用戶請求權限。

使用 `#include` 導入

```OleanderJS
#include com.oleander.file
```

### Oleander UI 部分

本文檔介紹了如何使用提供的 UI 組件，幫助你快速建立和渲染介面。文檔將通過詳細的示例，幫助你理解如何構建互動式和響應式 UI。

### 0. Oleander UI 語法

#### 佈局組件

使用 `佈局組件名稱() {}` 請注意，屬性（css 屬性）的設定需要尾隨逗號

```OleanderJS
佈局組件名稱() {
  包含的組件
}
.style(屬性=值)
```

#### 基礎組件

##### OleanderUI-ArkPRO 框架（更推薦）

請注意尾隨逗號

使用 `.SA("x",y)` 更改屬性，使用 `.x(y)` 調用方法

```OleanderJS
Button()
.SA("text", "1")
.set_on_click("alert('按鈕1被點擊')")
```

更改屬性的特殊方式支持通過 `組件名稱(屬性)` 的方法更改屬性，這種方法叫做 `DCA`

比如上面的例子就可以寫成

```OleanderJS
Button("1")
.set_on_click("alert('按鈕1被點擊')")
```

#### 條件渲染
```OleanderJS
if("條件") {
  條件渲染的組件
}
```

#### 循環渲染
```OleanderJS
x() {}
.text = "${item}"
.for_render("[1,2,3]")
```
這樣就會渲染三個“x”，並顯示為 1、2、3。任何需要調用 list（如這裡的 `[1,2,3]`）的內容的地方都可以使用 `${item}`

#### 示例：

見項目 `/ProjectExample-ark` 資料夾

##### OleanderUI-object 框架（更強大）

類似於 python 的物件

使用 `物件.屬性=內容` 前綴更改屬性，使用 `物件.方法(內容)` 前綴調用方法

```OleanderJS
Button = Button()
Button.text = "1"
Button.on_click = "alert('按鈕1被點擊')
```

#### 條件渲染

使用 `condition` 方法

```OleanderJS
物件.condition("js 返回 bool 的表達式")
```

#### 循環渲染

使用 `for_render` 方法

```OleanderJS
物件.for_render(第一項,第二項...)
```
這樣就會渲染三個“物件”，並顯示為 1、2...。任何需要調用 list（如這裡的 `[1,2...]`）的內容的地方都可以使用 `${item}`

#### 示例：

見項目 `/ProjectExample-object` 資料夾

### 1. 基礎組件

這些基礎組件是 UI 構建的核心，可以通過組合和定制這些組件來構建你的介面。

#### 1.1 `UIComponent` 類別
所有 UI 組件都繼承自 `UIComponent` 類別。該類別包含常見的樣式和子組件管理功能。

##### 方法：
- `set_style(**kwargs)`：設定樣式，支持傳入多個 CSS 屬性和值。
- `render()`：渲染該組件並返回 HTML。

##### 特性
- `text屬性`：可以使用`js_`前綴以使用在 JavaScript 中定義的變數作為顯示的文字

#### 1.2 `Text` 類別

文字組件，允許建立文字。

##### 屬性：
- `text`：顯示的文字

##### DCA：
`Text(text="", size=1)`

#### 1.3 `Button` 類別

按鈕組件，允許用戶建立可點擊的按鈕。

##### 方法：
- `set_on_click(callback)`：設定按鈕的點擊事件，可以傳入 JavaScript 程式碼或回調函數。（依賴於 on_click 屬性）

##### 屬性：
- `text`：顯示的文字
- `on_click`：設定按鈕的點擊事件，可以傳入 JavaScript 程式碼或回調函數。

##### DCA：
`Button(text="")`

#### 1.4 `Radio` 類別

單選框組件，允許用戶在多個選項中選擇一個。

##### 方法:
- `set_checked(True)`：是否預設選中

##### DCA：
`Radio(name="", value="")`

#### 1.5 `Toggle` 類別

切換按鈕組件，可以在兩種狀態（如開啟/關閉）之間切換。

##### 方法:

- `set_checked(True)`：是否預設選中

##### 屬性:

- `label_on`：開啟時顯示的文字
- `label_off`：關閉時顯示的文字

##### DCA:
`Toggle(label_on="", label_off="")`

#### 1.6 `Progress` 類別

進度條組件，用於顯示任務的完成進度。

##### 屬性：
- `value`：進度

##### DCA：
`Progress(value=0)`

#### 1.7 `Image` 類別

圖片組件，用於在介面中嵌入圖片。

##### 屬性：
- `src`：圖片地址

##### DCA：
`Image(src="")`

### 2. 佈局組件

佈局組件用來控制多個子組件的排版。你可以使用 `Row` 或 `Column` 類別來組織組件。

#### 2.1 `Row` 類別

行佈局，子組件按水平方向排列。

#### 2.2 `Column` 類別

列佈局，子組件按垂直方向排列。

### 3. 互動組件

互動組件如 `Dialog` 和 `Menu` 可以幫助你建立包含互動式內容的彈窗和導航選單。

#### 3.1 `Dialog` 類別

對話框組件，用於顯示消息或內容。

##### 屬性：
- `title`：標題
- `content`：內容

##### DCA：
`Dialog(title="", content="")`

#### 3.2 `Menu` 類別

選單組件，用於建立可點擊的列表項。

##### 方法：
- `add_item`：添加列表項

### 4. 高級用法

#### 4.1 條件渲染（全部組件可使用的方法）

可以判斷條件並決定是否渲染

##### 示例
```OleanderJS
Button() {
  data_text : "2-白天才能看見的按鈕",
  data_on_click: "alert('按鈕2被點擊')",
  method_condition: "isDaytime"
}
```

注意：isDaytime 函數已經在 Oleander 部分使用 JS 定義過了，白天返回 true，晚上返回 false

白天能看見 button，晚上再打開就看不見了

#### 4.1 內置調用

內置調用以 `$` 開頭

##### $r

獲取文件，如 `$r("$media: app_icon.png")` 獲取 `APP_Scope/media/app_icon.png` 文件

其中 `$xx` 就代表在 `APP_Scope/xx` 路徑下

---

## 編譯

配置文件有 `json5` 和 `toml` 兩種格式，可以任選一種使用。推薦使用 `toml`。

請先安裝 json5 和 filetype 庫

### 檔案結構

```file
└─ init
└─── init.yh
└─ app.json5 \ app.toml
└─ build.json5 \ build.toml
```

### json5

#### app.json5

```json5
{
  "page": [// 頁面表
    {
      "name": "init",// 頁面名稱
      "srcPath": "./init",// 頁面位置（相對路徑）
      "dependencies": ["dependencies.yh"]// 依賴庫表
    },
    {
      "name": "JumpTest",// 頁面名稱
      "srcPath": "./JumpTest",// 頁面位置（相對路徑）
      "dependencies": []// 依賴庫表
    }
  ],
  "APP_Scope": {// 軟體配置
    "icon": "$media: app_icon.png",// 圖示，位於 “APP_Scope/media/app_icon.png” $xx 就代表在 “APP_Scope/xx” 路徑下
    "name": "DEMO",// 名稱
    "lang":"zh_cn",// 語言
    "require":[// APP 需要調用的權限
      "com.oleander.file"
    ]
  }
}
```

#### build.json5

```json5
{
  "Minimum-required-API-version": "0.10.9",// 最低相容的 API 版本，必需
  "Target-API-version": "0.10.9",// 目標的 API 版本，必需
  "name": "demo",// 項目名及模組 root 包名，必需
  "version": "1.0.0",// 模組版本資訊，必需
  "compile-option": {
    "version": true
  }// 額外編譯命令選項，非必需
}
```

### toml

#### app.toml

```toml
[[page]] # 頁面表 項1
name = "init" # 頁面名稱
srcPath = "./init" # 頁面位置（相對路徑）
dependencies = ["dependencies.yh"] # 依賴庫表

[[page]] # 頁面表 項2
name = "JumpTest"
srcPath = "./JumpTest"
dependencies = []

[APP_Scope]
icon = "$media: app_icon.png" # 圖標，位於 “APP_Scope/media/app_icon.png” $xx 就代表在 “APP_Scope/xx” 路徑下
name = "DEMO" # 名稱
lang = "zh_cn" # 語言
require = ["com.oleander.file"] # APP需要調用的權限
```

#### build.toml

```toml
Minimum-required-API-version = "1.12.5" # 最低兼容的API版本，必需
Target-API-version = "1.12.6" # 目標的API版本，必需
name = "demo" # 項目名及模塊 root 包名，必需
version = "1.0.0" # 模塊版本信息，必需

[compile-option] # 額外編譯命令選項，非必需(可以空着但不能刪除)
version = true
```

### 額外編譯命令選項

```
“--fapi-version API版本” 或 “-fver API版本” 指定 API 版本
“--version” 或 “-v” 獲取 API 版本
“--skip-env-check” 或 “-e” 跳過環境檢查
“--verbose” 或 “-V” 打印出工具鏈依賴的相關信息以及編譯過程中執行的命令

也可以在 build.json5 或 build.toml 中指定

[compile-option] # 額外編譯命令選項，非必需(可以空着但不能刪除)
version = true # 獲取 API 版本，使用 true 或 false 控制
skip_env_check = true # 跳過環境檢查，使用 true 或 false 控制
fapi_version = "ArkPRO" # 指定 API 版本，有 object 和 ark 兩個版本可選
verbose = true # 打印出工具鏈依賴的相關信息以及編譯過程中執行的命令，使用 true 或 false 控制

"compile-option": {
  "version": true,// 獲取 API 版本，使用 true 或 false 控制
  "skip_env_check": true,// 跳過環境檢查，使用 true 或 false 控制
  "fapi_version": "ArkPRO",// 指定 API 版本，有 object 和 ark 兩個版本可選
  "verbose": true// 打印出工具鏈依賴的相關信息以及編譯過程中執行的命令，使用 true 或 false 控制
}

```

## 命令行工具使用指南

### OJPM(OleanderJsProjectManager)

#### init

初始化 OleanderJS 專案

如：
```shell
OJPM --init
```

#### build

編譯 OleanderJS 至 HTML

先 `cd` 至您的專案資料夾，然後執行 `OJPM --build`

將編譯為 /build/app.html

### OJC(OleanderJsCompiler)

編譯 OleanderJS 至 HTML

如：
```shell
OJC init.yh
```

將編譯為 init.html

## 注意
* 本教程適用於 OleanderJS-API V1.13.0 版
