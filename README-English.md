# OleanderJS Documentation

[简体中文](https://github.com/M720111120126/OleanderJS/blob/master/README.md) [繁體中文](https://github.com/M720111120126/OleanderJS/blob/master/README-TraditionalChinese.md)

---

## Syntax

### Oleander Section

The Oleander section only brings preprocessing and JS calling features to OleanderJS.

#### Precautions

##### Variables

Variables must start with a letter and can only contain letters and underscores.

#### Preprocessing

Preprocessing directives start with `#` and are expanded at compile time.

##### `#include file`

```OleanderJS
#include preprocess_test.yh
// → Directly copy the file content here
```
Note:

1.  Here, `file` is the relative directory of the page code, such as `./entry/init.yh`. Using `#include preprocess_test.yh` fills in `./entry/preprocess_test.yh`.

2.  Everything included must have its name written in the `dependencies` of the page corresponding to `app.json5`. For example:
```json5
{
  "page": [// Page table
    {
      "name": "init",// Page name
      "srcPath": "./entry",// Page location (relative path)
      "dependencies": [
        "preprocess_test.yh"// Enter the name
      ]// Dependency library table
    }
  ]
}
```

##### `#include dependency library`

Available standard library:

* [data](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/data_English.md)
* [router](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/router_English.md)
* [std](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/std_English.md)

##### `#define value key`

A replacement

```OleanderJS
# For example, the code here works normally
#define + left

1 left 1
```

##### `# UI_start`

The start flag of the Oleander UI section

```OleanderJS
#include ……
#define ……
Some JS code

# UI_start

Oleander UI code should be written here
```

#### JS Calling

See the example of `# UI_start` above. JS can be executed directly by writing it in the Oleander section.

#### Permission Management

##### Permission List

*   [`com.oleander.file` Get a file space belonging to the app](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/com.oleander.file_English.md)
*   [`con.oleander.os.file` Get the file space shared by all OleanderAPP](https://github.com/M720111120126/OleanderJS/blob/master/library/docs/com.oleander.os.file_English.md)

Please note: Failure to request permission will not throw an exception. After obtaining permission, you should check whether the requested permission is in the `rights_name_json` list.

##### Permission Acquisition Method - Static Acquisition

This will request permission from the user when the app starts.

Defined in `app.json5`.

```json5
{
  ...
  "APP_Scope": {// Software configuration
    ...
    "require":[// Permissions that the APP needs to call
      "com.oleander.file"
    ]
  }
}
```

##### Permission Acquisition Method - Dynamic Acquisition

This will request permission from the user when the app runs to the place where it is imported.

Import using `#include`

```OleanderJS
#include com.oleander.file
```

### Oleander UI Section

This document describes how to use the provided UI components to help you quickly create and render interfaces. The document will help you understand how to build interactive and responsive UIs through detailed examples.

### 0. Oleander UI Syntax

#### Layout Components

Use `LayoutComponentName() {}` Please note that the setting of attributes (CSS attributes) requires a trailing comma.

```OleanderJS
LayoutComponentName() {
  Included components
}
.style(attribute=value)
```

#### Basic Components

##### OleanderUI-ArkPRO Framework (More Recommended)

Please note the trailing comma.

Use `.SA("x",y)` to change attributes, use `.x(y)` to call methods.

```OleanderJS
Button()
.SA("text", "1")
.set_on_click("alert('Button 1 was clicked')")
```

A special way to change attributes supports changing attributes through the `ComponentName(attribute)` method. This method is called `DCA`.

For example, the above example can be written as

```OleanderJS
Button("1")
.set_on_click("alert('Button 1 was clicked')")
```

#### Conditional Rendering
```OleanderJS
if("condition") {
  Components for conditional rendering
}
```

#### Loop Rendering
```OleanderJS
x() {}
.text = "${item}"
.for_render("[1,2,3]")
```
This will render three "x"s and display them as 1, 2, 3. `${item}` can be used anywhere that needs to call a list (such as `[1,2,3]` here).

#### Example:

See the `/ProjectExample-ark` folder in the project.

##### OleanderUI-object Framework (More Powerful)

Similar to Python objects

Use the `object.attribute=content` prefix to change attributes, use the `object.method(content)` prefix to call methods.

```OleanderJS
Button = Button()
Button.text = "1"
Button.on_click = "alert('Button 1 was clicked')"
```

#### Conditional Rendering

Use the `condition` method

```OleanderJS
object.condition("js expression that returns bool")
```

#### Loop Rendering

Use the `for_render` method

```OleanderJS
object.for_render(item1,item2...)
```
This will render three "objects" and display them as 1, 2... `${item}` can be used anywhere that needs to call a list (such as `[1,2...]` here).

#### Example:

See the `/ProjectExample-object` folder in the project.

### 1. Basic Components

These basic components are the core of UI construction. You can build your interface by combining and customizing these components.

#### 1.1 `UIComponent` Class

All UI components inherit from the `UIComponent` class. This class contains common style and subcomponent management functions.

##### Methods:

-   `set_style(**kwargs)`: Set styles, supporting passing in multiple CSS attributes and values.
-   `render()`: Render the component and return HTML.

##### Features

-   `text attribute`: You can use the `js_` prefix to use variables defined in JavaScript as the displayed text.

#### 1.2 `Text` Class

Text component, allows creating text.

##### Attributes:

-   `text`: The text to display

##### DCA:

`Text(text="", size=1)`

#### 1.3 `Button` Class

Button component, allows users to create clickable buttons.

##### Methods:

-   `set_on_click(callback)`: Set the button's click event, you can pass in JavaScript code or a callback function. (Depends on the on_click attribute)

##### Attributes:

-   `text`: The text to display
-   `on_click`: Set the button's click event, you can pass in JavaScript code or a callback function.

##### DCA:

`Button(text="")`

#### 1.4 `Radio` Class

Radio button component, allows users to select one of multiple options.

##### Methods:

-   `set_checked(True)`: Whether to select by default

##### DCA:

`Radio(name="", value="")`

#### 1.5 `Toggle` Class

Toggle button component, can switch between two states (such as on/off).

##### Methods:

-   `set_checked(True)`: Whether to select by default

##### Attributes:

-   `label_on`: The text displayed when turned on
-   `label_off`: The text displayed when turned off

##### DCA:

`Toggle(label_on="", label_off="")`

#### 1.6 `Progress` Class

Progress bar component, used to display the completion progress of a task.

##### Attributes:

-   `value`: Progress

##### DCA:

`Progress(value=0)`

#### 1.7 `Image` Class

Image component, used to embed images in the interface.

##### Attributes:

-   `src`: Image address

##### DCA:

`Image(src="")`

### 2. Layout Components

Layout components are used to control the layout of multiple subcomponents. You can use the `Row` or `Column` class to organize components.

#### 2.1 `Row` Class

Row layout, subcomponents are arranged horizontally.

#### 2.2 `Column` Class

Column layout, subcomponents are arranged vertically.

### 3. Interactive Components

Interactive components such as `Dialog` and `Menu` can help you create pop-up windows and navigation menus containing interactive content.

#### 3.1 `Dialog` Class

Dialog box component, used to display messages or content.

##### Attributes:

-   `title`: Title
-   `content`: Content

##### DCA:

`Dialog(title="", content="")`

#### 3.2 `Menu` Class

Menu component, used to create clickable list items.

##### Methods:

-   `add_item`: Add a list item

### 4. Advanced Usage

#### 4.1 Conditional Rendering (Method Available for All Components)

You can determine the condition and decide whether to render

##### Example
```OleanderJS
Button() {
  data_text : "2-Button that can only be seen during the day",
  data_on_click: "alert('Button 2 was clicked')",
  method_condition: "isDaytime"
}
```

Note: The isDaytime function has already been defined in JS in the Oleander section. It returns true during the day and false at night.

You can see the button during the day, but you can't see it when you open it again at night.

#### 4.1 Built in Call

Built in calls start with '$'

##### $r

Retrieve files, such as `$r("$media: app_icon.png")` Retrieve `APP_Scope/media/app_icon.png` files

Among them, '$xx' represents in the 'APP_Scope/xx' path

---

## Compilation

The configuration files come in two formats: `json5` and `toml`. You can choose either one. `toml` is recommended.

### File Structure

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
  "page": [// Page table
    {
      "name": "init",// Page name
      "srcPath": "./init",// Page location (relative path)
      "dependencies": ["dependencies.yh"]// Dependency library table
    },
    {
      "name": "JumpTest",// Page name
      "srcPath": "./JumpTest",// Page location (relative path)
      "dependencies": []// Dependency library table
    }
  ],
  "APP_Scope": {// Software configuration
    "icon": "$media: app_icon.png",// Icon, located in "APP_Scope/media/app_icon.png" $xx means under the "APP_Scope/xx" path
    "name": "DEMO",// Name
    "lang":"zh_cn",// Language
    "require":[// Permissions that the APP needs to call
      "com.oleander.file"
    ]
  }
}
```

#### build.json5

```json5
{
  "Minimum-required-API-version": "0.10.9",// Minimum compatible API version, required
  "Target-API-version": "0.10.9",// Target API version, required
  "name": "demo",// Project name and module root package name, required
  "version": "1.0.0",// Module version information, required
  "compile-option": {
    "version": true
  }// Additional compilation command options, not required
}
```

### toml

#### app.toml

```toml
[[page]] # Page list Item 1
name = "init" # Page name
srcPath = "./init" # Page location (relative path)
dependencies = ["dependencies.yh"] # Dependency library list

[[page]] # Page list Item 2
name = "JumpTest"
srcPath = "./JumpTest"
dependencies = []

[APP_Scope]
icon = "$media: app_icon.png" # Icon, located at “APP_Scope/media/app_icon.png” $xx represents the path under “APP_Scope/xx”
name = "DEMO" # Name
lang = "zh_cn" # Language
require = ["com.oleander.file"] # Permissions that the APP needs to call
```

#### build.toml

```toml
Minimum-required-API-version = "1.12.5" # Minimum compatible API version, required
Target-API-version = "1.12.6" # Target API version, required
name = "demo" # Project name and module root package name, required
version = "1.0.0" # Module version information, required

[compile-option] # Additional compilation command options, not required (can be empty but cannot be deleted)
version = true
```

### Additional compilation command options

```
“--fapi-version API version” or “-fver API version” Specify the API version
“--version” or “-v” Get the API version
“--skip-env-check” or “-e” Skip environment check
“--verbose” or “-V” Print out the related information of the toolchain dependencies and the commands executed during the compilation process

Can also be specified in build.json5 or build.toml

[compile-option] # Additional compilation command options, not required (can be empty but cannot be deleted)
version = true # Get the API version, use true or false to control
skip_env_check = true # Skip environment check, use true or false to control
fapi_version = "ArkPRO" # Specify the API version, there are two versions available: object and ark
verbose = true # Print out the related information of the toolchain dependencies and the commands executed during the compilation process, use true or false to control

"compile-option": {
  "version": true,// Get the API version, use true or false to control
  "skip_env_check": true,// Skip environment check, use true or false to control
  "fapi_version": "ArkPRO",// Specify the API version, there are two versions available: object and ark
  "verbose": true// Print out the related information of the toolchain dependencies and the commands executed during the compilation process, use true or false to control
}

```

## Command-Line Tool Usage Guide

### OJPM (OleanderJsProjectManager)

#### init

Initializes an OleanderJS project

For example:
```shell
OJPM --init
```

#### build

Compiles OleanderJS to HTML

First `cd` to your project folder, then run `OJPM --build`

Will compile to /build/app.html

### OJC (OleanderJsCompiler)

Compiles OleanderJS to HTML

For example:
```shell
OJC init.yh
```

Will compile to init.html

## Note
* This tutorial is applicable to OleanderJS-API V1.13.0
