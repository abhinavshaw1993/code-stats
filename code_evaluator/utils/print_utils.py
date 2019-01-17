from tabulate import tabulate

def table(data, header, format='orgtbl'):
    """
    Return Printable table object with the heder and data.
    1. Hearder - List of headers
    2. Data - List of lists containing the data to be tabulated.
    """
    return  tabulate(data, header, tablefmt=format)

def convert_dict_to_list(output_dict):
    output_list = []
    for k in output_dict.keys():
        output_list.append([k, output_dict[k]])

    return output_list
