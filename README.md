# OleanderJS文档

[繁體中文](https://github.com/M720111120126/OleanderJS/blob/master/README-TraditionalChinese.md) [English](https://github.com/M720111120126/OleanderJS/blob/master/README-English.md)

---

## 语法

### Oleander部分

Oleander部分只为OleanderJS带来了预处理和JS调用特性

#### 注意事项

##### 变量

变量必须以字母开头，只能有字母和下划线。

#### 预处理

预处理指令以 `#` 开头，在编译时会进行展开。

##### `#include file`

```OleanderJS
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

##### `#include 依赖库`

可用的标准库

* [data](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/data.md)
* [router](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/router.md)
* [std](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/std.md)

##### `#define value key`

一个替换

```OleanderJS
# 例如这里的代码正常工作
#define + left

1 left 1
```

##### `# UI_start`

Oleander UI部分的开启标志

```OleanderJS
#include ……
#define ……
一些JS代码

# UI_start

这里应该写Oleander UI代码了
```

#### JS调用

见上面的 # UI_start 的示例，js直接写在 Oleander部分 就可以执行了

#### 权限管理

##### 权限列表

* [`com.oleander.file` 获取一个属于该app的文件空间](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/com.oleander.file.md)
* [`con.oleander.os.file` 获取所有OleanderAPP共用的文件空间](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/com.oleander.os.file.md)
* [`com.oleander.JMS` JZH账号支持（仅提供简体中文文档，不建议国外使用）](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/com.oleander.os.jms.md)

请注意：请求权限失败不会抛出异常，在获取权限后应当检查`rights_name_json`这个list内有没有请求的权限

##### 权限获取方式-静态获取

这将会在app启动的时候向用户请求权限。

在 `app.json5` 中定义。

```json5
{
  ...
  "APP_Scope": {// 软件配置
    ...
    "require":[// APP需要调用的权限
      "com.oleander.file"
    ]
  }
}
```

##### 权限获取方式-动态获取

这将会在app运行至导入的地方的时候向用户请求权限。

使用 `#include` 导入

```OleanderJS
#include com.oleander.file
```

### Oleander UI部分

本文档介绍了如何使用提供的 UI 组件，帮助你快速创建和渲染界面。文档将通过详细的示例，帮助你理解如何构建交互式和响应式 UI。

### 0. Oleander UI 语法

#### 布局组件

使用 `布局组件名称() {}` 请注意，属性（css属性）的设置需要尾随逗号

```OleanderJS
布局组件名称() {
  包含的组件
}
.style(属性=值)
```

#### 基础组件

##### OleanderUI-ArkPRO框架（更推荐）

请注意尾随逗号

使用 `.SA("x",y)` 更改属性，使用 `.x(y)` 调用方法

```OleanderJS
Button()
.SA("text", "1")
.set_on_click("alert('按钮1被点击')")
```

更改属性的特殊方式支持通过 `组件名称(属性)` 的方法更改属性，这种方法叫做 `DCA`

比如上面的例子就可以写成

```OleanderJS
Button("1")
.set_on_click("alert('按钮1被点击')")
```

#### 条件渲染
```OleanderJS
if("条件") {
  条件渲染的组件
}
```

#### 循环渲染
```OleanderJS
x() {}
.text = "${item}"
.for_render("[1,2,3]")
```
这样就会渲染三个“x”，并显示为 1、2、3。任何需要调用list（如这里的 `[1,2,3]`）的内容的地方都可以使用 `${item}`

#### 示例：

见项目 `/ProjectExample-ark` 文件夹

##### OleanderUI-object框架（更强大）

类似于 python 的对象

使用 `对象.属性=内容` 前缀更改属性，使用 `对象.方法(内容)` 前缀调用方法

```OleanderJS
Button = Button()
Button.text = "1"
Button.on_click = "alert('按钮1被点击')"
```

#### 条件渲染

使用 `condition` 方法

```OleanderJS
对象.condition("js返回bool的表达式")
```

#### 循环渲染

使用 `for_render` 方法

```OleanderJS
对象.for_render(第一项,第二项...)
```
这样就会渲染三个“对象”，并显示为 1、2...。任何需要调用list（如这里的 `[1,2...]`）的内容的地方都可以使用 `${item}`

#### 示例：

见项目 `/ProjectExample-object` 文件夹

### 1. 基础组件

这些基础组件是 UI 构建的核心，可以通过组合和定制这些组件来构建你的界面。

#### 1.1 `UIComponent` 类
所有 UI 组件都继承自 `UIComponent` 类。该类包含常见的样式和子组件管理功能。

##### 方法：
- `set_style(**kwargs)`：设置样式，支持传入多个 CSS 属性和值。
- `render()`：渲染该组件并返回 HTML。

##### 特性
- `text属性`：可以使用`js_`前缀以使用在JavaScript中定义的变量作为显示的文本

#### 1.2 `Text` 类

文本组件，允许创建文本。

##### 属性：
- `text`：显示的文本

##### DCA：
`Text(text="", size=1)`

#### 1.3 `Button` 类

按钮组件，允许用户创建可点击的按钮。

##### 方法：
- `set_on_click(callback)`：设置按钮的点击事件，可以传入 JavaScript 代码或回调函数。（依赖于on_click属性）

##### 属性：
- `text`：显示的文本
- `on_click`：设置按钮的点击事件，可以传入 JavaScript 代码或回调函数。

##### DCA：
`Button(text="")`

#### 1.4 `Radio` 类

单选框组件，允许用户在多个选项中选择一个。

##### 方法:
- `set_checked(True)`：是否默认选中

##### DCA：
`Radio(name="", value="")`

#### 1.5 `Toggle` 类

切换按钮组件，可以在两种状态（如开启/关闭）之间切换。

##### 方法:

- `set_checked(True)`：是否默认选中

##### 属性:

- `label_on`：开启时显示的文本
- `label_off`：关闭时显示的文本

##### DCA:
`Toggle(label_on="", label_off="")`

#### 1.6 `Progress` 类

进度条组件，用于显示任务的完成进度。

##### 属性：
- `value`：进度

##### DCA：
`Progress(value=0)`

#### 1.7 `Image` 类

图片组件，用于在界面中嵌入图片。

##### 属性：
- `src`：图片地址

##### DCA：
`Image(src="")`

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

##### 属性：
- `title`：标题
- `content`：内容

##### DCA：
`Dialog(title="", content="")`

#### 3.2 `Menu` 类

菜单组件，用于创建可点击的列表项。

##### 方法：
- `add_item`：添加列表项

### 4. 高级用法

#### 4.1 条件渲染（全部组件可使用的方法）

可以判断条件并决定是否渲染

##### 示例
```OleanderJS
Button() {
  data_text : "2-白天才能看见的按钮",
  data_on_click: "alert('按钮2被点击')",
  method_condition: "isDaytime"
}
```

注意：isDaytime函数已经在 Oleander 部分使用JS定义过了，白天返回true，晚上返回false

白天能看见button，晚上再打开就看不见了

#### 4.1 内置调用

内置调用以 `$` 开头

##### $r

获取文件，如 `$r("$media: app_icon.png")` 获取 `APP_Scope/media/app_icon.png` 文件

其中 `$xx` 就代表在 `APP_Scope/xx` 路径下

---

## 编译

配置文件有 `json5` 和 `toml` 两种格式，可以任选一种使用。推荐使用 `toml`。

### 文件结构

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
  "page": [// 页面表
    {
      "name": "init",// 页面名称
      "srcPath": "./init",// 页面位置（相对路径）
      "dependencies": ["dependencies.yh"]// 依赖库表
    },
    {
      "name": "JumpTest",// 页面名称
      "srcPath": "./JumpTest",// 页面位置（相对路径）
      "dependencies": []// 依赖库表
    }
  ],
  "APP_Scope": {// 软件配置
    "icon": "$media: app_icon.png",// 图标，位于 “APP_Scope/media/app_icon.png” $xx 就代表在 “APP_Scope/xx” 路径下
    "name": "DEMO",// 名称
    "lang":"zh_cn",// 语言
    "require":[// APP需要调用的权限
      "com.oleander.file"
    ]
  }
}
```

#### build.json5

```json5
{
  "Minimum-required-API-version": "0.10.9",// 最低兼容的API版本，必需
  "Target-API-version": "0.10.9",// 目标的API版本，必需
  "name": "demo",// 项目名及模块 root 包名，必需
  "version": "1.0.0",// 模块版本信息，必需
  "compile-option": {
    "version": true
  }// 额外编译命令选项，非必需
}
```

### toml

#### app.toml

```toml
[[page]] # 页面表 项1
name = "init" # 页面名称
srcPath = "./init" # 页面位置（相对路径）
dependencies = ["dependencies.yh"] # 依赖库表

[[page]] # 页面表 项2
name = "JumpTest"
srcPath = "./JumpTest"
dependencies = []

[APP_Scope]
icon = "$media: app_icon.png" # 图标，位于 “APP_Scope/media/app_icon.png” $xx 就代表在 “APP_Scope/xx” 路径下
name = "DEMO" # 名称
lang = "zh_cn" # 语言
require = ["com.oleander.file"] # APP需要调用的权限
```

#### build.toml

```toml
Minimum-required-API-version = "1.12.5" # 最低兼容的API版本，必需
Target-API-version = "1.12.6" # 目标的API版本，必需
name = "demo" # 项目名及模块 root 包名，必需
version = "1.0.0" # 模块版本信息，必需

[compile-option] # 额外编译命令选项，非必需(可以空着但不能删除)
version = true
```

### 编译方式

额外编译命令选项 :

```
“--fapi-version API版本” 或 “-fver API版本” 指定 API 版本
“--version” 或 “-v” 获取 API 版本
“--skip-env-check” 或 “-e” 跳过环境检查

也可以在 build.json5 或 build.toml 中指定

[compile-option] # 额外编译命令选项，非必需(可以空着但不能删除)
version = true # 获取 API 版本，使用true或false控制
skip_env_check = true # 跳过环境检查，使用true或false控制
fapi_version = "ArkPRO" # 指定 API 版本，有object和ark两个版本可选

"compile-option": {
  "version": true,// 获取 API 版本，使用true或false控制
  "skip_env_check": true,// 跳过环境检查，使用true或false控制
  "fapi_version": "ArkPRO"// 指定 API 版本，有object和ark两个版本可选
}

```

先 `cd` 至您的项目文件夹

直接执行 main.py

将编译为 app.html

注意：
* 本教程适用于 OleanderJS-API V1.12.6 版