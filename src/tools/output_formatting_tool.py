def format_output(data, format_type='text'):
    """
    Formats the output data based on the specified format type.

    Parameters:
    - data: The data to be formatted.
    - format_type: The type of format to apply ('text', 'json', 'xml').

    Returns:
    - str: Formatted output as a string.
    """
    if format_type == 'text':
        return str(data)
    elif format_type == 'json':
        import json
        return json.dumps(data, indent=4)
    elif format_type == 'xml':
        import dicttoxml
        return dicttoxml.dicttoxml(data).decode()
    else:
        raise ValueError("Unsupported format type. Use 'text', 'json', or 'xml'.")

def print_formatted_output(data, format_type='text'):
    """
    Prints the formatted output to the console.

    Parameters:
    - data: The data to be formatted and printed.
    - format_type: The type of format to apply ('text', 'json', 'xml').
    """
    formatted_data = format_output(data, format_type)
    print(formatted_data)