# Quartus_Verilog_Builder_v2
Tool to assist in the creation of finite state machines in Quartus, written in Verilog HDL 

The Quartus Verilog Builder script is written in Python and works with Python 2
and Python 3. If you do not have Python installed on your computer, you can find
the Windows link here:
https://www.python.org/ftp/python/3.7.1/python-3.7.1-amd64.exe

and the Mac link here:
https://www.python.org/ftp/python/3.7.1/python-3.7.1-macosx10.6.pkg


========================================================================================================================================
INSTRUCTIONS

To use this tool, run the "fileBuilder.py" Python script by double clicking it or right clicking and
open with Python. You should then be presented with a GUI where you can input the module name, select
the FPGA components you need, and enter the names of the states for the FSM. When you are finished, click
the "Done" button and a .v Verilog header file should be in the Quartus_Verilog_Builder_v2 folder, along 
with a .csv pin assignments file.

To use the Verilog header file, include the file when you are creating your project, or add it later: 
1) Move the .v file into the Quartus project directory.
2) Project -> Add/Remove Files in Project, select the file using the file explorer, and click OK.
3) Project -> Set as Top-Level Entity.

To use the pin assignments file in Quartus: Once you have created your project, go to Assignments -> Import Assignments
and select the .csv file from the Quartus_Verilog_Builder_v2 folder.

*****NOTE: The fileBuilder just builds the outline Verilog and you still have to implement the logic. Control-f, type "#####" to find all the lines that need code added


========================================================================================================================================
Copyright <2018> <Tyler McGrew>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Quartus Verilog Builder"), to deal in the Quartus Verilog Builder without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Quartus Verilog Builder, and to permit persons to whom the Quartus Verilog Builder is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Quartus Verilog Builder.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE 
