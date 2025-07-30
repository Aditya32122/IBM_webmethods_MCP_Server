IBM WebMethods MCP Server (Local Setup)
This MCP server integrates IBM WebMethods API Gateway with AI applications using the Model Context Protocol (MCP) over STDIO transport. This guide explains how to set up and run the server locally on Windows, Linux, or macOS without Docker, using the uv tool to execute webmethods.py.

🛠 Prerequisites
Python 3.10 or higher
Install from python.org

uv (A fast Python package and script runner)
Install via pip:

bash
Copy
Edit
pip install uv
MCP-compatible client
Such as Visual Studio Code with the MCP extension or Claude Desktop.

IBM WebMethods API Gateway credentials
Obtain your API Gateway URL, username, and password. These can be set using the set_credentials tool during runtime.

🚀 Setup Instructions
1. Clone or Download the Repository
bash
Copy
Edit
git clone https://github.com/Aditya32122/IBM_webmethods_MCP_Server.git
cd IBM_webmethods_MCP_Server
2. Install Dependencies
Use uv to install required Python packages:

bash
Copy
Edit
uv pip install -r requirements.txt
On Windows, if the command is not recognized, try using the full path to uv, e.g.:

bash
Copy
Edit
C:\Users\<your-username>\.local\bin\uv.exe pip install -r requirements.txt
3. Configure the MCP Client
📝 Create or Edit the MCP Config File
On Windows:
Create or edit the file at ~/.mcp.json or .vscode/mcp.json inside your project.

Example config:

json
Copy
Edit
{
  "mcpServers": {
    "IBM WebMethods MCP server": {
      "command": "C:\\Users\\<your-username>\\.local\\bin\\uv.exe",
      "args": [
        "run",
        "--with",
        "mcp[cli],requests",
        "mcp",
        "run",
        "D:\\mcpdemo\\server.py"
      ],
      "type": "stdio"
    }
  }
}
Replace paths according to your OS and file locations.

✅ Example Usage
Once configured, launch your MCP-compatible client (e.g., VS Code), and it should automatically detect and communicate with the server via STDIO.

📁 File Structure
Copy
Edit
IBM_webmethods_MCP_Server/
├── webmethods.py
├── requirements.txt
└── README.md