# 🕸️ Arduino Web Inject

[![Pylint](https://github.com/fulminati/arduino-web-inject/actions/workflows/pylint.yml/badge.svg)](https://github.com/fulminati/arduino-web-inject/actions/workflows/pylint.yml)

> Inject and build web files into your sketches.

Arduino Web Inject fills your sketches (*.ino) files with HTML/CSS/JS code from files on your PC. This is useful to work with Web Server and create complex web app around Arduino platform.

### Why I need this?

This is a list of benefit of using Arduino Web Inject:

* The HTML/CSS/JS code will be minified and cleaned of comments before being loaded into Arduino. This will allow for significant space savings.
* Develop a web application using a natural approach and a web-friendly editor.
* Compile your web files into Arduino without relying on heavy and unnecessary filesystem libraries.
* Organize your web application with variables populated directly from Arduino code and reusable layouts. Additionally, you can maximize the use of JavaScript and create SPAs or PWAs.

## 💾 Installation

Arduino Web Inject is a full-written Python project, choose your OS to for detailed installation instructions


<details>
<summary><strong>Windows</strong></summary>

### Install on Windows
  
This project require Python on your PC, please visit this page <https://www.python.org/downloads/windows/>, then download and install the "Windows installer (64-bit)". Keep note where Python will be installed. Make sure to select the option "Add Python 3.x to PATH" during installation.

Open a shell and type the following command (amend path on your PC with the right username)

```
C:\Users\Sam\AppData\Local\Programs\Python\Python310\Scripts\pip install arduino-web-inject
```
</details>



<details>
<summary><strong>macOS</strong></summary>

### Install on macOS

This project require Python on your Mac, please visit this page <https://www.python.org/downloads/macos/>, then download and install the "macOS 64-bit universal2 installer". Keep note where Python will be installed.

> Alternativley you can use `$ brew install python@3.10`

Open a shell and type the following command (amend path on your PC with the right username)

```shell
% pip3 install arduino-web-inject  
```
</details>



<details>
<summary><strong>Ubuntu/Debian</strong></summary>

### Install on Ubuntu/Debian

```shell
$ sudo apt install python
```

```shell
$ pip install arduino-web-inject
```

</details>



<details>
<summary><strong>Linux</strong></summary>

### Install on Linux
    
Found best Python package fit to your needs here <https://www.python.org/downloads/source/>, then use `pip` to install `arduino-web-inject` on your PC.

```shell
$ pip install arduino-web-inject
```

</details>



## 🛠️ Usage

Open a shell and type the following command

```shell
$ arduino-web-inject MY_SKETCHES_DIRECTORY
```

Replace `MY_SKETCHES_DIRECTORY` with your source code directory. For instances

On **Windows** (with `cmd.exe`)

```shell
C:\Users\Sam\AppData\Local\Programs\Python\Python310\Scripts\arduino-web-inject C:\Users\SamSepiol\OneDrive\Documents\Arduino
```

On **macOS** (with `Terminal`)

```shell
% arduino-web-inject /Users/SamSepiol/Documents/Arduino
```

On **Ubuntu/Debian/Linux**

```shell
$ arduino-web-inject /home/SamSepiol/Arduino
```

### Load HTML file into Arduino

To load a HTML file into your project type a comment like this

```cpp
// @inject "index.html"
const String indexPage = "...";

void setup() {
}
```

When you use the `// @inject "filename.html"` our tool automatically load and replace the HTML into the string constant declared below the comment

### Load CSS file into Arduino

To load a CSS file into your project type a comment like this

```cpp
// @inject "style.css"
const String style = "...";

void setup() {
}
```

When you use the `// @inject "filename.css"` our tool automatically load and replace the CSS code into the string constant declared below the comment

### Load JavaScript file into Arduino

To load a JS file into your project type a comment like this

```cpp
// @inject "app.js"
const String js = "...";

void setup() {
}
```

When you use the `// @inject "filename.js"` our tool automatically load and replace the JavaScript code into the string constant declared below the comment

### Where place my web files?

The `@inject` comment looks for files inside your sketeches with a relative path starting from the source file (e.g. Arduino/Blink/Blink.ino), we suggest to use a specific sub-directory as example `web/` and place all your web files inside it. See [examples](https://github.com/fulminati/arduino-web-inject/blob/main/examples/WiFi/WiFi.ino#L22) for inspirations.

### How edit my web files?

To modify your web files, you can use your preferred IDE such as VSCode or WebStorm, but also Notepad++. When our tool detects a change in your web files, it will automatically update your Arduino files.

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
