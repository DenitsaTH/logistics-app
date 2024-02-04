from core.logistics_facade import LogisticsFacade


file_path = 'client_code.txt'
logistics_facade = LogisticsFacade()

with open(file_path, 'r') as file:
    line = file.readline()

    while line: 
        output = []

        try:
            output.append(exec(line))
        except Exception as err:
            output.append(str(err))


print('\n'.join(output))
