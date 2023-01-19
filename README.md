# Computer Architecture (17 bit)

This is a 17 bit computer architecture that supports 32 unique instructions. The project also includes an assembler written in Python.

## Registers
The register file will contain 32 registers, among which the first one will be a constant value of 0.

The registers will be named R0,R1,...,R31 and shall be used with these names in assembly.

## R type instructions
|Opcode |Register 1 ($1) |Register 1 ($2)  |Register 1 ($3) |
---| --- | ---| ---|
5 bit | 4 bit | 4 bit | 4 bit|

## I type instructions
|Opcode |Register 1 ($1) |Register 1 ($2)  |Immediate (imm) |
---| --- | ---| ---|
5 bit | 4 bit | 4 bit | 4 bit|

## J type instructions
|Opcode |Address |
---| --- |
5 bit | 12 bit|

## ISA

|Instruction |Opcode |Assembly  |Machine |Meaning |
--- | --- | ---| ---| ---|
|and|00000|and $1,$2,$3|and $1,$2,$3|$1=$2&$3|
|or|00001|or $1,$2,$3|or $1,$2,$3|$1=$2\|$3|
|not|00010|not $1,$2|not $1,$2,R0|$1=!$2|
|nand|00011|nand $1,$2,$3|nand $1,$2,$3|$1=!($2&$3)|
|nor|00100|nor $1,$2,$3|nor $1,$2,$3|$1=($2\|$3)|
|xor|00101|xor $1,$2,$3|xor $1,$2,$3|$1=$2^$3|
|add|00110|add $1,$2,$3|add $1,$2,$3|$1=$2+$3|
|subtract|00111|sub $1,$2,$3|sub $1,$2,$3|$1=$2-$3|
|multiply|01000|mul $1,$2,$3|mul $1,$2,$3|$1=$2*$3|
|divide|01001|div $1,$2,$3|div $1,$2,$3|$1=$2/$3|
|remainder|01010|rem $1,$2,$3|rem $1,$2,$3|$1=$2%$3|
|shift left logical|01011|sll $1,$2,imm|sll $1,$2,immediate|$1=$2<<imm|
|shift right logical|01100|srl $1,$2,imm|srl $1,$2,imm|$1=$2>>imm|
|add immediate|01101|addi $1,$2,imm|addi $1,$2,imm|$1=$2+imm|
|subtract immediate|01111|subi $1,$2,imm|subi $1,$2,imm|$1=$2-imm|
|load word|01111|lw $1,$2,imm|lw $1,$2,imm|$1 = MEMORY[$2+imm]|
|store word|10000|sw $1,$2,imm|sw $1,$2,imm|MEMORY[$2+imm]=$1|
|branch if equal|10001|beq $1,$2,imm|beq $1,$2,imm|if($1==$2) goto PC+imm|
|branch if not equal|10010|bne $1,$2,imm|bne $1,$2,imm|if($1!=$2) goto PC+imm|
|branch if greater|10011|bgt $1,$2,imm|bgt $1,$2,imm|if($1>$2) goto PC+imm|
|branch if greater equal|10100|bge $1,$2,imm|bge $1,$2,imm|if($1>=$2) goto PC+imm|
|branch if less than|10101|blt $1,$2,imm|blt $1,$2,imm|if($1<$2) goto PC+imm|
|branch if less equal|10110|ble $1,$2,imm|ble $1,$2,imm|if($1<=$2) goto PC+imm|
|set if equal|10111|sle $1,$2,$3|sle $1,$2,$3|if($2==$3)$1=1 else $1=0|
|set if less than|11000|slt $1,$2,$3|slt $1,$2,$3|if($2<$3)$1=1 else $1=0|
|set if greater|11001|sgt $1,$2,$3|sgt $1,$2,$3|if($2>$3)$1=1 else $1=0|
|jump|11010|jump imm|jump imm|goto imm|
|jump register|11011|jumpr $1|jumpr R0,$1,R0|goto $1|
|jump if carry|11100|jc $1|jc R0,$1,R0|if(alu_carry==1) goto $1|
|jump if zero|11101|jz $1|jz R0,$1,R0|if(alu_output==0) goto $1|
|input|11110|in $1|in $1,R0,R0|$1=user_input|
|output|11111|out $1|out R0,$1,R0|display $1|

# Pseudo Instructions
The assembler will support all the machine instructions along with the pseudo instructions listed below. These pseudo instructions have been provided to add some syntactic sugar to the language. The assembler will substitute these instructions with equivalent machine instructions.
## These instructions are provided by the assembler
|Instruction| Assembly  |Machine |Meaning |
--- | --- | ---| ---|
|mov|mov $1, $2|add $1,$2,R0|$1=$2|
load immediate|lwi $1, imm|addi $1,R0,imm|$1=imm|
increment|inc $1|addi $1,$1,1|$1=$1+1|
decrement|dec $1|subi $1,$1,1|$1=$1-1|
|no operation|nop|AND R0,R0,R0|-|