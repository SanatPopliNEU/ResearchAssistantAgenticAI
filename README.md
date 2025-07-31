# Agentic System

## Overview
The Agentic System is a multi-agent orchestration framework designed to facilitate task delegation and enhance productivity through specialized agents. This system integrates various tools to perform tasks such as web searching, data processing, and content summarization, while also allowing for the development of custom tools tailored to specific needs.

## Project Structure
```
agentic-system
├── src
│   ├── controller_agent.py          # Implements the ControllerAgent class for workflow orchestration
│   ├── specialized_agents            # Contains specialized agents for specific tasks
│   │   ├── research_agent.py         # Gathers and analyzes information
│   │   └── summarization_agent.py    # Summarizes content
│   ├── tools                         # Various tools for data handling and processing
│   │   ├── web_search_tool.py        # Retrieves information from the internet
│   │   ├── data_processing_tool.py    # Transforms and cleans data
│   │   ├── output_formatting_tool.py  # Formats output data for presentation
│   │   └── custom_domain_extractor.py # Extracts domain-specific information
│   ├── orchestration                 # Coordinates agent interactions
│   │   └── workflow.py               # Defines the workflow for task execution
│   ├── memory                        # Manages contextual awareness
│   │   └── memory_manager.py         # Implements memory management functions
│   └── main.py                       # Entry point for the application
├── tests                             # Contains unit tests for the system
│   ├── test_controller_agent.py      # Tests for the controller agent
│   ├── test_specialized_agents.py    # Tests for specialized agents
│   ├── test_tools.py                 # Tests for the various tools
│   └── test_workflow.py              # Tests for the workflow implementation
├── requirements.txt                  # Lists project dependencies
├── README.md                         # Documentation for the project
└── docs                              # Additional documentation
    ├── architecture_diagram.png      # System architecture diagram
    └── technical_report.pdf           # Comprehensive system report
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd agentic-system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Features
- **Controller Agent**: Orchestrates the workflow by delegating tasks to specialized agents and managing communication between them.
- **Specialized Agents**: 
  - **Research Agent**: Gathers and analyzes information based on defined objectives.
  - **Summarization Agent**: Processes input data to generate concise summaries.
- **Integrated Tools**: 
  - **Web Search Tool**: Retrieves information from the internet.
  - **Data Processing Tool**: Transforms and cleans data for analysis.
  - **Output Formatting Tool**: Structures and presents information in a user-friendly manner.
- **Custom Tool**: Allows for the extraction of domain-specific information with input validation and error handling.

## Documentation
For detailed documentation, including system architecture and technical reports, please refer to the `docs` directory. 

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes. 

## License
This project is licensed under the MIT License. See the LICENSE file for more details.