import unittest
from discussion import start_discussion

class TestStartDiscussion(unittest.TestCase):
    def setUp(self):
        self.topic = "Tech Startup"
        self.agents = [
            {
                "title": "CEO",
                "description": "You are the CEO of the company.",
                "instruction": "Discuss the business strategy."
            },
            {
                "title": "CTO",
                "description": "You are the CTO of the company.",
                "instruction": "Discuss the technology stack."
            }
        ]

    def test_start_discussion(self):
        response = start_discussion(self.topic, self.agents)
        print(response)
        #self.assertIsNotNone(response)
        #self.assertIn("Founder", response)

if __name__ == '__main__':
    unittest.main()
