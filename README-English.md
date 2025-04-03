## This tutorial uses machine translation, which may be somewhat inaccurate.

# Oleander TS Documentation

The language is Oleander+JS+OleanderUI, but the author wanted to use Oleander+TS+OleanderUI, so it's called "Oleander TS".

[简体中文](https://github.com/M720111120126/OleanderTS/blob/master/README.md) [繁體中文](https://github.com/M720111120126/OleanderTS/blob/master/README-TraditionalChinese.md)

---

## grammatical

### Oleander section

The Oleander section only brings preprocessing and JS call features to Oleander TS

#### 

The preprocessing instructions begin with`#`header, which will be expanded at compile time.

##### `#include "file"`

```scl
#include preprocess_test.yh
// → 直接将文件内容复制到此处
```
Attention:

1. The file here is the relative directory of the page code, such as ./entry/init.yh using #include preprocess_test.yh filled with ./entry/preprocess_test.yh

2. All things included must be written in the dependencies of the page corresponding to the app.json5 page, such as:
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

A replacement

```Oleander TS
# 例如这里的代码正常工作
#define + left

1 left 1
```

##### `# UI_start`

Oleander UI part of the on sign

```Oleander TS
#include ……
#define ……
一些JS代码

# UI_start

这里应该写Oleander UI代码了
```

#### JS calls

See the # UI_start example above, the js is written directly in the Oleander section and is ready to be executed

### Oleander UI section

This document describes how to use the provided UI components to help you quickly create and render interfaces.The document will help you understand how to build interactive and responsive UI with detailed examples.

### 1. Basic components

These basic components are the core of UI construction and can be combined and customized to build your interface.

#### 1.1 `UIComponent`resemble
All UI components inherit from the`UIComponent`class, which contains common style and subcomponent management features.

##### Methods:
- `set_style(**kwargs)`: Sets styles and supports passing in multiple CSS properties and values.
- `add_child(child)`: Adds the child component to the current component.
- `render()`: Renders the component and returns the HTML.

#### 1.2 `Button`resemble

Button component that allows users to create clickable buttons.

##### Methods:
- `set_on_click(callback)`: Set the button's click event, either by passing in JavaScript code or a callback function.

##### Example:
```Oleander TS
button = Button("点击我")
button.set_on_click("alert('按钮被点击')")
button.set_style(color="white", background="blue", padding="10px")
html = button.render()
```

Output:
```html
<button style="color: white; background: blue; padding: 10px;" onclick="alert('按钮被点击')">点击我</button>
```

#### 1.3 `Radio`resemble

A radio box component that allows the user to select one of several options.

##### Example:
```Oleander TS
radio1 = Radio("group1", "选项1").set_checked(True)
radio2 = Radio("group1", "选项2")
radio1.set_style(margin="10px")
radio2.set_style(margin="10px")
html = radio1.render() + radio2.render()
```

Output:
```html
<input type="radio" name="group1" value="选项1" checked style="margin: 10px"/>
<input type="radio" name="group1" value="选项2" style="margin: 10px"/>
```

#### 1.4 `Toggle`resemble



##### 
```Oleander TS
toggle = Toggle("开启", "关闭")
toggle.set_checked(True)
toggle.set_style(background="lightgreen", padding="10px")
html = toggle.render()
```

Output:
```html
<button style="background: lightgreen; padding: 10px;">开启</button>
```

#### 1.5 `Progress`resemble

Progress bar component that displays the progress of the task completion.

##### Example:
```Oleander TS
progress = Progress(50)
progress.set_style(width="100%", height="20px", background="lightgray")
html = progress.render()
```

Output:
```html
<progress value="50" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
```

#### 1.6 `Image`resemble

Image component for embedding images in the interface.

##### Example:
```Oleander TS
image = Image("https://example.com/image.jpg")
image.set_style(width="200px", height="auto")
html = image.render()
```

Output:
```html
<img src="https://example.com/image.jpg" style="width: 200px; height: auto"/>
```



### 2. Layout components

The layout component is used to control the layout of multiple subcomponents. you can use the`Row`maybe`Column`class to organize components.

#### 2.1 `Row`resemble

Row layout with subcomponents arranged horizontally.

##### Example:
```Oleander TS
row = Row()
row.add_child(button).add_child(progress).add_child(image)
row.set_style(background="lightblue", padding="20px")
html = row.render()
```

Output:
```html
<div style="display: flex; background: lightblue; padding: 20px;">
    <button style="color: white; background: blue; padding: 10px;" onclick="alert('按钮被点击')">点击我</button>
    <progress value="50" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
    <img src="https://example.com/image.jpg" style="width: 200px; height: auto"/>
</div>
```

#### 2.2 `Column`resemble

Column layout with subcomponents arranged vertically.

##### Example:
```Oleander TS
column = Column()
column.add_child(dialog).add_child(menu)
column.set_style(margin="20px", padding="10px")
html = column.render()
```

Output:
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



### 3. Interactive components

interactive component such as`Dialog`cap (a poem)`Menu`Can help you create popups and navigation menus that contain interactive content.

#### 3.1 `Dialog`resemble



##### Example:
```Oleander TS
dialog = Dialog("欢迎", "这是一个简单的对话框")
dialog.set_style(border="1px solid #ccc", padding="10px", background="#f9f9f9")
html = dialog.render()
```

Output:
```html
<div class="dialog" style="border: 1px solid #ccc; padding: 10px; background: #f9f9f9;">
    <h1>欢迎</h1>
    <p>这是一个简单的对话框</p>
</div>
```

#### 3.2 `Menu`resemble

Menu component for creating clickable list items.

##### Example:
```Oleander TS
menu = Menu()
menu.add_item("菜单项1").add_item("菜单项2").add_item("菜单项3")
menu.set_style(list_style_type="none", padding="0", margin="0")
html = menu.render()
```

Output:
```html
<ul style="list-style-type: none; padding: 0; margin: 0;">
    <li>菜单项1</li>
    <li>菜单项2</li>
    <li>菜单项3</li>
</ul>
```

### 4. Advanced usage

#### 4.1 Conditional Rendering

Can judge conditions and decide whether to render

##### typical example
```Oleander TS
button = Button("3")
button.set_on_click("alert('按钮3被点击')")
button.set_style(color="white", background="blue", padding="10px")
button.condition("isDaytime")
html = button.render() + iframe.render()
```



You can see the button during the day, but not when you open it at night.

#### 4.2 Page Call

You can call other pages by setting the component's properties.

##### Example:
```Oleander TS
iframe = Iframe(src="pay", width="800", height="600")
iframe.set_style(border="2px solid black")
html = button.render() + iframe.render() + auto_js_code
```

Output:
```html
<iframe width="800" height="600" style="border: 2px solid black;">您名称为pay的页面的编译结果</iframe>
```

#### 4.3 Dynamic updating

You can dynamically update the state of a component by setting its properties, such as updating the value of a progress bar, the state of a toggle button, etc. You just need to call the corresponding`set_*`method and re-renders the component.

##### 
```Oleander TS
progress.set_value(75)
html = progress.render()
```

Output:
```html
<progress value="75" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
```

#### 

`Row`cap (a poem)`Column`) nested together to create complex layouts.

##### Example:
```Oleander TS
row = Row()
row.add_child(button).add_child(progress)

column = Column()
column.add_child(row).add_child(dialog)

html = column.render()
```

Output:
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

## compiling

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

### Compilation method

First cd to the OleanderTS project folder

Execute main.py directly

will compile to app.html

Attention:
* This tutorial applies to OleanderTS-API V0.2.4 alpha version
* The HTML compiled output in this tutorial is for reference only and is sometimes modified and not synchronized to the tutorial.