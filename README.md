# 🕸️ Arduino Web Inject

> Inject and build web files into your sketches.

## 💾 Installation

Arduino Web Inject is a full-written Python project, choose your OS to for detailed installation instructions


<details>
<summary><strong>Windows</strong></summary>

### Install on Windows
  
This project require Python on your PC, please visit this page <https://www.python.org/downloads/windows/>, then download and install the "Windows installer (64-bit)". Keep note where Python will be installed.

Open a shell and type the following command (amend path on your PC with the right username)

```
C:\Users\Sam\AppData\Local\Programs\Python\Python310\Scripts\pip install arduino-web-inject
```
</details>



<details>
<summary><strong>macOS</strong></summary>

### Install on macOS

</details>


<details>
<summary><strong>Ubuntu/Debian</strong></summary>

```shell
$ sudo apt install python
```

```shell
$ pip install arduino-web-inject
```

</details>



<details>
<summary><strong>Linux</strong></summary>

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

On Windows (with `cmd.exe`)

```shell
C:\Users\Sam\AppData\Local\Programs\Python\Python310\Scripts\arduino-web-inject C:\Users\SamSepiol\OneDrive\Documents\Arduino
```

On macOS

```shell
% arduino-web-inject /Users/SamSepiol/Documents/Arduino
```

On Ubuntu/Debian/Linux

```shell
$ arduino-web-inject /home/SamSepiol/Arduino
```

