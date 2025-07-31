def clean_data(raw_data):
    # Implement data cleaning logic here
    cleaned_data = raw_data.strip()  # Example: stripping whitespace
    return cleaned_data

def transform_data(cleaned_data):
    # Implement data transformation logic here
    transformed_data = cleaned_data.lower()  # Example: converting to lowercase
    return transformed_data

def process_data(raw_data):
    cleaned = clean_data(raw_data)
    transformed = transform_data(cleaned)
    return transformed

def validate_data(data):
    # Implement data validation logic here
    if not isinstance(data, str) or not data:
        raise ValueError("Invalid data: must be a non-empty string.")
    return True

def data_summary(data):
    # Implement logic to summarize data
    return {
        "length": len(data),
        "first_100_chars": data[:100],
    }