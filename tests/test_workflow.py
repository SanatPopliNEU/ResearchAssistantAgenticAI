import unittest
from src.orchestration.workflow import execute_workflow

class TestWorkflow(unittest.TestCase):

    def test_workflow_execution(self):
        result = execute_workflow()
        self.assertIsNotNone(result)
        self.assertTrue(result['success'])
        self.assertIn('data', result)
        self.assertGreater(len(result['data']), 0)

    def test_workflow_error_handling(self):
        with self.assertRaises(Exception):
            execute_workflow(invalid_param=True)

    def test_agent_interaction(self):
        result = execute_workflow()
        self.assertIn('agent_responses', result)
        self.assertEqual(len(result['agent_responses']), 2)  # Assuming two specialized agents

if __name__ == '__main__':
    unittest.main()