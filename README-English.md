# Oleander TS Documentation

Actually, this language is Oleander+JS+OleanderUI, but the author originally wanted to use Oleander+TS+OleanderUI. So it's called "Oleander TS".

[简体中文](https://github.com/M720111120126/OleanderTS/blob/master/README.md) [繁體中文](https://github.com/M720111120126/OleanderTS/blob/master/README-TraditionalChinese.md)

---

## Syntax

### Oleander Part

The Oleander part only brings preprocessing and JS calling features to Oleander TS.

#### Preprocessing

Preprocessing directives start with `#` and are expanded at compile time.

##### `#include "file"`

```scl
#include preprocess_test.yh
// → Directly copy the file content here
```
Note:

1.  The file here is the relative directory of the page code, such as ./entry/init.yh. Using #include preprocess_test.yh fills in ./entry/preprocess_test.yh.

2.  All included items must have their names written in the dependencies of the page corresponding to app.json5, such as:
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
# The code here works normally
#define + left

1 left 1
```

##### `# UI_start`

The opening flag of the Oleander UI part

```Oleander TS
#include ……
#define ……
Some JS code

# UI_start

Oleander UI code should be written here
```

#### JS Calling

See the example of # UI_start above, js can be executed directly by writing it in the Oleander part.

### Oleander UI Part

This document describes how to use the provided UI components to help you quickly create and render interfaces. The document will help you understand how to build interactive and responsive UIs through detailed examples.

### 0. Oleander UI Syntax

#### Layout Components

Use `LayoutComponentName() {}` Note that the setting of attributes (css attributes) requires a trailing comma.

```Oleander TS
LayoutComponentName() {
  attribute: value,
  contained components
}
```

#### Basic Components

Use `BasicComponentName(passed content)` or `BasicComponentName() {content}`

##### `BasicComponentName(passed content)`

```Oleander TS
Button(1)
```

##### `BasicComponentName() {content}`

Please note the trailing comma.

Use the `data_` prefix to change attributes and the `method_` prefix to call methods in `{}`.

```Oleander TS
Button() {
  data_text : "1",
  method_set_on_click: "alert('Button 1 was clicked')",
  }
```

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
      data_on_click: "alert('Button 1 was clicked')",
    }
  }
  Column() {
    "margin" : "20px",
    "padding" : "10px",
    Button() {
      data_text : "3",
      data_on_click: "alert('Button 3 was clicked')",
    }
    Button() {
      data_text : "2-Button visible only during the day",
      data_on_click: "alert('Button 2 was clicked')",
      method_condition: "isDaytime"
    }
    Button() {
      data_text : "2-Button visible only at night",
      data_on_click: "alert('Button 2 was clicked')",
      method_condition: "!isDaytime"
    }
  }
}
```

### 1. Basic Components

These basic components are the core of UI construction. You can build your interface by combining and customizing these components.

#### 1.1 `UIComponent` Class
All UI components inherit from the `UIComponent` class. This class contains common style and subcomponent management functions.

##### Methods:
- `set_style(**kwargs)`: Sets the style, supports passing in multiple CSS attributes and values.
- `render()`: Renders the component and returns HTML.

#### 1.2 `Button` Class

Button component, allows users to create clickable buttons.

##### Methods:
- `set_on_click(callback)`: Sets the click event of the button, you can pass in JavaScript code or a callback function. (Depends on the on_click attribute)

##### Attributes:
- `text`: Displayed text
- `on_click`: Sets the click event of the button, you can pass in JavaScript code or a callback function.

#### 1.3 `Radio` Class

Radio button component, allows users to select one of multiple options.

##### Methods

- `set_checked(True)`: Whether to select by default

#### 1.4 `Toggle` Class

Toggle button component, can switch between two states (such as on/off).

##### Methods

- `set_checked(True)`: Whether to select by default

##### Attributes

- `label_on`: Text displayed when turned on
- `label_off`: Text displayed when turned off on style="background: lightgreen; padding: 10px;">On</button>

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

##### Methods

- `add_item`: Add a list item

### 4. Advanced Usage

#### 4.1 Conditional Rendering (Method available for all components)

You can determine the condition and decide whether to render

##### Example
```Oleander TS
Button() {
  data_text : "2-Button visible only during the day",
  data_on_click: "alert('Button 2 was clicked')",
  method_condition: "isDaytime"
}
```

Note: The isDaytime function has been defined in JS in the Oleander part. It returns true during the day and false at night.

You can see the button during the day, but you can't see it when you open it at night.

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
      data_on_click: "alert('Button 1 was clicked')",
    }
  }
  Column() {
    "margin" : "20px",
    "padding" : "10px",
    Button() {
      data_text : "3",
      data_on_click: "alert('Button 3 was clicked')",
    }
    Button() {
      data_text : "2-Button visible only during the day",
      data_on_click: "alert('Button 2 was clicked')",
      method_condition: "isDaytime"
    }
    Button() {
      data_text : "2-Button visible only at night",
      data_on_click: "alert('Button 2 was clicked')",
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

### app.json5

```json5
{
  "Minimum-required-API-version": "0.1.0",// Minimum compatible API version, required
  "Target-API-version": "0.1.0",// Target API version, required
  "name": "demo",// Project name and module root package name, required
  "version": "1.0.0",// Module version information, required
  "compile-option": ""// Additional compilation command options, not required
}
```

### Compilation Method

First cd to the OleanderTS project folder

Directly execute main.py

Will be compiled into app.html

Note:
* This tutorial is applicable to OleanderTS-API V0.4.6 Beta version
