## This tutorial uses machine translation, which may be somewhat inaccurate.

# Oleander TS document

Actually, this language is Oleander+JS+OleanderUI, but the author originally intended to use Oleander+TS+OleanderUI. So it's called 'Oleander TS'

---

## Grammar

### Oleander section

The Oleander section only brings pre-processing features to the Oleander TS

#### Preprocessing

Preprocessing instructions start with '#' and will be expanded during compilation.

##### `#include "file"`

```scl
#include preprocess_test.yh
//→ Copy the file content directly here
```
be careful:

1. The file here is the relative directory of the page code, such as/ The entry/init.rh is filled with # include preprocess_test.rh/ entry/preprocess_test.yh

Everything included must be named in the dependencies section of the page corresponding to app.json5, such as:
```json5
{
"page":  [//Page Table
{
"name": "init",//  page name
"srcPath": "./entry",//  Page position (relative path)
"dependencies": [
Preprocess_test. yh "//Fill in the name
]//Dependency library table
}
]
}
```

##### `#define value key`

A replacement

```Oleander TS
#For example, the code here works normally
#define + left

1 left 1
```

##### `# UI_start`

Open flag for Oleander UI section

```Oleander TS
#include ……
#define ……
Some JS code

# UI_start

I should write Oleander UI code here
```

### Oleander UI section

This document explains how to use the provided UI components to help you quickly create and render interfaces. The document will help you understand how to build interactive and responsive UI through detailed examples.

### 1.  Basic components

These basic components are the core of UI construction, and you can build your interface by combining and customizing these components.

#### 1.1 'UIComponent' Class
All UI components inherit from the 'UIComponent' class. This class includes common styles and sub component management functions.

##### Method:
-Set_style (* * kwargs): Set the style and support passing multiple CSS properties and values.
-` add_child (child) `: Add the child component to the current component.
-Render(): renders the component and returns HTML.

#### 1.2 Button Class

Button component that allows users to create clickable buttons.

##### Method:
-Set_on_click (callback): Set the click event for the button, which can be passed in JavaScript code or callback functions.

##### Example:
```Oleander TS
Button=Button (click on me)
Button.set_on_click ("alert")
button.set_style(color="white", background="blue", padding="10px")
html = button.render()
```

Output:
```html
<button style="color: white; background: blue; padding: 10px;" onclick="alert">Click on me</button>
```

#### 1.3 'Radio' Class

A radio button component that allows users to choose from multiple options.

##### Example:
```Oleander TS
Radio1=Radio ("group1", "option 1"). setchecked (True)
Radio2=Radio ("group1", "option 2")
radio1.set_style(margin="10px")
radio2.set_style(margin="10px")
html = radio1.render() + radio2.render()
```

Output:
```html
<input type="radio" name="group1" value="option 1" checked style="margin: 10px"/>
<input type="radio" name="group1" value="option 2" style="margin: 10px"/>
```

#### 1.4 'Toggle' Class

The toggle button component can switch between two states (such as on/off).

##### Example:
```Oleander TS
Toggle=toggle ("on", "off")
toggle.set_checked(True)
toggle.set_style(background="lightgreen", padding="10px")
html = toggle.render()
```

Output:
```html
<button style="background: lightgreen; padding: 10px;">Enable</button>
```

#### 1.5 'Progress' Class

Progress bar component, used to display the completion progress of tasks.

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

#### 1.6 'Image' Class

Image component, used to embed images in the interface.

##### Example:
```Oleander TS
image = Image(" https://example.com/image.jpg ")
image.set_style(width="200px", height="auto")
html = image.render()
```

Output:
```html
<img src=" https://example.com/image.jpg " style="width: 200px;  height: auto"/>
```



### 2.  Layout

The layout component is used to control the layout of multiple sub components. You can use the 'Row' or 'Column' classes to organize components.

#### 2.1 Row Class

Row layout, with sub components arranged horizontally.

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
<button style="color: white; background: blue; padding: 10px;" onclick="alert">Click on me</button>
<progress value="50" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
<img src=" https://example.com/image.jpg " style="width: 200px;  height: auto"/>
</div>
```

#### 2.2 Column Class

Arrange the sub components vertically in the layout.

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
<h1>Welcome</h1>
<p>This is a simple dialog box</p>
</div>
<ul style="list-style-type: none; padding: 0; margin: 0;">
<li>Menu item 1</li>
<li>Menu item 2</li>
<li>Menu item 3</li>
</ul>
</div>
```

### 3.  Interactive components

Interactive components such as Dialogue and Menu can help you create pop ups and navigation menus that contain interactive content.

#### 3.1 'Dialogue' Class

A dialog box component used to display messages or content.

##### Example:
```Oleander TS
Dialog=Dialogue ("Welcome", "This is a simple dialog box")
dialog.set_style(border="1px solid #ccc", padding="10px", background="#f9f9f9")
html = dialog.render()
```

Output:
```html
<div class="dialog" style="border: 1px solid #ccc; padding: 10px; background: #f9f9f9;">
<h1>Welcome</h1>
<p>This is a simple dialog box</p>
</div>
```

#### 3.2 'Menu' Class

Menu component, used to create clickable list items.

##### Example:
```Oleander TS
menu = Menu()
Menu.add_item ("Menu Item 1"). add_item ("Menu Item 2"). add_item ("Menu Item 3")
menu.set_style(list_style_type="none", padding="0", margin="0")
html = menu.render()
```

Output:
```html
<ul style="list-style-type: none; padding: 0; margin: 0;">
<li>Menu item 1</li>
<li>Menu item 2</li>
<li>Menu item 3</li>
</ul>
```

### 4.  Advanced Usage

#### 4.1 Page Call

You can call other pages by setting the properties of the component

##### Example:
```Oleander TS
iframe = Iframe(src="pay", width="800", height="600")
iframe.set_style(border="2px solid black")
html = button.render() + iframe.render() + auto_js_code
```

Output:
```html
<iframe width="800" height="600" style="border: 2px solid black;">The compilation result of your page named pay</iframe>
```

#### 4.1 Dynamic updates

You can dynamically update the status of a component by setting its properties, such as updating the value of the progress bar, the status of the toggle button, etc. You just need to call the corresponding 'set_ *' method and re render the component.

#####Example:
```Oleander TS
progress.set_value(75)
html = progress.render()
```

Output:
```html
<progress value="75" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
```

#### 4.2 Composite Complex Layout

You can create complex layouts by nesting multiple layout components such as Row and Column together.

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
<button style="color: white; background: blue; padding: 10px;" onclick="alert">Click on me</button>
<progress value="50" max="100" style="width: 100%; height: 20px; background: lightgray;"></progress>
</div>
<div class="dialog" style="border: 1px solid #ccc; padding: 10px; background: #f9f9f9;">
<h1>Welcome</h1>
<p>This is a simple dialog box</p>
</div>
</div>
```

---

## Compile

```file
└─ init
└─── init.yh
└─ app.json5
└─ build.json5
```

### app.json5

```json5
{
"page":  [//Page Table
{
"name": "init",//  page name
"srcPath": "./entry",//  Page position (relative path)
"dependencies":  []//Dependency library table
}
]
}
```

### app.json5

```json5
{
"Minimum-required-API-version":  0.1.0 ",//Minimum compatible API version, must be
"Target-API-version":  0.1.0 ",//The API version of the target must be
"name": "demo",//  Project name and module root package name, required
"version":  1.0.0 ",//module version information, required
"compile-option":  //Additional compilation command options, not required
}
```

Note: This tutorial is applicable to OleanderTS-API V0.0.1 alpha version