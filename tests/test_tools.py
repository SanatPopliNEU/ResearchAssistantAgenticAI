import unittest
from src.tools.web_search_tool import perform_search
from src.tools.data_processing_tool import clean_data
from src.tools.output_formatting_tool import format_output
from src.tools.custom_domain_extractor import extract_domain_info

class TestTools(unittest.TestCase):

    def test_perform_search(self):
        query = "OpenAI"
        results = perform_search(query)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)

    def test_clean_data(self):
        raw_data = ["  Data1  ", "Data2", "  Data3  "]
        cleaned_data = clean_data(raw_data)
        self.assertEqual(cleaned_data, ["Data1", "Data2", "Data3"])

    def test_format_output(self):
        data = {"title": "Test Title", "content": "Test Content"}
        formatted = format_output(data)
        self.assertIn("Test Title", formatted)
        self.assertIn("Test Content", formatted)

    def test_extract_domain_info(self):
        input_data = "Sample text with domain-specific information."
        extracted_info = extract_domain_info(input_data)
        self.assertIsInstance(extracted_info, dict)
        self.assertIn("domain_key", extracted_info)

if __name__ == '__main__':
    unittest.main()