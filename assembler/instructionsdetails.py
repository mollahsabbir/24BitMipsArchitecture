from enum import Enum

class InstructionType(Enum):
    R = 1
    I = 2
    J = 3
    IO = 4
    PSEUDO_R = 5
    PSEUDO_I = 6

class InstructionsDetails:
    
    def __init__(self,
                machine_code: str = None,
                instruction_type: InstructionType = InstructionType.R,
                ignore_registers_indices: list[int] = [],
                swap_registers_rules: list[list[int]] = [],
                copy_registers_rules: list[list[int]] = [],
                imm_value: int = None,
                pseudo_substitute: str = None):
        self.machine_code = machine_code
        self.instruction_type = instruction_type
        self.ignore_registers_indices = ignore_registers_indices
        self.swap_registers_rules = swap_registers_rules
        self.copy_registers_rules = copy_registers_rules
        self.imm_value = imm_value
        self.pseudo_substitute = pseudo_substitute

assembly_details = {
    "and": InstructionsDetails("00000", InstructionType.R),
    "or": InstructionsDetails("00001", InstructionType.R),
    "not": InstructionsDetails("00010", InstructionType.R, [2]),
    "nand": InstructionsDetails("00011", InstructionType.R),
    "nor": InstructionsDetails("00100", InstructionType.R),
    "xor": InstructionsDetails("00101", InstructionType.R),
    "add": InstructionsDetails("00110", InstructionType.R),
    "sub": InstructionsDetails("00111", InstructionType.R),
    "mul": InstructionsDetails("01000", InstructionType.R),
    "div": InstructionsDetails("01001", InstructionType.R),
    "rem": InstructionsDetails("01010", InstructionType.R),
    "sll": InstructionsDetails("01011", InstructionType.I),
    "srl": InstructionsDetails("01100", InstructionType.I),
    "addi": InstructionsDetails("01101", InstructionType.I),
    "subi": InstructionsDetails("01111", InstructionType.I),
    "lw": InstructionsDetails("01111", InstructionType.I),
    "sw": InstructionsDetails("10000", InstructionType.I),
    "beq": InstructionsDetails("10001", InstructionType.I),
    "bne": InstructionsDetails("10010", InstructionType.I),
    "bgt": InstructionsDetails("10011", InstructionType.I),
    "bge": InstructionsDetails("10100", InstructionType.I),
    "blt": InstructionsDetails("10101", InstructionType.I),
    "ble": InstructionsDetails("10110", InstructionType.I),
    "sle": InstructionsDetails("10111", InstructionType.R),
    "slt": InstructionsDetails("11000", InstructionType.R),
    "sgt": InstructionsDetails("11001", InstructionType.R),
    "jump": InstructionsDetails("11010", InstructionType.J),
    "jumpr": InstructionsDetails("11011", InstructionType.R, [0,2], [[0,1]]),
    "jc": InstructionsDetails("11100", InstructionType.R, [0,2], [[0,1]]),
    "jz": InstructionsDetails("11101", InstructionType.R, [0,2], [[0,1]]),
    "in": InstructionsDetails("11110", InstructionType.IO, [1,2]),
    "out": InstructionsDetails("11111", InstructionType.IO, [0,2], [[0,1]]),
    "mov": InstructionsDetails(None, InstructionType.PSEUDO_R, [2], pseudo_substitute="add"),
    "lwi": InstructionsDetails(None, InstructionType.PSEUDO_I, [1], pseudo_substitute="addi"),
    "inc": InstructionsDetails(None, InstructionType.PSEUDO_I, [1], copy_registers_rules=[[0,1]] , pseudo_substitute="addi",imm_value=1),
    "dec": InstructionsDetails(None, InstructionType.PSEUDO_I, [1], copy_registers_rules=[[0,1]] , pseudo_substitute="subi",imm_value=1),
    "nop": InstructionsDetails(None, InstructionType.PSEUDO_R, ignore_registers_indices=[0,1,2], pseudo_substitute="and"),
}