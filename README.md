# Oleander TS文档

其实本语言是Oleander+JS+OleanderUI，但是作者本来想用Oleander+TS+OleanderUI。所以叫“Oleander TS”

[繁體中文](https://github.com/M720111120126/OleanderTS/blob/master/README-TraditionalChinese.md) [English](https://github.com/M720111120126/OleanderTS/blob/master/README-English.md)

---

## 语法

### Oleander部分

Oleander部分只为Oleander TS带来了预处理和JS调用特性

#### 预处理

预处理指令以 `#` 开头，在编译时会进行展开。

##### `#include "file"`

```scl
#include preprocess_test.yh
// → 直接将文件内容复制到此处
```
注意：

1.此处的file为页面代码的相对目录，如 ./entry/init.yh 使用 #include preprocess_test.yh 填充的是 ./entry/preprocess_test.yh

2.include的所有东西，都必须在 app.json5 的 page 对应页面的 dependencies 中写好名称 如：
```json5
{
  "page": [// 页面表
    {
      "name": "init",// 页面名称
      "srcPath": "./entry",// 页面位置（相对路径）
      "dependencies": [
        "preprocess_test.yh"// 填入名称
      ]// 依赖库表
    }
  ]
}
```

##### `#define value key`

一个替换

```Oleander TS
# 例如这里的代码正常工作
#define + left

1 left 1
```

##### `# UI_start`

Oleander UI部分的开启标志

```Oleander TS
#include ……
#define ……
一些JS代码

# UI_start

这里应该写Oleander UI代码了
```

#### JS调用

见上面的 # UI_start 的示例，js直接写在 Oleander部分 就可以执行了

### Oleander UI部分

本文档介绍了如何使用提供的 UI 组件，帮助你快速创建和渲染界面。文档将通过详细的示例，帮助你理解如何构建交互式和响应式 UI。

### 0. Oleander UI 语法

#### 布局组件

使用 `布局组件名称() {}` 请注意，属性（css属性）的设置需要尾随逗号

```Oleander TS
布局组件名称() {
  属性: 值,
  包含的组件
}
```

#### 基础组件

使用 `基础组件名称(传入的内容)` 或 `基础组件名称() {内容}`

##### `基础组件名称(传入的内容)`

```Oleander TS
Button(1)
```

##### `基础组件名称() {内容}`

请注意尾随逗号

`{}` 中使用 `data_` 前缀更改属性，使用 `method_` 前缀调用方法

```Oleander TS
Button() {
  data_text : "1",
  method_set_on_click: "alert('按钮1被点击')",
  }
```

#### 条件渲染
```Oleander TS
if(条件) {
  条件渲染的组件
}
```

#### 循环渲染
```Oleander TS
x() {
  data_text : "${item}",
  method_for_render: "[1,2,3]"
}
```
这样就会渲染三个“x”，并显示为 1、2、3。任何需要调用list（如这里的 `[1,2,3]`）的内容的地方都可以使用 `${item}`

#### 示例：
```Oleander TS
Row() {
  "background" : "lightblue",
  "padding" : "20px",
  Column() {
    "margin" : "20px",
    "padding" : "10px",
    Button() {
      data_text : "1",
      data_on_click: "alert('按钮1被点击')",
    }
  }
  Column() {
    "margin" : "20px",
    "padding" : "10px",
    Button() {
      data_text : "3",
      data_on_click: "alert('按钮3被点击')",
    }
    if(isDaytime) {
      Button() {
        data_text : "2-白天才能看见的按钮",
        data_on_click: "alert('按钮2被点击')"
      }
    }
    if(!isDaytime) {
      Button() {
        data_text : "2-晚上才能看见的按钮",
        data_on_click: "alert('按钮2被点击')"
      }
    }
  }
}
```

### 1. 基础组件

这些基础组件是 UI 构建的核心，可以通过组合和定制这些组件来构建你的界面。

#### 1.1 `UIComponent` 类
所有 UI 组件都继承自 `UIComponent` 类。该类包含常见的样式和子组件管理功能。

##### 方法：
- `set_style(**kwargs)`：设置样式，支持传入多个 CSS 属性和值。
- `render()`：渲染该组件并返回 HTML。

#### 1.2 `Button` 类

按钮组件，允许用户创建可点击的按钮。

##### 方法：
- `set_on_click(callback)`：设置按钮的点击事件，可以传入 JavaScript 代码或回调函数。（依赖于on_click属性）

##### 属性：
- `text`：显示的文本
- `on_click`：设置按钮的点击事件，可以传入 JavaScript 代码或回调函数。

#### 1.3 `Radio` 类

单选框组件，允许用户在多个选项中选择一个。

##### 方法

- `set_checked(True)`：是否默认选中

#### 1.4 `Toggle` 类

切换按钮组件，可以在两种状态（如开启/关闭）之间切换。

##### 方法

- `set_checked(True)`：是否默认选中

##### 属性

- `label_on`：开启时显示的文本
- `label_off`：关闭时显示的文本on style="background: lightgreen; padding: 10px;">开启</button>

#### 1.5 `Progress` 类

进度条组件，用于显示任务的完成进度。

##### 属性

- `value`：进度

#### 1.6 `Image` 类

图片组件，用于在界面中嵌入图片。

##### 属性

- `src`：图片地址

### 2. 布局组件

布局组件用来控制多个子组件的排版。你可以使用 `Row` 或 `Column` 类来组织组件。

#### 2.1 `Row` 类

行布局，子组件按水平方向排列。

#### 2.2 `Column` 类

列布局，子组件按垂直方向排列。

### 3. 交互组件

交互组件如 `Dialog` 和 `Menu` 可以帮助你创建包含交互式内容的弹窗和导航菜单。

#### 3.1 `Dialog` 类

对话框组件，用于显示消息或内容。

##### 属性

- `title`：标题
- `content`：内容

#### 3.2 `Menu` 类

菜单组件，用于创建可点击的列表项。

##### 方法

- `add_item`：添加列表项

### 4. 高级用法

#### 4.1 条件渲染（全部组件可使用的方法）

可以判断条件并决定是否渲染

##### 示例
```Oleander TS
Button() {
  data_text : "2-白天才能看见的按钮",
  data_on_click: "alert('按钮2被点击')",
  method_condition: "isDaytime"
}
```

注意：isDaytime函数已经在 Oleander 部分使用JS定义过了，白天返回true，晚上返回false

白天能看见button，晚上再打开就看不见了

#### 4.2 页面调用

可以通过设置组件的属性来嵌入其他的页面

##### 属性

- `src`：页面名称
- `width`：嵌入宽度
- `height`：嵌入高度

##### 示例：
```Oleander TS
iframe = Iframe(src="pay", width="800", height="600")
iframe.set_style(border="2px solid black")
html = button.render() + iframe.render() + auto_js_code
```

#### 4.3 组合复杂布局

你可以通过将多个布局组件（如 `Row` 和 `Column`）嵌套在一起，创建复杂的布局。

##### 示例：
```Oleander TS
Row() {
  "background" : "lightblue",
  "padding" : "20px",
  Column() {
    "margin" : "20px",
    "padding" : "10px",
    Button() {
      data_text : "1",
      data_on_click: "alert('按钮1被点击')",
    }
  }
  Column() {
    "margin" : "20px",
    "padding" : "10px",
    Button() {
      data_text : "3",
      data_on_click: "alert('按钮3被点击')",
    }
    Button() {
      data_text : "2-白天才能看见的按钮",
      data_on_click: "alert('按钮2被点击')",
      method_condition: "isDaytime"
    }
    Button() {
      data_text : "2-晚上才能看见的按钮",
      data_on_click: "alert('按钮2被点击')",
      method_condition: "!isDaytime"
    }
  }
}
```

---

## 编译

```file
└─ init
└─── init.yh
└─ app.json5
└─ build.json5
```

### app.json5

```json5
{
  "page": [// 页面表
    {
      "name": "init",// 页面名称
      "srcPath": "./entry",// 页面位置（相对路径）
      "dependencies": []// 依赖库表
    }
  ]
}
```

### app.json5

```json5
{
  "Minimum-required-API-version": "0.1.0",// 最低兼容的API版本，必须
  "Target-API-version": "0.1.0",// 目标的API版本，必须
  "name": "demo",// 项目名及模块 root 包名，必需
  "version": "1.0.0",// 模块版本信息，必需
  "compile-option": ""// 额外编译命令选项，非必需
}
```

### 编译方式

先 cd 至OleanderTS项目文件夹

直接执行 main.py

将编译为 app.html

注意：
* 本教程适用于 OleanderTS-API V0.4.8 Beta3 版