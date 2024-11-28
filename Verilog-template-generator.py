# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 08:30:58 2024

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Final Pyrhon Project - First Release - Only writing the design module template
"""

"""
Verilog design module template creation
"""

import os #To handle os directory accessing
import re #For regular expression
import random #random generation

def generate_binary_string(width):
    return ''.join(random.choice('01') for _ in range(width))

def is_binary_string(s): #check if the input is binary
    return all(char in '01' for char in s)

#is_valid_verilog_identifier?
def is_valid_verilog_identifier(identifier):
    # Check if the string consists only of letters, dollar signs, and underscores
    if not re.match("^[a-zA-Z_\$][a-zA-Z0-9_\$]*$", identifier):
        return False
    
    # Check if the string does not have a space
    if ' ' in identifier:
        return False
    
    # Check if the string is not a Verilog reserved word
    verilog_reserved_words = set([
        'always', 'and', 'assign', 'automatic', 'before', 'begin', 'buf', 'bufif0', 'bufif1',
        'case', 'casex', 'casez', 'cmos', 'deassign', 'default', 'defparam', 'disable', 'edge',
        'else', 'end', 'endcase', 'endfunction', 'endmodule', 'endprimitive', 'endspecify', 'endtable',
        'endtask', 'event', 'for', 'force', 'forever', 'fork', 'function', 'highz0', 'highz1',
        'if', 'ifnone', 'initial', 'inout', 'input', 'integer', 'join', 'large', 'localparam',
        'macromodule', 'medium', 'module', 'nand', 'negedge', 'nmos', 'nor', 'not', 'notif0',
        'notif1', 'or', 'output', 'parameter', 'pmos', 'posedge', 'primitive', 'pull0', 'pull1',
        'pulldown', 'pullup', 'rcmos', 'real', 'realtime', 'reg', 'release', 'repeat', 'rnmos',
        'rpmos', 'rtran', 'rtranif0', 'rtranif1', 'scalared', 'small', 'specify', 'specparam',
        'strong0', 'strong1', 'supply0', 'supply1', 'table', 'task', 'time', 'tran', 'tranif0',
        'tranif1', 'tri', 'tri0', 'tri1', 'triand', 'trior', 'trireg', 'vectored', 'wait',
        'wand', 'wor', 'while', 'wire', 'wor', 'xnor', 'xor'
    ])
    
    if identifier.lower() in verilog_reserved_words:
        return False
    
    # If all checks pass, the identifier is valid
    return True

# Check if the the choice is only one or two
def is_valid_choice12(choice):
    if choice.isdigit():
        if choice == '1' or choice == '2':
            return True
        else:
            return False
    else:
        print("Input should be only numeric.")
        return False
    
    
 
# Check if the the choice is only one or two
def is_only_digit(choice):
    if choice.isdigit():
        return True
    else:
        print("Input should be only numeric.")
        return False
    
#Lists for ports declaration
ports_name = []
ports_dir = []
ports_MSB = []
ports_LSB = []

#List to hold previous used port names
names_used = [] 

#check if it is the first entered port or not (For Combinationatiol block)
first_port = '0'
print("This wizard will guide you through the creation of a verilog design module template")
print("and its testbench")

print("\nTo create a new verilog module template with its testbench, you will need to provide")
print("a name for the design module file and a location for both files (the design and the testbench)")


#check the file extension and naming
while (True):
    design_name = input("\nEnter design module name(with (.v) extension): ") #save the design module name
    if not design_name[-2:] == ".v":
        print("wrong file extension!")
        continue
    
    if is_valid_verilog_identifier(design_name[:-2]):
        break
    else:
        print("Invalid file naming!")
        continue

"""
open the design file in the specifiend location
"""
# Get the file path from the user
while True:
    path = input("\nEnter the design file path: ")
    if path == "":
        continue
    else:
        break

files_path = os.path.join(path, design_name) 

# Ensure the directory exists
directory = os.path.dirname(files_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Open the file for writing
try:
    with open(files_path, 'w') as file:
        # Perform any write operations here    
        print(f"File '{files_path}' has been created.")
        
        #write module header name
        design_name = design_name[:-2] #wrong: change it
        line_write = "module " +design_name + "("
        file.write(line_write)
        
        #Add I/O ports
        print("Define module and specify I/O ports to be added to your design")
        
        
        #Is it sequential or combainational module?
        print("\nIs it sequential or combainational module?")
        print("1- Sequential")
        print("2- Combinational")
        
        #check if the input is valid or not
        while(True):
            SeqorComb = input("Eneter your choice: ")
            if is_valid_choice12(SeqorComb):
                break
            else:
                print("Wrong choice!")
        
        
        if SeqorComb == '1':
            #Enter clock name
            while (True):#check the port naming
                clock_name = input("Enter clock name: ")
                if is_valid_verilog_identifier(clock_name):
                    break
                else:
                    print("Invalid port naming!")
                    continue
                
            names_used.append(clock_name);#to not use this name again
                
            line_write = "\n\tinput " + clock_name
            file.write(line_write)
            
            #For Testbench
            ports_name.append(clock_name)
            ports_dir.append("input")
            ports_MSB.append("0")
            ports_LSB.append("0")
            
            #Is it psitive or negative edge triggerd?
            print("\nIs it psitive or negative edge triggerd?")
            print("1- Positive")
            print("2- Negative")
            
            
            #check if the input is valid or not
            while(True):
                PosorNegclk = input("Eneter your choice: ")#save this variable for later use
                if is_valid_choice12(PosorNegclk):
                    break
                else:
                    print("Wrong choice!")
            
            #Enter reset name
            while (True):#check the port naming
                reset_name = input("Enter the reset signal name: ")#saved for later use
                
                if reset_name in names_used:#make sure this name is not used before
                    print("error: {",reset_name,"} has already been declared in this scope.")
                    continue
                
                if is_valid_verilog_identifier(reset_name):
                    break
                else:
                    print("Invalid port naming!")
                    continue
            
            #For Testbench
            ports_name.append(reset_name)
            ports_dir.append("input")
            ports_MSB.append("0")
            ports_LSB.append("0")   
                
            names_used.append(reset_name);#to not use this name again    
                
            
            #Is it Synchronous or Asynchronous reset?
            print("\nIs it Synchronous or Asynchronous reset?")
            print("1- Synchronous")
            print("2- Asynchronous")
            
            #check if the input is valid or not
            while(True):
                SynorAsyn = input("Eneter your choice: ")#saved for later use
                if is_valid_choice12(SynorAsyn):
                    break
                else:
                    print("Wrong choice!")
            
            #Is it Positive or Negative reset?
            print("\nIs it Positive or Negative reset?")
            print("1- Positive")
            print("2- Negative")
                        
            #check if the input is valid or not
            while(True):
                PosorNegRes = input("Eneter your choice: ")#saved for later use
                if is_valid_choice12(PosorNegRes):
                    break
                else:
                    print("Wrong choice!")  
                    
            line_write = ",\n\tinput " + reset_name + ","
            file.write(line_write)
        
        #Enter Design input ports
        print("I/O ports definitions:")
        i=0#iterator
        first_port = '0'#To check if is is the first port or not
        while(True):
            
            #Enter port name
            while (True):#check the port naming
                port_name = input("\nEnter port name: ")
                
                if port_name in names_used:#make sure this name is not used before
                    print("error: {",port_name,"} has already been declared in this scope.")
                    continue
                
                if is_valid_verilog_identifier(port_name):
                    break
                else:
                    print("Invalid port naming!")
                    continue
                
            
            names_used.append(port_name);#to not use this name again      
            ports_name.append(port_name)#saved to be used in the testbench file creation
            
            
            
            #Enter port direction
            while (True):#check the port naming
                port_dir = input("Enter port direction: ")
                if port_dir == "input" or port_dir == "output":
                    break
                else:
                    print("Invalid port direction!")
                    continue
                
            ports_dir.append(port_dir)#saved to be used in the testbench file creation
            
            #IS it a bus
            print("\nIs it a bus or a signal?")
            print("1- Bus")
            print("2- Signal")
            
            #check if the input is valid or not
            while(True):
                BusorSig = input("Enter your choice: ")
                if is_valid_choice12(BusorSig):
                    break
                else:
                    print("Wrong choice!") 
            
            if BusorSig == '1':
                #check if the input is valid or not
                while(True):
                    MSB = input("Enter MSB: ") #input MSB
                    if is_only_digit(MSB):
                        break
                    else:
                        print("Wrong choice!") 
                        
                ports_MSB.append(MSB)#saved to be used in the testbench file creation
                
                #check if the input is valid or not
                while(True):
                    LSB = input("Enter LSB: ") #input LSB
                    if is_only_digit(LSB):
                        break
                    else:
                        print("Wrong choice!")  
                        
                ports_LSB.append(LSB)#saved to be used in the testbench file creation
                
                if first_port == '0':
                    line_write = "\n\t" + port_dir + " [" + MSB + ":" + LSB + "] " + port_name
                else:
                    line_write = ",\n\t" + port_dir + " [" + MSB + ":" + LSB + "] " + port_name
                    
                file.write(line_write)  
                first_port = '1'   
                
            else:
                if first_port == '0':
                    line_write = "\n\t" + port_dir + " " + port_name
                else:
                    line_write = ",\n\t" + port_dir + " " + port_name
                    
                first_port = '1'
                file.write(line_write)
                
                ports_MSB.append('0')#saved to be used in the testbench file creation
                ports_LSB.append('0')#saved to be used in the testbench file creation
                
            #another input?
            addport = input("\nAdd another port? (yes/no (or any other input)): ")
            lowercase_addport = addport.lower()
            
            if lowercase_addport == "yes":
                continue
            else:
                break
            
        file.write("\n\t);\n")
        file.write("\n\t//Contents of the module")
        
        #Write the always block
        if SeqorComb == '1':
            line_write = "\n\talways @("
            file.write(line_write)
            
            #positive or negative edge clock?
            if PosorNegclk == '1':
                line_write = "posedge " + clock_name
                file.write(line_write)    
            else:
                line_write = "negedge " + clock_name
                file.write(line_write)
            
            #Syn/Asyn & positive or negative reset?
            if SynorAsyn == '1':
                line_write = ")"
                file.write(line_write)
                
                if PosorNegRes == '1':
                    file.write("\n\tbegin")
                    line_write = "\n\t\tif(" + reset_name + ")"
                    file.write(line_write)
                else:
                    file.write("\n\tbegin")
                    line_write = "\n\t\tif(!" + reset_name + ")"
                    file.write(line_write)
            else:
                if PosorNegRes == '1':
                    line_write = " or posedge " + reset_name + ")"
                    file.write(line_write)
                    file.write("\n\tbegin")
                    line_write = "\n\t\tif(" + reset_name + ")"
                    file.write(line_write)
                else:
                    line_write = " or negedge " + reset_name + ")"
                    file.write(line_write)
                    file.write("\n\tbegin")
                    line_write = "\n\t\tif(!" + reset_name + ")"
                    file.write(line_write)
                    
            file.write("\n\t\tbegin")
            file.write("\n\t\t\t//Reset condition")
            file.write("\n\t\tend")
            file.write("\n\t\telse")
            file.write("\n\t\tbegin")
            file.write("\n\t\t\t//Non-Reset condition")
            file.write("\n\t\tend")
            file.write("\n\tend")
        else:
            file.write("\n\talways @(*)")
            file.write("\n\tbegin")
            file.write("\n\t\t//combinational logic here")
            file.write("\n\tend")
            
        file.write("\n\nendmodule")
        print("\nYour desin modulefile  is created!")
        #SeqorComb clock_name PosorNegclk reset_name SynorAsyn PosorNegRes    
except IOError as e:
    print(f"Error: {e}")
    
    
"""
Verilog Testbench template creation for the associative design module
"""

#check if the input is valid or not
cases_userinput = '0'
while(True):
    Testcases = input("How many testcases you need: ")
    
    if Testcases == "":#Check if no input
        Testcases = '2'
        print("Only two testcases will be generated")
        break
    
    if is_only_digit(Testcases):#check if the input is valis or not
        cases_userinput = '1'
        break
    else:
        print("Invalid choice!")
 
#Ask for clock period
while(True):
    clock_period = input("Enter Clock period in ns: ")
    
    if is_only_digit(clock_period) == True:
        clock_period = clock_period
        break
    else:
        print("Wrong Choice!")
        continue
    
    if is_only_digit(Testcases):#check if the input is valis or not
        break
    else:
        print("Invalid choice!")
 
Testbench_name = design_name + "_TB" + ".v"
#create the testbench file at the same location with the design file
files_path = os.path.join(path, Testbench_name) 
# Ensure the directory exists
directory = os.path.dirname(files_path)
if not os.path.exists(directory):
    os.makedirs(directory)

try:
    with open(files_path, 'w') as file:
        # Perform any write operations here    
        print(f"File '{files_path}' has been created and written to.")
        
        #write module header name
        Testbench_name = Testbench_name[:-2] 
        line_write = "module " + design_name + "_TB();"
        file.write(line_write)
        
        #Write Testbench signals(Inputs)
        file.write("\n\n\t//Inputs")
        
        for index, value in enumerate(ports_dir):
            if value == "input":#xheck if it was input or output
                line_write = "\n\treg "
                
                if not ports_MSB[index] == '0':#check if it is bus or a signal
                    line_write = line_write + "["+ports_MSB[index] + ":" + ports_LSB[index] + "]"
                
                line_write = line_write + " " + ports_name[index] + "_TB;"
                file.write(line_write)

        #Write Testbench signals(Outputs)
        file.write("\n\n\t//Outputs")
        
        for index, value in enumerate(ports_dir):
            if value == "output":#xheck if it was input or output
                line_write = "\n\twire "
                
                if not ports_MSB[index] == '0':#check if it is bus or a signal
                    line_write = line_write + "["+ports_MSB[index] + ":" + ports_LSB[index] + "] "
                
                line_write = line_write + ports_name[index] + "_TB;"
                file.write(line_write)
              
        #design module instantiation
        file.write("\n\n\t//Instantiate the module\n")
        line_write = "\t" + design_name + " uut (\n" #header of instantiation
        file.write(line_write)
        
        for index, value in enumerate(ports_name):#ports(module)+signals(testbench) wiring
            line_write = "\t\t." + value + "(" + value + "_TB)"
            
            # Check if it's the last iteration
            if index == len(ports_name) -1:
                line_write = line_write + "\n"
                file.write(line_write)
                break
            else:
                line_write = line_write + ",\n"
                file.write(line_write)
            
        file.write("\t);\n")
        
        
        if SeqorComb == '1':#if Sequential
            #Clock generation
            file.write("\t//Clock generation\n")
            file.write("\tinitial begin\n")
            line_write = "\t\t"+ ports_name[0] + "_TB = 0;\n"
            file.write(line_write)
            line_write = "\t\t"+ "forever #" + str(round(int(clock_period) / 2)) + " " + ports_name[0] + "_TB = ~" + ports_name[0] + "_TB;\n"
            file.write(line_write)
            file.write("\tend\n\n")
             
        """
        Stimulus Generation
        """
        file.write("\t//Stimulus\n")
        file.write("\tinitial begin\n")
        
        
        if SeqorComb == '1':#if Sequential
            #*******
            #Reset initialization and input signals intialization
            #*******
            file.write("\t\t//Input initialization\n")
            
            #Initialize reset
            line_write = "\t\t" + ports_name[1] + "_TB = "
            if (PosorNegRes == '1'):#initial reset value
                resvalue = '1'
            else:
                resvalue = '0'
                
            line_write = line_write + resvalue + ";\n"
            file.write(line_write)
        
        #initialize inputs
        for index, value in enumerate(ports_dir):#ports(module)+signals(testbench) wiring
            if SeqorComb == '1':#if Sequential
                if index == 0 or index == 1:#bypass clock and reset
                    continue
                
            if value == "input":#xheck if it was input or output
                line_write = "\t\t" + ports_name[index] + "_TB = 0;\n"
                file.write(line_write)
        
        if SeqorComb == '1':#if Sequential
            #Release Reset Condition
            line_write = "\n\t\t//Release Reset Signal\n\t\t#" + str(2 * round(int(clock_period) / 2)) + "\n"
            file.write(line_write)
            
            if (resvalue == '1'):#initial reset value
                resvalue = '0'
            else:
                resvalue = '1'
            
            line_write = "\t\t" + ports_name[1] + "_TB = "
            line_write = line_write + resvalue + ";\n"
            file.write(line_write)
        
        #*******
        #Input Stimulus
        #*******
        for j in range (int(Testcases)):
            
            if cases_userinput == '1':#the inputs are from the user
                line_word = "\nTest case number " + str(j+1) + ":" 
                print(line_word)
            
            line_write = "\t\t#" + str(2 * round(int(clock_period) / 2)) + "\n"
            file.write(line_write)
            
            if cases_userinput == '1':#the inputs are from the user
                for index, value in enumerate(ports_dir):#loop over inputs
                    if SeqorComb == '1':#if Sequential
                        if index == 0 or index == 1:#bypass clock and reset
                            continue
                    
                    if value == "input":#check if it was input or output
                        line_write = "\nEnter input port{" + ports_name[index] +"} "
                        
                        if not ports_MSB[index] == '0':#check if it is bus or a signal
                            line_write = line_write + "["+ports_MSB[index] + ":" + ports_LSB[index] + "]"
                        
                        line_write = line_write + " " + ports_name[index] + "_TB: "
                        
                        
                        while True:
                            bits = input(line_write)#print to screen and get input
                            
                            if is_binary_string(bits):#check if it is bit input or not
                                if len(bits) == (int(ports_MSB[index]) - int(ports_LSB[index]) + 1):
                                    line_write = "\t\t" + ports_name[index] + "_TB = " + str(int(ports_MSB[index]) - int(ports_LSB[index]) + 1) + "'b" +  bits + ";\n"
                                    file.write(line_write)
                                    break
                                else:
                                    print("Wrong input size!")
                                    continue
                                
                                break
                            else:
                                print("Wrong input (only ones and zeros!)")
                                continue
                        
            else:#the inputs are generated randomly
                
                for index, value in enumerate(ports_dir):#loop over inputs
                
                    if SeqorComb == '1':#if Sequential
                        if index == 0 or index == 1:#bypass clock and reset
                            continue
                    
                    if value == "input":
                        bits = generate_binary_string(int(ports_MSB[index]) - int(ports_LSB[index]) + 1)
                        line_write = "\t\t" + ports_name[index] + "_TB = " + str(int(ports_MSB[index]) + int(ports_LSB[index]) + 1) + "'b" +  bits + ";\n"
                        
                        file.write(line_write)
        
        file.write("\n\t\t//Add more stimulus as needed\n\n")
        file.write("\t\t//End simulation after some time\n")
        file.write("\t\t#100 $finish;\n")
        file.write("\tend\n")
        file.write("\nendmodule\n")   
        
        print("\nYour Testbench file is generated")
            
                
except IOError as e:
    print(f"Error: {e}")
    
    #seqasynnegclknegrst.v