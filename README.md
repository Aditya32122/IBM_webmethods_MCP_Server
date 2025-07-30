IBM WebMethods MCP Server (Local Setup)
This MCP server integrates IBM WebMethods API Gateway with AI applications using the Model Context Protocol (MCP) over STDIO transport. This guide explains how to set up and run the server locally on Windows, Linux, or macOS without Docker, using the uv tool to execute webmethods.py.
Prerequisites
• Python 3.10 or higher: Install from python.org.
• uv: A fast Python package and script runner.
  Install via pip:  pip install uv
• MCP-compatible client: Such as Visual Studio Code with the MCP extension or Claude Desktop.
• IBM WebMethods API Gateway credentials: Obtain a base URL (e.g., https://<your-api-gateway-url>), username, and password from your IBM WebMethods account. These can be set using the set_credentials tool during runtime.
Setup Instructions
1. Clone or Download the Repository
Download or clone the repository containing webmethods.py to a local directory, e.g., ~/mcpdemo (Linux/macOS) or D:\mcpdemo (Windows).
git clone https://github.com/Aditya32122/IBM_webmethods_MCP_Server.git
cd webmethods-mcp-server
2. Install Dependencies
The server requires specific Python packages listed in requirements.txt.
Install dependencies using uv:
uv pip install -r requirements.txt
On Windows, use the full path to uv if needed, e.g., C:\\Users\\<your-username>\\.local\\bin\\uv.exe.
3. Configure the MCP Client
Configure your MCP client (e.g., VS Code) to communicate with the server using STDIO transport.
Create or edit the MCP configuration file:
• On Windows: ~/.mcp.json or .vscode/mcp.json in your project directory.
Add the following configuration, adjusting the command and args paths for your system:
{
  "mcpServers": {
    "IBM Webmethods MCP server": {
      "command": "uv",  // or C:\Users\<your-username>\.local\bin\uv.exe
      "args": [
        "run",
        "--with",
        "mcp[cli],requests",
        "mcp",
        "run",
        "<path-to-server-py>"
      ],
      "type": "stdio"
    }
  }
}
Example:
"IBM Webmethods MCP server": {
  "command": "C:\\Users\\adity\\.local\\bin\\uv.EXE",
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

