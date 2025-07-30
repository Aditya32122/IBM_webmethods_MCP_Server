# IBM WebMethods MCP Server 🚀

A Model Context Protocol (MCP) server that integrates IBM WebMethods API Gateway with AI applications using STDIO transport. This server enables seamless interaction with WebMethods API Gateway through AI-powered tools and automation.

## ✨ Features

- **Complete API Management**: Create, read, update, and delete APIs
- **Application Management**: Manage applications and their API associations  
- **Transaction Analytics**: Retrieve and analyze API transaction data
- **Real-time Monitoring**: Monitor API performance and usage
- **MCP Integration**: Native support for AI assistants and automation tools

## 🛠️ Prerequisites

### Required Software

| Component | Version | Installation |
|-----------|---------|--------------|
| **Python** | 3.10+ | [Download from python.org](https://python.org) |
| **uv** | Latest | `pip install uv` |
| **MCP Client** | Latest | VS Code with MCP extension or Claude Desktop |

### Required Credentials

- IBM WebMethods API Gateway URL
- Valid username and password
- Network access to your API Gateway instance

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Aditya32122/IBM_webmethods_MCP_Server.git
cd IBM_webmethods_MCP_Server
```

### 2. Install Dependencies

```bash
uv pip install -r requirements.txt
```

**Windows Users**: If the command isn't recognized, use the full path:
```bash
C:\Users\<your-username>\.local\bin\uv.exe pip install -r requirements.txt
```

### 3. Configure MCP Client

Create or edit your MCP configuration file:

**File Location:**
- Windows: `~/.mcp.json` or `.vscode/mcp.json`
- macOS/Linux: `~/.mcp.json` or `.vscode/mcp.json`

**Configuration Example:**

```json
{
  "mcpServers": {
    "IBM WebMethods MCP server": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli],requests",
        "mcp",
        "run",
        "/path/to/your/server.py"
      ],
      "type": "stdio"
    }
  }
}
```

**Platform-Specific Paths:**

<details>
<summary>Windows Configuration</summary>

```json
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
        "D:\\path\\to\\server.py"
      ],
      "type": "stdio"
    }
  }
}
```

</details>

<details>
<summary>macOS/Linux Configuration</summary>

```json
{
  "mcpServers": {
    "IBM WebMethods MCP server": {
      "command": "/usr/local/bin/uv",
      "args": [
        "run",
        "--with",
        "mcp[cli],requests",
        "mcp",
        "run",
        "/home/user/path/to/server.py"
      ],
      "type": "stdio"
    }
  }
}
```

</details>

## 🎯 Usage

### Initial Setup

1. **Launch your MCP client** (VS Code or Claude Desktop)
2. **Set credentials** using the `set_credentials` tool:
   ```
   set_credentials(
       base_url="https://your-gateway.webmethods.io/rest/apigateway",
       username="your-username", 
       password="your-password"
   )
   ```

### Available Tools

| Tool Category | Functions |
|---------------|-----------|
| **🔐 Authentication** | `set_credentials` |
| **📊 APIs** | `get_all_apis`, `get_api_details`, `delete_api`, `activate_api`, `deactivate_api` |
| **📱 Applications** | `get_all_applications`, `create_application`, `delete_application`, `associate_apis_with_application` |
| **📈 Analytics** | `get_api_transactions` |

### Example Commands

<details>
<summary>View API Transactions</summary>

```python
get_api_transactions(
    duration="3d",
    start_date="2024-01-01 00:00:00",
    end_date="2024-01-03 23:59:59",
    event_type="ALL"
)
```

</details>

<details>
<summary>Create New Application</summary>

```python
create_application(
    name="My App",
    description="Application for testing",
    version="1.0",
    identifiers=[{"name": "app-id", "key": "api-key", "value": ["test-key"]}],
    contact_emails=["admin@company.com"]
)
```

</details>

## 📁 Project Structure

```
IBM_webmethods_MCP_Server/
├── 📄 server.py           # Main MCP server implementation
├── 📄 requirements.txt    # Python dependencies
├── 📄 README.md          # This file
└── 📄 .gitignore         # Git ignore rules
```

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **Command not found: uv** | Install uv: `pip install uv` |
| **Permission denied** | Use full path to uv executable |
| **Connection refused** | Verify API Gateway URL and network access |
| **Authentication failed** | Check username/password and permissions |

### Debug Mode

Enable detailed logging by setting environment variable:

```bash
# Windows
set MCP_DEBUG=1

# macOS/Linux  
export MCP_DEBUG=1
```

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature-name`
3. **Commit** your changes: `git commit -am 'Add feature'`
4. **Push** to the branch: `git push origin feature-name`
5. **Submit** a pull request



---

