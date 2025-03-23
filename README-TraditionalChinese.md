# Oleander TS文件

其實本語言是Oleander+JS+OleanderUI，但是作者本來想用Oleander+TS+OleanderUI。所以叫“Oleander TS”

[简体中文](https://github.com/M720111120126/OleanderTS/blob/master/README.md) [English](https://github.com/M720111120126/OleanderTS/blob/master/README-English.md)

---

## 語法

### Oleander部分

Oleander部分只為Oleander TS帶來了預處理和JS呼叫特性

#### 預處理

預處理指令以 `#` 開頭，在編譯時會進行展開。

##### `#include "file"`

```scl
#include preprocess_test.yh
// → 直接將檔案內容複製到此處
```
注意：

1.此處的file為頁面程式碼的相對目錄，如 ./entry/init.yh 使用 #include preprocess_test.yh 填充的是 ./entry/preprocess_test.yh

2.include的所有東西，都必須在 app.json5 的 page 對應頁面的 dependencies 中寫好名稱 如：
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

```Oleander TS
# 例如這裡的程式碼正常工作
#define + left

1 left 1
```

##### `# UI_start`

Oleander UI部分的開啟標誌

```Oleander TS
#include ……
#define ……
一些JS程式碼

# UI_start

這裡應該寫Oleander UI程式碼了
```

#### JS呼叫

見上面的 # UI_start 的示例，js直接寫在 Oleander部分 就可以執行了

### Oleander UI部分

本文件介紹瞭如何使用提供的 UI 元件，幫助你快速建立和渲染介面。文件將透過詳細的示例，幫助你理解如何構建互動式和響應式 UI。

### 1. 基礎元件

這些基礎元件是 UI 構建的核心，可以透過組合和定製這些元件來構建你的介面。

#### 1.1 `UIComponent` 類
所有 UI 元件都繼承自 `UIComponent` 類。該類包含常見的樣式和子元件管理功能。

##### 方法：
- `set_style(**kwargs)`：設定樣式，支援傳入多個 CSS 屬性和值。
- `add_child(child)`：將子元件新增到當前元件中。
- `render()`：渲染該元件並返回 HTML。

#### 1.2 `Button` 類

按鈕元件，允許使用者建立可點選的按鈕。

##### 方法：
- `set_on_click(callback)`：設定按鈕的點選事件，可以傳入 JavaScript 程式碼或回撥函式。

##### 示例：
```Oleander TS
button = Button("點選我")
button.set_on_click("alert('按鈕被點選')")
button.set_style(color="white", background="blue", padding="10px")
html = button.render()
```

輸出：
```html
<button style="color: white; background: blue; padding: 10px;" onclick="alert('按鈕被點選')">點選我</button>
```

#### 1.3 `Radio` 類

單選框元件，允許使用者在多個選項中選擇一個。

##### 示例：
```Oleander TS
radio1 = Radio("group1", "選項1").set_checked(True)
radio2 = Radio("group1", "選項2")
radio1.set_style(margin="10px")
radio2.set_style(margin="10px")
html = radio1.render() + radio2.render()
```

輸出：
```html
<input type="radio" name="group1" value="選項1" checked style="margin: 10px"/>
<input type="radio" name="group1" value="選項2" style="margin: 10px"/>
```

#### 1.4 `Toggle` 類

切換按鈕元件，可以在兩種狀態（如開啟/關閉）之間切換。

##### 示例：
```Oleander TS
toggle = Toggle("開啟", "關閉")
toggle.set_checked(True)
toggle.set_style(background="lightgreen", padding="10px")
html = toggle.render()
```

輸出：
```html
<button style="background: lightgreen; padding: 10px;">開啟</button>
```

#### 1.5 `Progress` 類

進度條元件，用於顯示任務的完成進度。

##### 示例：
```Oleander TS
progress = Progress(50)
progress.set_style(width="100%", height="20px", background="lightgray")
html = progress.render()
```

輸出：
```html
<progress value="50" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
```

#### 1.6 `Image` 類

圖片元件，用於在介面中嵌入圖片。

##### 示例：
```Oleander TS
image = Image("https://example.com/image.jpg")
image.set_style(width="200px", height="auto")
html = image.render()
```

輸出：
```html
<img src="https://example.com/image.jpg" style="width: 200px; height: auto"/>
```



### 2. 佈局元件

佈局元件用來控制多個子元件的排版。你可以使用 `Row` 或 `Column` 類來組織元件。

#### 2.1 `Row` 類

行佈局，子元件按水平方向排列。

##### 示例：
```Oleander TS
row = Row()
row.add_child(button).add_child(progress).add_child(image)
row.set_style(background="lightblue", padding="20px")
html = row.render()
```

輸出：
```html
<div style="display: flex; background: lightblue; padding: 20px;">
    <button style="color: white; background: blue; padding: 10px;" onclick="alert('按鈕被點選')">點選我</button>
    <progress value="50" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
    <img src="https://example.com/image.jpg" style="width: 200px; height: auto"/>
</div>
```

#### 2.2 `Column` 類

列布局，子元件按垂直方向排列。

##### 示例：
```Oleander TS
column = Column()
column.add_child(dialog).add_child(menu)
column.set_style(margin="20px", padding="10px")
html = column.render()
```

輸出：
```html
<div style="display: block; margin: 20px; padding: 10px;">
    <div class="dialog" style="border: 1px solid #ccc; padding: 10px; background: #f9f9f9;">
        <h1>歡迎</h1>
        <p>這是一個簡單的對話方塊</p>
    </div>
    <ul style="list-style-type: none; padding: 0; margin: 0;">
        <li>選單項1</li>
        <li>選單項2</li>
        <li>選單項3</li>
    </ul>
</div>
```



### 3. 互動元件

互動元件如 `Dialog` 和 `Menu` 可以幫助你建立包含互動式內容的彈窗和導航選單。

#### 3.1 `Dialog` 類

對話方塊元件，用於顯示訊息或內容。

##### 示例：
```Oleander TS
dialog = Dialog("歡迎", "這是一個簡單的對話方塊")
dialog.set_style(border="1px solid #ccc", padding="10px", background="#f9f9f9")
html = dialog.render()
```

輸出：
```html
<div class="dialog" style="border: 1px solid #ccc; padding: 10px; background: #f9f9f9;">
    <h1>歡迎</h1>
    <p>這是一個簡單的對話方塊</p>
</div>
```

#### 3.2 `Menu` 類

選單元件，用於建立可點選的列表項。

##### 示例：
```Oleander TS
menu = Menu()
menu.add_item("選單項1").add_item("選單項2").add_item("選單項3")
menu.set_style(list_style_type="none", padding="0", margin="0")
html = menu.render()
```

輸出：
```html
<ul style="list-style-type: none; padding: 0; margin: 0;">
    <li>選單項1</li>
    <li>選單項2</li>
    <li>選單項3</li>
</ul>
```

### 4. 高階用法

#### 4.1 條件渲染

可以判斷條件並決定是否渲染

##### 示例
```Oleander TS
button = Button("3")
button.set_on_click("alert('按鈕3被點選')")
button.set_style(color="white", background="blue", padding="10px")
button.if_render("isDaytime")
html = button.render() + iframe.render()
```

注意：isDaytime函式已經在 Oleander 部分使用JS定義過了，白天返回true，晚上返回false

白天能看見button，晚上再開啟就看不見了

#### 4.2 頁面呼叫

可以透過設定元件的屬性來呼叫其他的頁面

##### 示例：
```Oleander TS
iframe = Iframe(src="pay", width="800", height="600")
iframe.set_style(border="2px solid black")
html = button.render() + iframe.render() + auto_js_code
```

輸出：
```html
<iframe width="800" height="600" style="border: 2px solid black;">您名稱為pay的頁面的編譯結果</iframe>
```

#### 4.3 動態更新

可以透過設定元件的屬性來動態更新元件的狀態，例如更新進度條的值、切換按鈕的狀態等。你只需要呼叫相應的 `set_*` 方法，並重新渲染該元件。

##### 示例：
```Oleander TS
progress.set_value(75)
html = progress.render()
```

輸出：
```html
<progress value="75" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
```

#### 4.4 組合複雜佈局

你可以透過將多個佈局元件（如 `Row` 和 `Column`）巢狀在一起，建立複雜的佈局。

##### 示例：
```Oleander TS
row = Row()
row.add_child(button).add_child(progress)

column = Column()
column.add_child(row).add_child(dialog)

html = column.render()
```

輸出：
```html
<div style="display: block; margin: 20px; padding: 10px;">
    <div style="display: flex; background: lightblue; padding: 20px;">
        <button style="color: white; background: blue; padding: 10px;" onclick="alert('按鈕被點選')">點選我</button>
        <progress value="50" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
    </div>
    <div class="dialog" style="border: 1px solid #ccc; padding: 10px; background: #f9f9f9;">
        <h1>歡迎</h1>
        <p>這是一個簡單的對話方塊</p>
    </div>
</div>
```

---

## 編譯

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
      "srcPath": "./entry",// 頁面位置（相對路徑）
      "dependencies": []// 依賴庫表
    }
  ]
}
```

### app.json5

```json5
{
  "Minimum-required-API-version": "0.1.0",// 最低相容的API版本，必須
  "Target-API-version": "0.1.0",// 目標的API版本，必須
  "name": "demo",// 專案名及模組 root 包名，必需
  "version": "1.0.0",// 模組版本資訊，必需
  "compile-option": ""// 額外編譯命令選項，非必需
}
```

### 編譯方式

先 cd 至OleanderTS專案資料夾

直接執行 main.py

將編譯為 app.html

注意：
* 本教程適用於 OleanderTS-API V0.2.4 alpha 版
* 本教程中的 HTML 編譯輸出僅供參考，有時加以修改未同步至教程