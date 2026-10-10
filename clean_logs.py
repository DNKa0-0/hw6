def parse_and_clean(line:str):
    not_stripped_parameters = line.split("|")
    parameters = []
    for parameter in not_stripped_parameters:
        parameters.append(parameter.strip())
    if len(parameters) != 5:
        return None
    elif parameters[4] != "ACTIVE":
        return None
    return parameters

def celsius_converter(f_temp:str):
    if f_temp == "ERROR" or f_temp == "N/A":
        return f_temp
    c_temp = ((float(f_temp) - 32) * 5) / 9
    return round(c_temp, 2)

with open ("environmental_raw.txt") as input_file:
    with open ("environmental_output.csv", "w") as output_file:
        error_line = 0
        for line in input_file:
            clean_line = parse_and_clean(line)
            if clean_line == None:
                error_line += 1
            else:
                f_temp = clean_line[2]
                c_temp = celsius_converter(f_temp)
                clean_line[2]= str(c_temp)
                output_file.write(",".join(clean_line)+"\n")

print(f"Number of invalid lines: {error_line}")


    
