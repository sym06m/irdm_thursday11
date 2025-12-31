class MCPClientAgent:
    def __init__(self, tool_server):
        self.tool_server = tool_server

    def run(self, city):
        tools = self.tool_server.list_tools()
        result = self.tool_server.call_tool(
            "estimate_budget",
            {"city": city, "size": "small"}
        )
        return result


agent = MCPClientAgent(server)
print(agent.run("Almaty"))
