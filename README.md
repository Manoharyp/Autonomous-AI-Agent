Autonomous AI Agent
🚀 An Autonomous AI Agent that executes tasks based on instructions without human intervention.

Features
Finds the latest AI headlines and saves them to a file.

Autonomous decision-making with modular agents (Browser, File, Terminal).

Simple and efficient architecture.

How It Works
Input Instruction:
The agent takes an instruction (e.g., "Find top 5 AI headlines and save to file").

Autonomous Execution:
Based on the instruction, the agent selects the right module (browser, file, terminal) to complete the task.

Output Result:
Results are saved into output/result.txt automatically.

Project Structure
bash
Copy
Edit
autonomous_agent/
├── browser_agent.py    # Handles web browsing tasks
├── file_agent.py       # Handles file operations
├── terminal_agent.py   # Handles terminal commands
├── main.py             # Main program to run the agent
├── requirements.txt    # Python dependencies
└── output/             # Directory where results are saved
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Manoharyp/Autonomous-AI-Agent.git
cd Autonomous-AI-Agent
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
bash
Copy
Edit
python main.py
Follow the on-screen instructions!

Example Output
"Find top 5 AI headlines and save to file."
✅ Task completed successfully! Results saved in output/result.txt.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
This project is open-source and free to use under the MIT License.

