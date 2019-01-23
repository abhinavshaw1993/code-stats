from tabulate import tabulate

def table(data, header, format='orgtbl'):
    """
    Return Printable table object with the heder and data.
    1. Hearder - List of headers
    2. Data - List of lists containing the data to be tabulated.
    """
    return  tabulate(data, header, tablefmt=format)
