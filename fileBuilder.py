'''
Created on Nov 10, 2018

@author: Tyler
'''

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import os
import math


########################################################################## Method to reset info and clear fields
def clearAll():
    name.set('')
    states[:] = []
    addstatestext.set('')
    statesText.config(state=NORMAL)
    statesText.delete('1.0', END)
    statesText.config(state=DISABLED)
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)

########################################################################## Method to add states
states = []
def addStates():
    inputstring = addstatestext.get().strip()
    inputs = inputstring.split(',')
    addstatestext.set('')
    for state in inputs:
        if state.strip() not in states and state != '':
            states.append(state.strip())
    statesText.config(state=NORMAL)
    statesText.delete('1.0', END)
    statesText.insert('1.0', ', '.join(states))
    statesText.config(state=DISABLED)

########################################################################## Method to execute done
def done():
    root.destroy()
    writePins()
    writeHeader()

########################################################################## Method to write pin assignments file    
def writePins():
    with open('Pin_Assignments.csv','w') as g:    
        g.write('To,Direction,Location\n\
        AUD_ADCDAT,Input,PIN_D2\n\
        AUD_ADCLRCK,Bidir,PIN_C2\n\
        AUD_BCLK,Bidir,PIN_F2\n\
        AUD_DACDAT,Output,PIN_D1\n\
        AUD_DACLRCK,Bidir,PIN_E3\n\
        AUD_XCK,Output,PIN_E1\n\
        CLOCK2_50,Input,PIN_AG14\n\
        CLOCK3_50,Input,PIN_AG15\n\
        CLOCK_50,Input,PIN_Y2\n\
        EX_IO[6],Bidir,PIN_D9\n\
        EX_IO[5],Bidir,PIN_E10\n\
        EX_IO[4],Bidir,PIN_F14\n\
        EX_IO[3],Bidir,PIN_H14\n\
        EX_IO[2],Bidir,PIN_H13\n\
        EX_IO[1],Bidir,PIN_J14\n\
        EX_IO[0],Bidir,PIN_J10\n\
        HEX0[6],Output,PIN_H22\n\
        HEX0[5],Output,PIN_J22\n\
        HEX0[4],Output,PIN_L25\n\
        HEX0[3],Output,PIN_L26\n\
        HEX0[2],Output,PIN_E17\n\
        HEX0[1],Output,PIN_F22\n\
        HEX0[0],Output,PIN_G18\n\
        HEX1[6],Output,PIN_U24\n\
        HEX1[5],Output,PIN_U23\n\
        HEX1[4],Output,PIN_W25\n\
        HEX1[3],Output,PIN_W22\n\
        HEX1[2],Output,PIN_W21\n\
        HEX1[1],Output,PIN_Y22\n\
        HEX1[0],Output,PIN_M24\n\
        HEX2[6],Output,PIN_W28\n\
        HEX2[5],Output,PIN_W27\n\
        HEX2[4],Output,PIN_Y26\n\
        HEX2[3],Output,PIN_W26\n\
        HEX2[2],Output,PIN_Y25\n\
        HEX2[1],Output,PIN_AA26\n\
        HEX2[0],Output,PIN_AA25\n\
        HEX3[6],Output,PIN_Y19\n\
        HEX3[5],Output,PIN_AF23\n\
        HEX3[4],Output,PIN_AD24\n\
        HEX3[3],Output,PIN_AA21\n\
        HEX3[2],Output,PIN_AB20\n\
        HEX3[1],Output,PIN_U21\n\
        HEX3[0],Output,PIN_V21\n\
        HEX4[6],Output,PIN_AE18\n\
        HEX4[5],Output,PIN_AF19\n\
        HEX4[4],Output,PIN_AE19\n\
        HEX4[3],Output,PIN_AH21\n\
        HEX4[2],Output,PIN_AG21\n\
        HEX4[1],Output,PIN_AA19\n\
        HEX4[0],Output,PIN_AB19\n\
        HEX5[6],Output,PIN_AH18\n\
        HEX5[5],Output,PIN_AF18\n\
        HEX5[4],Output,PIN_AG19\n\
        HEX5[3],Output,PIN_AH19\n\
        HEX5[2],Output,PIN_AB18\n\
        HEX5[1],Output,PIN_AC18\n\
        HEX5[0],Output,PIN_AD18\n\
        HEX6[6],Output,PIN_AC17\n\
        HEX6[5],Output,PIN_AA15\n\
        HEX6[4],Output,PIN_AB15\n\
        HEX6[3],Output,PIN_AB17\n\
        HEX6[2],Output,PIN_AA16\n\
        HEX6[1],Output,PIN_AB16\n\
        HEX6[0],Output,PIN_AA17\n\
        HEX7[6],Output,PIN_AA14\n\
        HEX7[5],Output,PIN_AG18\n\
        HEX7[4],Output,PIN_AF17\n\
        HEX7[3],Output,PIN_AH17\n\
        HEX7[2],Output,PIN_AG17\n\
        HEX7[1],Output,PIN_AE17\n\
        HEX7[0],Output,PIN_AD17\n\
        I2C_SCLK,Output,PIN_B7\n\
        I2C_SDAT,Bidir,PIN_A8\n\
        IRDA_RXD,Input,PIN_Y15\n\
        KEY[3],Input,PIN_R24\n\
        KEY[2],Input,PIN_N21\n\
        KEY[1],Input,PIN_M21\n\
        KEY[0],Input,PIN_M23\n\
        LCD_BLON,Output,PIN_L6\n\
        LCD_DATA[7],Bidir,PIN_M5\n\
        LCD_DATA[6],Bidir,PIN_M3\n\
        LCD_DATA[5],Bidir,PIN_K2\n\
        LCD_DATA[4],Bidir,PIN_K1\n\
        LCD_DATA[3],Bidir,PIN_K7\n\
        LCD_DATA[2],Bidir,PIN_L2\n\
        LCD_DATA[1],Bidir,PIN_L1\n\
        LCD_DATA[0],Bidir,PIN_L3\n\
        LCD_EN,Output,PIN_L4\n\
        LCD_ON,Output,PIN_L5\n\
        LCD_RS,Output,PIN_M2\n\
        LCD_RW,Output,PIN_M1\n\
        LEDG[8],Output,PIN_F17\n\
        LEDG[7],Output,PIN_G21\n\
        LEDG[6],Output,PIN_G22\n\
        LEDG[5],Output,PIN_G20\n\
        LEDG[4],Output,PIN_H21\n\
        LEDG[3],Output,PIN_E24\n\
        LEDG[2],Output,PIN_E25\n\
        LEDG[1],Output,PIN_E22\n\
        LEDG[0],Output,PIN_E21\n\
        LEDR[17],Output,PIN_H15\n\
        LEDR[16],Output,PIN_G16\n\
        LEDR[15],Output,PIN_G15\n\
        LEDR[14],Output,PIN_F15\n\
        LEDR[13],Output,PIN_H17\n\
        LEDR[12],Output,PIN_J16\n\
        LEDR[11],Output,PIN_H16\n\
        LEDR[10],Output,PIN_J15\n\
        LEDR[9],Output,PIN_G17\n\
        LEDR[8],Output,PIN_J17\n\
        LEDR[7],Output,PIN_H19\n\
        LEDR[6],Output,PIN_J19\n\
        LEDR[5],Output,PIN_E18\n\
        LEDR[4],Output,PIN_F18\n\
        LEDR[3],Output,PIN_F21\n\
        LEDR[2],Output,PIN_E19\n\
        LEDR[1],Output,PIN_F19\n\
        LEDR[0],Output,PIN_G19\n\
        SMA_CLKIN,Input,PIN_AH14\n\
        SMA_CLKOUT,Output,PIN_AE23\n\
        SW[17],Input,PIN_Y23\n\
        SW[16],Input,PIN_Y24\n\
        SW[15],Input,PIN_AA22\n\
        SW[14],Input,PIN_AA23\n\
        SW[13],Input,PIN_AA24\n\
        SW[12],Input,PIN_AB23\n\
        SW[11],Input,PIN_AB24\n\
        SW[10],Input,PIN_AC24\n\
        SW[9],Input,PIN_AB25\n\
        SW[8],Input,PIN_AC25\n\
        SW[7],Input,PIN_AB26\n\
        SW[6],Input,PIN_AD26\n\
        SW[5],Input,PIN_AC26\n\
        SW[4],Input,PIN_AB27\n\
        SW[3],Input,PIN_AD27\n\
        SW[2],Input,PIN_AC27\n\
        SW[1],Input,PIN_AC28\n\
        SW[0],Input,PIN_AB28\n\
        UART_CTS,Output,PIN_G14\n\
        UART_RTS,Input,PIN_J13\n\
        UART_RXD,Input,PIN_G12\n\
        UART_TXD,Output,PIN_G9\n\
        VGA_B[7],Output,PIN_D12\n\
        VGA_B[6],Output,PIN_D11\n\
        VGA_B[5],Output,PIN_C12\n\
        VGA_B[4],Output,PIN_A11\n\
        VGA_B[3],Output,PIN_B11\n\
        VGA_B[2],Output,PIN_C11\n\
        VGA_B[1],Output,PIN_A10\n\
        VGA_B[0],Output,PIN_B10\n\
        VGA_BLANK_N,Output,PIN_F11\n\
        VGA_CLK,Output,PIN_A12\n\
        VGA_G[7],Output,PIN_C9\n\
        VGA_G[6],Output,PIN_F10\n\
        VGA_G[5],Output,PIN_B8\n\
        VGA_G[4],Output,PIN_C8\n\
        VGA_G[3],Output,PIN_H12\n\
        VGA_G[2],Output,PIN_F8\n\
        VGA_G[1],Output,PIN_G11\n\
        VGA_G[0],Output,PIN_G8\n\
        VGA_HS,Output,PIN_G13\n\
        VGA_R[7],Output,PIN_H10\n\
        VGA_R[6],Output,PIN_H8\n\
        VGA_R[5],Output,PIN_J12\n\
        VGA_R[4],Output,PIN_G10\n\
        VGA_R[3],Output,PIN_F12\n\
        VGA_R[2],Output,PIN_D10\n\
        VGA_R[1],Output,PIN_E11\n\
        VGA_R[0],Output,PIN_E12\n\
        VGA_SYNC_N,Output,PIN_C10\n\
        VGA_VS,Output,PIN_C13')
    
########################################################################## Method to write .v header file
def writeHeader():
    
    moduleName = name.get()
    if moduleName == '': moduleName = 'ModuleOne'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fileName = os.path.join(dir_path,str.format('{}.v', moduleName))

    
    with open(fileName, 'w') as f:
        
        f.write(str.format('module {} (\n', moduleName))
          
        if var1.get() == 1:
            f.write('\t//---------------------------------- Clock\n')
            f.write('\tCLOCK_50,\n')
            f.write('\tCLOCK2_50,\n')
            f.write('\tCLOCK3_50,\n\n')
          
        if var2.get() == 1:
            f.write('\t//---------------------------------- LED_Red\n')
            f.write('\tLED_R,\n\n')
              
        if var3.get() == 1:
            f.write('\t//---------------------------------- LED_Green\n')
            f.write('\tLED_G,\n\n')
              
        if var4.get() == 1:
            f.write('\t//---------------------------------- Button\n')
            f.write('\tBUTTON,\n\n')
              
        if var5.get() == 1:
            f.write('\t//---------------------------------- VGA\n')
            f.write('\tVGA_R,\n')
            f.write('\tVGA_G,\n')
            f.write('\tVGA_B,\n')
            f.write('\tVGA_CLK,\n')
            f.write('\tVGA_SYNC_N,\n')
            f.write('\tVGA_BLANK_N,\n')
            f.write('\tVGA_HS_N,\n')
            f.write('\tVGA_VS_N,\n\n')
          
        if var6.get() == 1:
            f.write('\t//---------------------------------- Audio\n')
            f.write('\tAUD_ADCDAT,\n')
            f.write('\tAUD_ADCLRCK,\n')
            f.write('\tAUD_BCLK,\n')
            f.write('\tAUD_DACDAT,\n')
            f.write('\tAUD_DACLRCK,\n')
            f.write('\tAUD_XCK,\n')
            f.write('\tI2C_SCLK,\n')
            f.write('\tI2C_SDAT,\n\n')
              
        if var7.get() == 1:
            f.write('\t//---------------------------------- IR_Receiver\n')
            f.write('\tIRDA_RXD,\n\n')
              
        if var8.get() == 1:
            f.write('\t//---------------------------------- RS_232\n')
            f.write('\tUART_CTS,\n')
            f.write('\tUART_RTS,\n')
            f.write('\tUART_RXD,\n')
            f.write('\tUART_TXD,\n\n')
          
        if var9.get() == 1:
            f.write('\t//---------------------------------- Seven_Segment\n')
            f.write('\tHEX0,\n')
            f.write('\tHEX1,\n')
            f.write('\tHEX2,\n')
            f.write('\tHEX3,\n')
            f.write('\tHEX4,\n')
            f.write('\tHEX5,\n')
            f.write('\tHEX6,\n')
            f.write('\tHEX7,\n\n')
              
        if var10.get() == 1:
            f.write('\t//---------------------------------- Switch\n')
            f.write('\tSW,\n\n')
              
        if var11.get() == 1:
            f.write('\t//---------------------------------- LCD\n')
            f.write('\tLCD_DATA,\n')
            f.write('\tLCD_BLON,\n')
            f.write('\tLCD_EN,\n')
            f.write('\tLCD_ON,\n')
            f.write('\tLCD_RS,\n')
            f.write('\tLCD_RW,\n\n')
            
        if var12.get() == 1:
            f.write('\t//---------------------------------- EX_IO\n')
            f.write('\tEX_IO,\n\n')
        
    with open(fileName, 'r') as f:
        
        lines = f.readlines()
        if len(lines) > 2:
            lines[-2] = lines[-2].replace(',','')
            lines[-1] = lines[-1].replace('\n','')
        
        
    with open(fileName, 'w') as f:
    
        f.write(''.join(lines))
        f.write(');\n\n\n')
        f.write('//------------------------------------------------------------------\n')
        f.write('//                 -- Input/Output Declarations --                  \n')
        f.write('//------------------------------------------------------------------\n\n')
          
        if var1.get() == 1:
            f.write('//---------------------------------- Clock\n')
            f.write('input CLOCK_50, CLOCK2_50, CLOCK3_50;\n\n')
          
        if var2.get() == 1:
            f.write('//---------------------------------- LED_Red\n')
            f.write('output [17:0]LED_R;\n\n')
              
        if var3.get() == 1:
            f.write('//---------------------------------- LED_Green\n')
            f.write('output [8:0]LED_G;\n\n')
              
        if var4.get() == 1:
            f.write('//---------------------------------- Button\n')
            f.write('input [3:0]BUTTON;\n\n')
              
        if var5.get() == 1:
            f.write('//---------------------------------- VGA\n')
            f.write('output [7:0]VGA_R;\n')
            f.write('output [7:0]VGA_G;\n')
            f.write('output [7:0]VGA_B;\n')
            f.write('output VGA_CLK, VGA_SYNC_N, VGA_BLANK_N, VGA_HS, VGA_VS;\n\n')
          
        if var6.get() == 1:
            f.write('//---------------------------------- Audio\n')
            f.write('input AUD_ADCDAT;\n')
            f.write('inout AUD_ADCLRCK;\n')
            f.write('inout AUD_BCLK;\n')
            f.write('output AUD_DACDAT;\n')
            f.write('inout AUD_DACLRCK;\n')
            f.write('output AUD_XCK;\n')
            f.write('output I2C_SCLK;\n')
            f.write('inout I2C_SDAT;\n\n')
              
        if var7.get() == 1:
            f.write('//---------------------------------- IR_Receiver\n')
            f.write('input IRDA_RXD;\n\n')
              
        if var8.get() == 1:
            f.write('//---------------------------------- RS_232\n')
            f.write('input UART_RTS, UART_RXD;\n')
            f.write('output UART_CTS, UART_TXD;\n\n')
          
        if var9.get() == 1:
            f.write('//---------------------------------- Seven_Segment\n')
            f.write('output [6:0]HEX0;\n')
            f.write('output [6:0]HEX1;\n')
            f.write('output [6:0]HEX2;\n')
            f.write('output [6:0]HEX3;\n')
            f.write('output [6:0]HEX4;\n')
            f.write('output [6:0]HEX5;\n')
            f.write('output [6:0]HEX6;\n')
            f.write('output [6:0]HEX7;\n\n')
              
        if var10.get() == 1:
            f.write('//---------------------------------- Switch\n')
            f.write('input [17:0]SW;\n\n')
              
        if var11.get() == 1:
            f.write('//---------------------------------- LCD\n')
            f.write('inout [7:0]LCD_DATA;\n')
            f.write('output LCD_BLON, LCD_EN, LCD_ ON, LCD_RS, LCD_RW;\n\n')
          
              
        if var12.get() == 1:
            f.write('//---------------------------------- EX_IO\n')
            f.write('inout [6:0]EX_IO;\n\n')
            
        f.write('\n//------------------------------------------------------------------\n')
        f.write('//                  -- State & Reg Declarations  --                   \n')
        f.write('//------------------------------------------------------------------\n\n')
        
        bits = 0
        if len(states) > 0:
            bits = math.ceil(math.log(len(states))/math.log(2))
            if bits == 0: bits = 1
            f.write('Parameter ')
            f.write('{} = {}\'d0'.format(states[0], bits))
            
            if len(states) > 1:
                count = 1
                for state in states[1:]:
                    f.write(',\n          ')
                    f.write('{} = {}\'d{}'.format(state, bits, count))
                    count += 1
                
            f.write(';\n\n')
            f.write('reg [{}:0]STATE, NEXT_STATE;\n\n'.format(bits-1))
                        
        f.write('\n//------------------------------------------------------------------\n')
        f.write('//                 -- Begin Declarations & Coding --                  \n')
        f.write('//------------------------------------------------------------------\n\n')

        f.write('always@(posedge clk or negedge rst)     // Determine STATE\n')
        f.write('begin\n\n')
        f.write('\tif (rst == 1\'b0)\n')
        f.write('\t\tSTATE <= #####;\n')
        f.write('\telse\n')
        f.write('\t\tSTATE <= NEXT_STATE;\n\n')
        f.write('end\n\n\n')
        
        f.write('always@(*)                              // Determine NEXT_STATE\n')
        f.write('begin\n')
        f.write('\tcase(STATE)\n\n')
        for state in states:
            f.write('\t{}:\n'.format(state))
            f.write('\tbegin\n')
            f.write('\t\tNEXT_STATE = #####;\n')
            f.write('\tend\n\n')
        if len(states) not in [0,1,2,4,8,16,32,64,128,256,512,1024,2048]:
            f.write('\tdefault:\n')
            f.write('\tbegin\n')
            f.write('\t\tNEXT_STATE = #####;\n')
            f.write('\tend\n\n')
        f.write('\tendcase\n')
        f.write('end\n\n\n')
        
        f.write('always@(posedge clk or negedge rst)     // Determine outputs\n')
        f.write('begin\n\n')
        f.write('\tif (rst == 1\'b0)\n')
        f.write('\tbegin\n\n')
        f.write('\t\t#####;\n\n')
        f.write('\tend\n\n')
        f.write('\telse\n')
        f.write('\tbegin\n')
        f.write('\t\tcase(STATE)\n\n')
        for state in states:
            f.write('\t\t{}:\n'.format(state))
            f.write('\t\tbegin\n')
            f.write('\t\t\t##### <= #####;\n')
            f.write('\t\tend\n\n')
        f.write('\t\tendcase\n')
        f.write('\tend\n\n')
        f.write('end\n\n\n')
        
        f.write('endmodule')
        
        
    
########################################################################## Initialize Tkinter GUI
root = Tk()   

########################################################################## Row 0: Name, clear button
Label(root, text='Verilog Module Name:').grid(row=0)
name = StringVar()
Entry(root, textvariable = name).grid(row=0, column=1)
Button(root, text='Clear All', command=clearAll).grid(row=0, column=2)

########################################################################## Row 1
Label(root).grid(row=1) # blank row for spacing

########################################################################## Rows 2-5: Checkboxes for selecting components
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
Checkbutton(root, text="Clock", variable=var1).grid(row=2, sticky=W)
Checkbutton(root, text="LED_Red", variable=var2).grid(row=3, sticky=W)
Checkbutton(root, text="LED_Green", variable=var3).grid(row=4, sticky=W)
Checkbutton(root, text="Button", variable=var4).grid(row=5, sticky=W)
Checkbutton(root, text="VGA", variable=var5).grid(row=2, column=1, sticky=W)
Checkbutton(root, text="Audio", variable=var6).grid(row=3, column=1, sticky=W)
Checkbutton(root, text="IR_Receiver", variable=var7).grid(row=4, column=1, sticky=W)
Checkbutton(root, text="RS_232", variable=var8).grid(row=5, column=1, sticky=W)
Checkbutton(root, text="Seven_Segment", variable=var9).grid(row=2, column=2, sticky=W)
Checkbutton(root, text="Switch", variable=var10).grid(row=3, column=2, sticky=W)
Checkbutton(root, text="LCD", variable=var11).grid(row=4, column=2, sticky=W)
Checkbutton(root, text="EX_IO", variable=var12).grid(row=5, column=2, sticky=W)

########################################################################## Row 6
Label(root).grid(row=6) # blank row for spacing

########################################################################## Row 7: Add states
Label(root, text='Enter state names separated by commas:').grid(row=7, columnspan=2, sticky=W)
Button(root, text='Add states', command=addStates).grid(row=7, column=2)

########################################################################## Row 8: Add states field
addstatestext = StringVar()
Entry(root, textvariable = addstatestext).grid(row=8, columnspan=3, sticky='we')

########################################################################## Row 9: States label
Label(root, text='States:').grid(row=9, sticky=W)

########################################################################## Row 10: States text
statesText = Text(root, width=50, height = 5)
statesText.grid(row=10, columnspan=3, sticky='we')
statesText.config(wrap=WORD)
statesText.config(state=DISABLED)

########################################################################## Row 11
Label(root).grid(row=11) # blank row for spacing

########################################################################## Row 12: Create/done button
Button(root, text='Done', command=done).grid(row=12, column=1, sticky='we')

########################################################################## Run Tkinter GUI
root.mainloop()



