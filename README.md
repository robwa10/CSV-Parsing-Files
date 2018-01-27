# Parse-and-Analyze
A collection of modules and example files used for parsing files and analyzing data.  

README.md contains overview documentation.  
[MODULES.md](/docs/MODULES.md) contains documentation for all modules.  
[EXAMPLE-FILES.md](/docs/EXAMPLE-FILES.md) contains documentation for files demonstrating module functionality.

## Table of Contents  
[Requirements](Requirements)  
[Structure, Usage, Installation](Structure, Usage, Installation)  
 * Structure  
 * Usage
  - As Modules
  - Example Files
 * Install and cd  

[Pull Requests and Maintenance](Pull Requests and Maintenance)  
[Copyright](Copyright)

## Requirements  
All files are written for Python v3 or higher. Instructions for downloading Python 3 can be found [here](https://www.python.org/downloads/).

## Structure, Usage, Installation  
#### Structure  
Each function is contained in a file of the same name. The file `parse.py` imports all functions.

#### Usage
__As Modules__  
  - Access all modules by importing `parse.py`. For example `import parse as p`.  
  - Access individual modules by importing them directly. For example `import parse_csv`.

__Example Files__  
Several example files are contained in this repository which can be used as is or expanded upon to increase functionality.

#### Install and cd  
`git clone https://github.com/robwa10/Parse-and-Analyze.git`  
`cd Parse-and-Analyze`

## Pull Requests and Maintenance
Pull requests are encouraged except for the following:
 * File and Folder Structure  

This repo is maintained by me and I have bills to pay and mouths to feed so please be patient with any pull requests or issues.

## Copyright  
Licensed under the MIT License.  
Copyright (c) 2018 Robert Hubbard

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
