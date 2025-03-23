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

### 1. 基础组件

这些基础组件是 UI 构建的核心，可以通过组合和定制这些组件来构建你的界面。

#### 1.1 `UIComponent` 类
所有 UI 组件都继承自 `UIComponent` 类。该类包含常见的样式和子组件管理功能。

##### 方法：
- `set_style(**kwargs)`：设置样式，支持传入多个 CSS 属性和值。
- `add_child(child)`：将子组件添加到当前组件中。
- `render()`：渲染该组件并返回 HTML。

#### 1.2 `Button` 类

按钮组件，允许用户创建可点击的按钮。

##### 方法：
- `set_on_click(callback)`：设置按钮的点击事件，可以传入 JavaScript 代码或回调函数。

##### 示例：
```Oleander TS
button = Button("点击我")
button.set_on_click("alert('按钮被点击')")
button.set_style(color="white", background="blue", padding="10px")
html = button.render()
```

输出：
```html
<button style="color: white; background: blue; padding: 10px;" onclick="alert('按钮被点击')">点击我</button>
```

#### 1.3 `Radio` 类

单选框组件，允许用户在多个选项中选择一个。

##### 示例：
```Oleander TS
radio1 = Radio("group1", "选项1").set_checked(True)
radio2 = Radio("group1", "选项2")
radio1.set_style(margin="10px")
radio2.set_style(margin="10px")
html = radio1.render() + radio2.render()
```

输出：
```html
<input type="radio" name="group1" value="选项1" checked style="margin: 10px"/>
<input type="radio" name="group1" value="选项2" style="margin: 10px"/>
```

#### 1.4 `Toggle` 类

切换按钮组件，可以在两种状态（如开启/关闭）之间切换。

##### 示例：
```Oleander TS
toggle = Toggle("开启", "关闭")
toggle.set_checked(True)
toggle.set_style(background="lightgreen", padding="10px")
html = toggle.render()
```

输出：
```html
<button style="background: lightgreen; padding: 10px;">开启</button>
```

#### 1.5 `Progress` 类

进度条组件，用于显示任务的完成进度。

##### 示例：
```Oleander TS
progress = Progress(50)
progress.set_style(width="100%", height="20px", background="lightgray")
html = progress.render()
```

输出：
```html
<progress value="50" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
```

#### 1.6 `Image` 类

图片组件，用于在界面中嵌入图片。

##### 示例：
```Oleander TS
image = Image("https://example.com/image.jpg")
image.set_style(width="200px", height="auto")
html = image.render()
```

输出：
```html
<img src="https://example.com/image.jpg" style="width: 200px; height: auto"/>
```



### 2. 布局组件

布局组件用来控制多个子组件的排版。你可以使用 `Row` 或 `Column` 类来组织组件。

#### 2.1 `Row` 类

行布局，子组件按水平方向排列。

##### 示例：
```Oleander TS
row = Row()
row.add_child(button).add_child(progress).add_child(image)
row.set_style(background="lightblue", padding="20px")
html = row.render()
```

输出：
```html
<div style="display: flex; background: lightblue; padding: 20px;">
    <button style="color: white; background: blue; padding: 10px;" onclick="alert('按钮被点击')">点击我</button>
    <progress value="50" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
    <img src="https://example.com/image.jpg" style="width: 200px; height: auto"/>
</div>
```

#### 2.2 `Column` 类

列布局，子组件按垂直方向排列。

##### 示例：
```Oleander TS
column = Column()
column.add_child(dialog).add_child(menu)
column.set_style(margin="20px", padding="10px")
html = column.render()
```

输出：
```html
<div style="display: block; margin: 20px; padding: 10px;">
    <div class="dialog" style="border: 1px solid #ccc; padding: 10px; background: #f9f9f9;">
        <h1>欢迎</h1>
        <p>这是一个简单的对话框</p>
    </div>
    <ul style="list-style-type: none; padding: 0; margin: 0;">
        <li>菜单项1</li>
        <li>菜单项2</li>
        <li>菜单项3</li>
    </ul>
</div>
```



### 3. 交互组件

交互组件如 `Dialog` 和 `Menu` 可以帮助你创建包含交互式内容的弹窗和导航菜单。

#### 3.1 `Dialog` 类

对话框组件，用于显示消息或内容。

##### 示例：
```Oleander TS
dialog = Dialog("欢迎", "这是一个简单的对话框")
dialog.set_style(border="1px solid #ccc", padding="10px", background="#f9f9f9")
html = dialog.render()
```

输出：
```html
<div class="dialog" style="border: 1px solid #ccc; padding: 10px; background: #f9f9f9;">
    <h1>欢迎</h1>
    <p>这是一个简单的对话框</p>
</div>
```

#### 3.2 `Menu` 类

菜单组件，用于创建可点击的列表项。

##### 示例：
```Oleander TS
menu = Menu()
menu.add_item("菜单项1").add_item("菜单项2").add_item("菜单项3")
menu.set_style(list_style_type="none", padding="0", margin="0")
html = menu.render()
```

输出：
```html
<ul style="list-style-type: none; padding: 0; margin: 0;">
    <li>菜单项1</li>
    <li>菜单项2</li>
    <li>菜单项3</li>
</ul>
```

### 4. 高级用法

#### 4.1 条件渲染

可以判断条件并决定是否渲染

##### 示例
```Oleander TS
button = Button("3")
button.set_on_click("alert('按钮3被点击')")
button.set_style(color="white", background="blue", padding="10px")
button.if_render("isDaytime")
html = button.render() + iframe.render()
```

注意：isDaytime函数已经在 Oleander 部分使用JS定义过了，白天返回true，晚上返回false

白天能看见button，晚上再打开就看不见了

#### 4.2 页面调用

可以通过设置组件的属性来调用其他的页面

##### 示例：
```Oleander TS
iframe = Iframe(src="pay", width="800", height="600")
iframe.set_style(border="2px solid black")
html = button.render() + iframe.render() + auto_js_code
```

输出：
```html
<iframe width="800" height="600" style="border: 2px solid black;">您名称为pay的页面的编译结果</iframe>
```

#### 4.3 动态更新

可以通过设置组件的属性来动态更新组件的状态，例如更新进度条的值、切换按钮的状态等。你只需要调用相应的 `set_*` 方法，并重新渲染该组件。

##### 示例：
```Oleander TS
progress.set_value(75)
html = progress.render()
```

输出：
```html
<progress value="75" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
```

#### 4.4 组合复杂布局

你可以通过将多个布局组件（如 `Row` 和 `Column`）嵌套在一起，创建复杂的布局。

##### 示例：
```Oleander TS
row = Row()
row.add_child(button).add_child(progress)

column = Column()
column.add_child(row).add_child(dialog)

html = column.render()
```

输出：
```html
<div style="display: block; margin: 20px; padding: 10px;">
    <div style="display: flex; background: lightblue; padding: 20px;">
        <button style="color: white; background: blue; padding: 10px;" onclick="alert('按钮被点击')">点击我</button>
        <progress value="50" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
    </div>
    <div class="dialog" style="border: 1px solid #ccc; padding: 10px; background: #f9f9f9;">
        <h1>欢迎</h1>
        <p>这是一个简单的对话框</p>
    </div>
</div>
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
* 本教程适用于 OleanderTS-API V0.2.4 alpha 版
* 本教程中的 HTML 编译输出仅供参考，有时加以修改未同步至教程