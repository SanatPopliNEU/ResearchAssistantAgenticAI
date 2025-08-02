# 📘 Agentic System - Technical Documentation
## 1. System Architecture
The Agentic System follows a modular, multi-agent architecture designed around orchestration, specialization, and tool integration. The architecture comprises:

A Controller Agent that acts as the central orchestrator

Multiple Specialized Agents with focused responsibilities

Integration with both built-in and custom tools

A dedicated Memory Management Layer

An Orchestration Workflow Engine for sequencing agent actions


## 2. Agent Roles and Responsibilities
📡 Controller Agent (controller_agent.py)
Responsibilities:

Coordinates all workflow stages

Delegates tasks to specialized agents

Handles failure cases with fallback strategies

Manages inter-agent communication

Features:

Decision logic based on input context

## Logging and verbose control for debugging

### 🧠 Research Agent (research_agent.py)
Responsibilities:

Performs web search and gathers topic-specific information

Interfaces with web_search_tool.py

### Prompt Strategy:

Uses domain-adapted prompts to extract relevant context

### ✍️ Summarization Agent (summarization_agent.py)
Responsibilities:

Generates concise summaries from retrieved content

Works with data_processing_tool.py and OpenAI API

## Prompt Strategy:

Instruction-tuned for clarity and brevity

## 3. Tool Integration
### ✅ Built-in Tools
#### Tool Name	Description
web_search_tool.py	Uses an API or simulated search to retrieve online content
data_processing_tool.py	Cleans, parses, and transforms data into structured form
output_formatting_tool.py	Converts raw output into readable formats like Markdown or JSON

### 🧩 Custom Tool
Tool: custom_domain_extractor.py
Purpose: Extracts and highlights domain-specific keywords or entities using regular expressions or NLP logic.

### Inputs:

Raw text or search results

### Outputs:

JSON with extracted terms and confidence (if scored)

Error Handling:

Handles null/empty text, malformed input, and noisy data gracefully

## 4. Orchestration Workflow
Implemented in workflow.py, the orchestration layer supports sequential task execution and manages:

Input validation and pre-processing

Calling agents with contextual memory

Storing intermediary outputs

Triggering fallback steps if agents fail

## 5. Memory System
The memory_manager.py module implements:

Ephemeral memory for short-term context sharing across a session

Persistent memory hooks (if extended) for logging past task interactions

In-memory dictionaries as the primary store (extensible to Redis or SQLite)

## 6. Implementation Notes
The system entry point is main.py, which takes a task query as input and runs the full agentic workflow.

Dependencies are defined in requirements.txt, supporting Python 3.11.x.

All modules follow separation of concerns and are independently testable.

## 7. Testing Strategy
Unit tests are provided in the tests/ folder:

test_controller_agent.py: Workflow and delegation logic

test_specialized_agents.py: Output correctness for agents

test_tools.py: Edge cases and transformation accuracy

test_workflow.py: End-to-end integration tests

## 8. Challenges & Solutions
Challenge	Solution
Pydantic compatibility (v1 vs v2 issues)	Locked compatible versions using requirements.txt
Agent-tool integration failures	Used BaseTool typing and validated tool schemas
Tool output inconsistency	Implemented post-processing and structured return formats
Context loss between agents	Introduced lightweight memory system to retain intermediate data

## 9. Performance Analysis
Metric	Description
Execution Time	Avg. 4.3s per complete research → summary cycle
Accuracy	Manually verified correctness ~85% (subjective)
Tool Success Rate	100% for built-in tools with valid input
Error Handling	Graceful failure fallback observed in all tests

## 10. Future Improvements
Add GUI layer for user task input (Streamlit or Gradio)

Extend memory to support long-term project history

Integrate document ingestion pipeline (e.g., PDFs, web pages)

Enhance domain extractor with NLP models (spaCy, Transformers)

## 11. Conclusion
The Agentic System demonstrates a robust implementation of multi-agent orchestration using Python, integrating built-in and custom tools. It shows strong potential for scalability, adaptability across domains, and practical use in content summarization and web intelligence gathering.

# Attributes/Contribution
1. OpenAI API key-https://openai.com/api/
2. serpapi-https://serpapi.com/search
3. Co-Pilot Pro:https://copilot.microsoft.com/chats/9r7uCCTtkbXLParTLhQYE
4. AI tools: Claude, Chatgpt, copilot
5. Chatgpt Chatlink: https://chatgpt.com/c/688b71d8-2888-8331-b989-d209512b8255

## Project Structure
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
    └── technical_report.pdf 

# License

MIT License

Copyright (c) 2025 Sanat Popli

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
