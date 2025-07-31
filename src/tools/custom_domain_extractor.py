import re

class CustomDomainExtractor:
    def __init__(self):
        pass

    def extract_information(self, input_data):
        """
        Extracts domain-specific information (emails and URLs) from the provided input data.
        
        Parameters:
        input_data (str): The data from which to extract information.

        Returns:
        dict: A dictionary containing the extracted information.
        """
        # Input validation
        if not self.validate_input(input_data):
            self.handle_error(ValueError("Input data must be a non-empty string."))
            return {}

        extracted_data = {}

        # Extract emails
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", input_data)
        extracted_data["emails"] = emails

        # Extract URLs
        urls = re.findall(r"https?://[^\s]+", input_data)
        extracted_data["urls"] = urls

        return extracted_data

    def validate_input(self, input_data):
        """
        Validates the input data for extraction.

        Parameters:
        input_data (str): The data to validate.

        Returns:
        bool: True if valid, False otherwise.
        """
        return isinstance(input_data, str) and len(input_data) > 0

    def handle_error(self, error):
        """
        Handles errors that occur during the extraction process.

        Parameters:
        error (Exception): The error to handle.
        """
        print(f"An error occurred: {error}")