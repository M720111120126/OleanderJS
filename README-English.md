# OleanderTS Documentation

In reality, this language is Oleander+JS+OleanderUI, but the author originally intended to use Oleander+TS+OleanderUI. Hence the name "OleanderTS".

[简体中文](https://github.com/M720111120126/OleanderTS/blob/master/README.md) [繁體中文](https://github.com/M720111120126/OleanderTS/blob/master/README-TraditionalChinese.md)

---

## Syntax

### Oleander Section

The Oleander section only brings preprocessing and JS calling features to OleanderTS.

#### Preprocessing

Preprocessing directives start with `#` and are expanded at compile time.

##### `#include "file"`

```OleanderTS
#include preprocess_test.yh
// → Directly copy the file content here
```
Note:

1.  Here, `file` is the relative directory of the page code. For example, `#include preprocess_test.yh` in `./entry/init.yh` fills in `./entry/preprocess_test.yh`.

2.  All included items must have their names written in the `dependencies` of the page corresponding to `app.json5`. For example:
```json5
{
  "page": [// Page table
    {
      "name": "init",// Page name
      "srcPath": "./entry",// Page location (relative path)
      "dependencies": [
        "preprocess_test.yh"// Fill in the name
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

The start flag for the Oleander UI section

```OleanderTS
#include ……
#define ……
Some JS code

# UI_start

Oleander UI code should be written here
```

#### JS Calling

See the example of `# UI_start` above. JS can be directly written in the Oleander section and executed.

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

Use `BasicComponentName(content)` or `BasicComponentName() {content}`

##### `BasicComponentName(content)`

```OleanderTS
Button(1)
```

##### `BasicComponentName() {content}`

Note the trailing comma.

Use the `data_` prefix to change attributes in `{}` and the `method_` prefix to call methods.

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
    if(isDaytime) {
      Button() {
        data_text : "Button 2 - Visible only during the day",
        data_on_click: "alert('Button 2 clicked')"
      }
    }
    if(!isDaytime) {
      Button() {
        data_text : "Button 2 - Visible only at night",
        data_on_click: "alert('Button 2 clicked')"
      }
    }
  }
}
```

### 1. Basic Components

These basic components are the core of UI construction. You can build your interface by combining and customizing these components.

#### 1.1 `UIComponent` Class
All UI components inherit from the `UIComponent` class. This class contains common style and subcomponent management functions.

##### Methods:
- `set_style(**kwargs)`: Sets the style, supporting passing in multiple CSS properties and values.
- `render()`: Renders the component and returns HTML.

##### Features:
- `Text`: Use the `js_` prefix to use variables defined in JavaScript as display text.

#### 1.2 `Text` Class

Text component, used for creating text.

##### Properties:
- `text`: The text to display.

#### 1.3 `Button` Class

Button component, allows creation of clickable buttons.

##### Methods:
- `set_on_click(callback)`: Sets the click event for the button, which can take JavaScript code or a callback function.

##### Properties:
- `text`: Text to display.
- `on_click`: The button's click event.

#### 1.4 `Radio` Class

Radio button component, allows users to select one option from multiple choices.

##### Methods:
- `set_checked(True)`: Whether it is checked by default.

#### 1.5 `Toggle` Class

Toggle button component, can switch between two states (e.g., on/off).

##### Methods:
- `set_checked(True)`: Whether it is checked by default.

##### Properties:
- `label_on`: Text displayed when on.
- `label_off`: Text displayed when off.

#### 1.6 `Progress` Class

Progress bar component, shows the completion progress of a task.

##### Properties:
- `value`: Progress value.

#### 1.7 `Image` Class

Image component, used for embedding images in the UI.

##### Properties:
- `src`: Image source URL.

### 2. Layout Components

Layout components control the arrangement of multiple child components. You can use `Row` or `Column` classes to organize components.

#### 2.1 `Row` Class

Row layout, arranges child components horizontally.

#### 2.2 `Column` Class

Column layout, arranges child components vertically.

### 3. Interactive Components

Interactive components such as `Dialog` and `Menu` help you create popups and navigation menus with interactive content.

#### 3.1 `Dialog` Class

Dialog component, used to display messages or content.

##### Properties:
- `title`: The title.
- `content`: The content.

#### 3.2 `Menu` Class

Menu component, used to create clickable list items.

##### Methods:
- `add_item`: Adds a list item.

### 4. Advanced Usage

#### 4.1 Conditional Rendering (Available for all components)

You can evaluate a condition to decide whether to render a component.

##### Example:
```OleanderTS
Button() {
  data_text : "2-Daytime only",
  data_on_click: "alert('Button 2 clicked')",
  method_condition: "isDaytime"
}
```

Note: The `isDaytime` function has been defined in the Oleander section with JS, returning `true` during the day and `false` at night.

The button will be visible during the day, and will not be visible at night.

#### 4.2 Page Invocation

You can embed other pages by setting component properties.

##### Properties:
- `src`: The page name.
- `width`: The embedded width.
- `height`: The embedded height.

##### Example:
```OleanderTS
iframe = Iframe(src="pay", width="800", height="600")
iframe.set_style(border="2px solid black")
html = button.render() + iframe.render() + auto_js_code
```

#### 4.3 Combining Complex Layouts

You can create complex layouts by nesting multiple layout components (such as `Row` and `Column`).

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
      data_text : "2-Daytime only",
      data_on_click: "alert('Button 2 clicked')",
      method_condition: "isDaytime"
    }
    Button() {
      data_text : "2-Nighttime only",
      data_on_click: "alert('Button 2 clicked')",
      method_condition: "!isDaytime"
    }
  }
}
```

---

## Compilation

### Notes

Please install the json5 and filetype libraries first.

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
    "icon": "$media: app_icon.png",// Icon, located in “APP_Scope/media/app_icon.png” $xx means under the “APP_Scope/xx” path
    "name": "DEMO",// Name
    "lang":"en"
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
  "fapi_version": "beta"// Specify the API version, with beta and alpha versions available
}

```

First, `cd` to your project folder

Directly execute `main.py`

It will be compiled into `app.html`

Note:
* This tutorial is applicable to OleanderTS-API V0.7.2 Gamma version.