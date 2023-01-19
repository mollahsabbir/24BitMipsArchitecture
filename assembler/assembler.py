import sys
from codeconverter import CodeConverter, InvalidOpcodeException

def main():
    
    if len(sys.argv) != 2:
        print("Please provide an assembly file.")
        print("[Usage] >> python assemble.py <asm_code_file_dir>")

    asm_code_file = sys.argv[1]
    with open(asm_code_file, "r") as asm_code_lines:
        code_converter: CodeConverter = CodeConverter()
        try:
            machine = code_converter.convert(asm_code_lines)
            print(machine)
        except InvalidOpcodeException as ex:
            print(ex)
        
if __name__=="__main__":
    main()