FROM python:3.10-slim
WORKDIR /app
COPY server.py .
COPY requirements.txt .
RUN pip install uv
RUN uv pip install --system -r requirements.txt
CMD ["uv", "run", "--with", "mcp[cli],requests", "mcp", "run", "server.py"]


# {
#   "mcpServers": {
#     "IBM Webmethods MCP server": {
#       "url": "http://localhost:8000/mcp",
#       "env": {
#         "WEBMETHODS_API_KEY": "<your-api-key>"
#       }
#     }
#   }
# }