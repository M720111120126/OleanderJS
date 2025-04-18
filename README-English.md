# Oleander TS Documentation

In reality, this language is Oleander+JS+OleanderUI, but the author originally intended to use Oleander+TS+OleanderUI. Hence the name "Oleander TS".

[简体中文](https://github.com/M720111120126/OleanderTS/blob/master/README.md) [繁體中文](https://github.com/M720111120126/OleanderTS/blob/master/README-TraditionalChinese.md)

---

## Syntax

### Oleander Section

The Oleander section only brings preprocessing and JS calling features to Oleander TS.

#### Preprocessing

Preprocessing directives start with `#` and are expanded at compile time.

##### `#include "file"`

```scl
#include preprocess_test.yh
// → Directly copy the file content here
```
Note:

1.  Here, `file` is the relative directory of the page code, such as `./entry/init.yh`. Using `#include preprocess_test.yh` fills in `./entry/preprocess_test.yh`.

2.  Everything included must have its name written in the `dependencies` of the page corresponding to `page` in `app.json5`. For example:
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

```Oleander TS
# For example, the code here works normally
#define + left

1 left 1
```

##### `# UI_start`

The start flag for the Oleander UI section

```Oleander TS
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

```Oleander TS
LayoutComponentName() {
  attribute: value,
  containedComponents
}
```

#### Basic Components

Use `BasicComponentName(contentPassedIn)` or `BasicComponentName() {content}`

##### `BasicComponentName(contentPassedIn)`

```Oleander TS
Button(1)
```

##### `BasicComponentName() {content}`

Note the trailing comma.

Use the `data_` prefix to change attributes in `{}` and the `method_` prefix to call methods.

```Oleander TS
Button() {
  data_text : "1",
  method_set_on_click: "alert('Button 1 clicked')",
  }
```

#### Conditional Rendering
```Oleander TS
if(condition) {
  componentsRenderedConditionally
}
```

#### Loop Rendering
```Oleander TS
x() {
  data_text : "${item}",
  method_for_render: "[1,2,3]"
}
```
This will render three "x"s and display them as 1, 2, 3. `${item}` can be used anywhere that needs to call a list (such as `[1,2,3]` here).

#### Example:
```Oleander TS
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

#### 1.2 `Button` Class

Button component, allowing users to create clickable buttons.

##### Methods:
- `set_on_click(callback)`: Sets the button's click event, which can pass in JavaScript code or a callback function. (Depends on the on_click attribute)

##### Attributes:
- `text`: The text displayed
- `on_click`: Sets the button's click event, which can pass in JavaScript code or a callback function.

#### 1.3 `Radio` Class

Radio button component, allowing users to select one of multiple options.

##### Method

- `set_checked(True)`: Whether to select by default

#### 1.4 `Toggle` Class

Toggle button component, which can switch between two states (such as on/off).

##### Method

- `set_checked(True)`: Whether to select by default

##### Attributes

- `label_on`: Text displayed when on
- `label_off`: Text displayed when offon style="background: lightgreen; padding: 10px;">On</button>

#### 1.5 `Progress` Class

Progress bar component, used to display the completion progress of a task.

##### Attributes

- `value`: Progress

#### 1.6 `Image` Class

Image component, used to embed images in the interface.

##### Attributes

- `src`: Image address

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

##### Attributes

- `title`: Title
- `content`: Content

#### 3.2 `Menu` Class

Menu component, used to create clickable list items.

##### Method

- `add_item`: Add a list item

### 4. Advanced Usage

#### 4.1 Conditional Rendering (Method Available for All Components)

You can determine conditions and decide whether to render

##### Example
```Oleander TS
Button() {
  data_text : "Button 2 - Visible only during the day",
  data_on_click: "alert('Button 2 clicked')",
  method_condition: "isDaytime"
}
```

Note: The `isDaytime` function has already been defined using JS in the Oleander section. It returns true during the day and false at night.

The button can be seen during the day, but it will disappear when opened at night.

#### 4.2 Page Calling

You can embed other pages by setting the attributes of the component.

##### Attributes

- `src`: Page name
- `width`: Embedded width
- `height`: Embedded height

##### Example:
```Oleander TS
iframe = Iframe(src="pay", width="800", height="600")
iframe.set_style(border="2px solid black")
html = button.render() + iframe.render() + auto_js_code
```

#### 4.3 Combining Complex Layouts

You can create complex layouts by nesting multiple layout components (such as `Row` and `Column`) together.

##### Example:
```Oleander TS
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
      data_text : "Button 2 - Visible only during the day",
      data_on_click: "alert('Button 2 clicked')",
      method_condition: "isDaytime"
    }
    Button() {
      data_text : "Button 2 - Visible only at night",
      data_on_click: "alert('Button 2 clicked')",
      method_condition: "!isDaytime"
    }
  }
}
```

---

## Compilation

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
      "srcPath": "./entry",// Page location (relative path)
      "dependencies": []// Dependency library table
    }
  ]
}
```

### build.json5

```json5
{
  "Minimum-required-API-version": "0.4.7",// Minimum compatible API version, required
  "Target-API-version": "0.4.7",// Target API version, required
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

First, `cd` to the OleanderTS project folder

Directly execute `main.py`

It will be compiled into `app.html`

Note:
* This tutorial is applicable to OleanderTS-API V0.4.8 Beta3
