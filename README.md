# verilog-template-generator
A Python-based tool designed to simplify the creation of Verilog designs and testbenches. By answering a series of straightforward questions, users can generate customizable, syntax error-free Verilog templates for both sequential and combinational designs, along with their corresponding testbenches.

## Features

- **Automated Code Generation**: Automatically generate Verilog templates for sequential and combinational designs.
- **Customizable Inputs**: Choose the number of inputs and outputs, as well as design parameters.
- **Testbench Creation**: Generate testbenches with user-defined test cases.
- **Syntax Error-Free**: The tool ensures that all generated code is syntax-error free, reducing manual debugging time.
- **Supports Sequential and Combinational Designs**: Select the design type based on your needs.

## Installation

To install **VeriGen**, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/verilog-template-generator.git

2. **Navigate to the project directory**:
   ```bash
   cd verilog-template-generator

3. **Install dependencies:** If you don't already have Python 3 installed, please install it. This tool only requires Python, and no additional dependencies are needed beyond Python itself.

## Usage

1. **Run the script:**
   To start using verilog-template-generator, run the main Python script from the command line:
   ```bash
   python verilog-template-generator.py
   
3. **Answer the prompts:**
   The script will ask you a series of questions to define your Verilog design

4. **Code Generation:**:
   Once you've answered the questions, verilog-template-generator will automatically generate.

3. **Customization:**:
   The generated Verilog templates can be further customized to meet specific project requirements.

## Example

Once you run the script, here's an example of what the generated files might look like:

1. **Verilog Design (design.v): For a sequential design, the generated Verilog code could look like this:**:
   ```
   module design(
	input clk,
	input rst,
	input [5:0] A,
	input B,
	output C
	);

	//Contents of the module
	always @(posedge clk)
	begin
		if(rst)
		begin
			//Reset condition
		end
		else
		begin
			//Non-Reset condition
		end
	end

   endmodule
   ```

2. **Testbench (design_TB.v): A simple testbench for the design:**:
   ```
   module design_TB();

	//Inputs
	reg  clk_TB;
	reg  rst_TB;
	reg [5:0] A_TB;
	reg  B_TB;

	//Outputs
	wire C_TB;

	//Instantiate the module
	Design uut (
		.clk(clk_TB),
		.rst(rst_TB),
		.A(A_TB),
		.B(B_TB),
		.C(C_TB)
	);
	//Clock generation
	initial begin
		clk_TB = 0;
		forever #25 clk_TB = ~clk_TB;
	end

	//Stimulus
	initial begin
		//Input initialization
		rst_TB = 1;
		A_TB = 0;
		B_TB = 0;

		//Release Reset Signal
		#50
		rst_TB = 0;
		#50
		A_TB = 6'b001100;
		B_TB = 1'b1;
		#50
		A_TB = 6'b110011;
		B_TB = 1'b1;
		#50
		A_TB = 6'b001110;
		B_TB = 1'b1;

		//Add more stimulus as needed

		//End simulation after some time
		#100 $finish;
	end

   endmodule
   ```

## Contributing

Contributions are welcome! If you'd like to improve the project or add new features, feel free to submit a pull request.

## Contact

For any questions or issues, feel free to reach out to the project maintainer:

Name: Mohamed Khalaf

Email: khalafmohamed9821@gmail.com

GitHub: @M-Khalf

