import io
from core.logistics_facade import LogisticsFacade

file_path = 'use_cases/use_case5.txt'
logistics_facade = LogisticsFacade()

with open(file_path, 'r') as file:
    line = file.readline().strip()
    output = []


    while line != 'exit':
        try:
            output_buffer = io.StringIO()
            exec(f"output_buffer.write({line})", {"logistics_facade": logistics_facade}, {"output_buffer": output_buffer})
            output.append(output_buffer.getvalue())
            
        except Exception as err:
            output.append(str(err)) # print output
        
        line = file.readline().strip() 

print('\n'.join(output))
