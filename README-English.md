# OleanderTS Documentation

In reality, this language is Oleander+JS+OleanderUI, but the author originally wanted to use Oleander+TS+OleanderUI. That's why it's called "OleanderTS".

[简体中文](https://github.com/M720111120126/OleanderTS/blob/master/README.md) [繁體中文](https://github.com/M720111120126/OleanderTS/blob/master/README-TraditionalChinese.md)

---

## Syntax

### Oleander Section

The Oleander section only brings preprocessing and JS calling features to OleanderTS.

#### Precautions

##### Variables

Variables must start with a letter and can only contain letters and underscores.

#### Preprocessing

Preprocessing directives start with `#` and will be expanded at compile time.

##### `#include "file"`

```OleanderTS
#include preprocess_test.yh
// → Directly copy the file content here
```
Note:

1.  Here, `file` is the relative directory of the page code. For example, if `./entry/init.yh` uses `#include preprocess_test.yh`, it will fill in `./entry/preprocess_test.yh`.

2.  All included items must have their names written in the `dependencies` of the page corresponding to `app.json5`. For example:
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

##### `#define value key`

A replacement

```OleanderTS
# For example, the code here works normally
#define + left

1 left 1
```

##### `# UI_start`

The start flag of the Oleander UI section

```OleanderTS
#include ……
#define ……
Some JS code

# UI_start

Oleander UI code should be written here
```

#### JS Calling

See the example of `# UI_start` above. JS can be directly written in the Oleander section to be executed.

### Oleander UI Section

This document introduces how to use the provided UI components to help you quickly create and render interfaces. The document will help you understand how to build interactive and responsive UIs through detailed examples.

### 0. Oleander UI Syntax

#### Layout Components

Use `LayoutComponentName() {}`. Note that the setting of attributes (CSS attributes) requires a trailing comma.

```OleanderTS
LayoutComponentName() {
  attribute: value,
  containedComponents
}
```

#### Basic Components

##### OleanderUI-ark Framework (Recommended)

Please note the trailing comma.

Use the `data_` prefix to change attributes and the `method_` prefix to call methods in `{}`.

```OleanderTS
Button() {
  data_text : "1",
  method_set_on_click: "alert('Button 1 clicked')",
}
```

#### Conditional Rendering
```OleanderTS
if(condition) {
  componentsToRenderConditionally
}
```

#### Loop Rendering
```OleanderTS
x() {
  data_text : "${item}",
  method_for_render: "[1,2,3]"
}
```
This will render three "x"s and display them as 1, 2, 3. `${item}` can be used anywhere that needs to call a list (such as `[1,2,3]` here).

#### Example:

See the `/ProjectExample-ark` folder in the project.

##### OleanderUI-object Framework (More Powerful)

Similar to Python objects

Use the `object.attribute = content` prefix to change attributes and the `object.method(content)` prefix to call methods.

```OleanderTS
Button = Button()
Button.text = "1"
Button.on_click = "alert('Button 1 clicked')"
```

#### Conditional Rendering

Use the `condition` method.

```OleanderTS
object.condition("js expression returning bool")
```

#### Loop Rendering

Use the `for_render` method.

```OleanderTS
object.for_render(item1,item2...)
```
This will render three "objects" and display them as 1, 2... `${item}` can be used anywhere that needs to call a list (such as `[1,2...]` here).

#### Example:

See the `/ProjectExample-object` folder in the project.

### 1. Basic Components

These basic components are the core of UI construction. You can build your interface by combining and customizing these components.

#### 1.1 `UIComponent` Class
All UI components inherit from the `UIComponent` class. This class contains common style and sub-component management functions.

##### Methods:
- `set_style(**kwargs)`: Sets the style, supporting passing in multiple CSS properties and values.
- `render()`: Renders the component and returns HTML.

##### Features
- `Text`: You can use the `js_` prefix to use variables defined in JavaScript as the displayed text.

#### 1.2 `Text` Class

Text component, allowing the creation of text.

##### Attributes:
- `text`: The text to display

#### 1.3 `Button` Class

Button component, allowing users to create clickable buttons.

##### Methods:
- `set_on_click(callback)`: Sets the button's click event, which can pass in JavaScript code or a callback function. (Depends on the `on_click` attribute)

##### Attributes:
- `text`: The text to display
- `on_click`: Sets the button's click event, which can pass in JavaScript code or a callback function.

#### 1.4 `Radio` Class

Radio button component, allowing users to select one of multiple options.

##### Methods

- `set_checked(True)`: Whether to select by default

#### 1.5 `Toggle` Class

Toggle button component, which can switch between two states (such as on/off).

##### Methods

- `set_checked(True)`: Whether to select by default

##### Attributes

- `label_on`: The text displayed when turned on
- `label_off`: The text displayed when turned off

#### 1.6 `Progress` Class

Progress bar component, used to display the completion progress of a task.

##### Attributes

- `value`: Progress

#### 1.7 `Image` Class

Image component, used to embed images in the interface.

##### Attributes

- `src`: Image address

### 2. Layout Components

Layout components are used to control the layout of multiple sub-components. You can use the `Row` or `Column` class to organize components.

#### 2.1 `Row` Class

Row layout, sub-components are arranged horizontally.

#### 2.2 `Column` Class

Column layout, sub-components are arranged vertically.

### 3. Interactive Components

Interactive components such as `Dialog` and `Menu` can help you create pop-up windows and navigation menus containing interactive content.

#### 3.1 `Dialog` Class

Dialog box component, used to display messages or content.

##### Attributes

- `title`: Title
- `content`: Content

#### 3.2 `Menu` Class

Menu component, used to create clickable list items.

##### Methods

- `add_item`: Add a list item

### 4. Advanced Usage

#### 4.1 Conditional Rendering (Method Available for All Components)

You can determine conditions and decide whether to render.

##### Example
```OleanderTS
Button() {
  data_text : "2-Button Only Visible During the Day",
  data_on_click: "alert('Button 2 clicked')",
  method_condition: "isDaytime"
}
```

Note: The `isDaytime` function has already been defined using JS in the Oleander section. It returns true during the day and false at night.

You can see the button during the day, but you can't see it when you open it at night.

#### 4.2 Page Calling

You can embed other pages by setting the attributes of the component.

##### Attributes

- `src`: Page name
- `width`: Embedded width
- `height`: Embedded height

##### Example:
```OleanderTS
iframe = Iframe(src="pay", width="800", height="600")
iframe.set_style(border="2px solid black")
html = button.render() + iframe.render() + auto_js_code
```

#### 4.3 Combining Complex Layouts

You can create complex layouts by nesting multiple layout components (such as `Row` and `Column`) together.

##### Example:
```OleanderTS
Row() {
  "background" : "lightblue",
  "padding" : "20px",
  Column() {
    "margin" : "20px",
    "padding" : "10px",
    Button() {
      data_text : "1",
      data_on_click: "alert('Button 1 clicked')",
    }
  }
  Column() {
    "margin" : "20px",
    "padding" : "10px",
    Button() {
      data_text : "3",
      data_on_click: "alert('Button 3 clicked')",
    }
    Button() {
      data_text : "2-Button Only Visible During the Day",
      data_on_click: "alert('Button 2 clicked')",
      method_condition: "isDaytime"
    }
    Button() {
      data_text : "2-Button Only Visible at Night",
      data_on_click: "alert('Button 2 clicked')",
      method_condition: "!isDaytime"
    }
  }
}
```

---

## Compilation

### Precautions

Please install the `json5` and `filetype` libraries first.

### File Structure

```file
└─ init
└─── init.yh
└─ app.json5
└─ build.json5
```

### app.json5

```json5
{
  "page": [// Page table
    {
      "name": "init",// Page name
      "srcPath": "./init",// Page location (relative path)
      "dependencies": ["dependencies.yh"]// Dependency library table
    }
  ],
  "APP_Scope": {// Software configuration
    "icon": "$media: app_icon.png",// Icon, located in “APP_Scope/media/app_icon.png” $xx represents the path under “APP_Scope/xx”
    "name": "DEMO",// Name
    "lang":"zh_cn"
  }
}
```

### build.json5

```json5
{
  "Minimum-required-API-version": "0.6.3",// Minimum compatible API version, required
  "Target-API-version": "0.6.3",// Target API version, required
  "name": "demo",// Project name and module root package name, required
  "version": "1.0.0",// Module version information, required
  "compile-option": {
    "version": true
  }// Additional compilation command options, not required
}
```

### Compilation Method

Additional compilation command options:

```
“--fapi-version API version” or “-fver API version” specifies the API version
“--version” or “-v” gets the API version
“--skip-env-check” or “-e” skips the environment check

Can also be specified in build.json5
"compile-option": {
  "version": true,// Get the API version, use true or false to control
  "skip_env_check": true,// Skip the environment check, use true or false to control
  "fapi_version": "ark"// Specify the API version, with object and ark versions available
}

```

First `cd` to your project folder

Directly execute main.py

It will be compiled into app.html

Note:
* This tutorial is applicable to OleanderTS-API V1.0.0 Stable version
