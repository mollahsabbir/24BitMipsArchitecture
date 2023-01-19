from instructionsdetails import assembly_details, InstructionsDetails, InstructionType

COMMENT_SEP = ";"
IGNORE_REGISTER = "R0"
TOTAL_REGISTERS = 16

class InvalidOpcodeException(Exception):
    def __init__(self, opcode, *args):
        super().__init__(args)
        self.opcode = opcode

    def __str__(self):
        return f'{self.opcode} is not a valid opcode.'
    
class InvalidRegisterException(Exception):
    def __init__(self, register, *args):
        super().__init__(args)
        self.opcode = register

    def __str__(self):
        return f'{self.register} is not a valid register.'
    
class CodeConverter:
    
    def convert(self, asm_code_lines:list[str]) -> tuple[list[str]]:
        cleaned_asm = self._clean_assembly(asm_code_lines)
        machine_code = self._assembly_to_machine(cleaned_asm, assembly_details)
        
        return (machine_code, ["placeholder"])
        
    def _clean_assembly(self, asm_code_lines:list[str])->list[str]:
        cleaned_asm_lines: list[str] = []
        for line in asm_code_lines:
            head, sep, tail = line.partition(COMMENT_SEP)
            if len(head.strip()) != 0:
                cleaned_asm_lines.append(head.strip())
                
        return cleaned_asm_lines

    def _assembly_to_machine(self, asm_code:list[str], 
                        assembly_details:dict[str,InstructionsDetails]) -> list[str]:
        machine_code: list[str] = []
        for line in asm_code:
            opcode_asm, params = line.split(" ", 2)
            
            if opcode_asm in assembly_details.keys():
                opcode_machine = self._parse_opcode(opcode_asm)
                structured_params = self._structure_assembly(opcode_asm, params)
                params_machine = self._params_to_machine(opcode_asm, structured_params)
                machine_code.append([opcode_machine, params_machine])
            else:
                raise InvalidOpcodeException(opcode_asm)
        
        return machine_code
    
    def _parse_opcode(self, opcode_asm:str) -> str:
        if assembly_details[opcode_asm].pseudo_substitute:
            opcode_machine = assembly_details[opcode_asm].pseudo_substitute
        else:
            opcode_machine = assembly_details[opcode_asm].machine_code
            
        return opcode_machine
        
    def _structure_assembly(self, opcode_asm:str, params:str) -> str:
        splitted = params.split(",")
        while len(splitted)!=3:
            splitted.append("")
   
        for rule in assembly_details[opcode_asm].copy_registers_rules:
            splitted[rule[1]] = splitted[rule[0]]
            
        for rule in assembly_details[opcode_asm].swap_registers_rules:
            splitted[rule[0]], splitted[rule[1]] = splitted[rule[1]], splitted[rule[0]]
            
        for i in assembly_details[opcode_asm].ignore_registers_indices:
            splitted[i] = IGNORE_REGISTER
            
        splitted = [i for i in splitted if i!=""]
        
        if assembly_details[opcode_asm].imm_value:
            splitted.append(assembly_details[opcode_asm].imm_value)
        
        return splitted
    
    def _params_to_machine(self, opcode_asm:str, params:list[str]) -> list[str]:
        instruction_type = assembly_details[opcode_asm].instruction_type
        param_machine = []
        
        if instruction_type==InstructionType.R or       \
                instruction_type==InstructionType.IO or \
                instruction_type==InstructionType.PSEUDO_R:
            param_machine.append(self._register_binary(params[0]))
            param_machine.append(self._register_binary(params[1]))
            param_machine.append(self._register_binary(params[2]))
        elif instruction_type==InstructionType.I or       \
                instruction_type==InstructionType.PSEUDO_I:
            param_machine.append(self._register_binary(params[0]))
            param_machine.append(self._register_binary(params[1]))
            param_machine.append(self._immediate_to_binary(params[2], 4))
        elif instruction_type==InstructionType.J:
            param_machine.append(self._immediate_to_binary(params[0], 12))
        
        return param_machine
        
    def _register_binary(self, register:str) -> str:
        register_num = int(register[1:])
        
        if register_num<0 or register_num>=TOTAL_REGISTERS:
            raise InvalidRegisterException(register)
        
        return f'{register_num:04b}'
    
    def _immediate_to_binary(self, imm, bin_length):
        imm = int(imm)
        return f'{imm:0{bin_length}b}'[0:bin_length]