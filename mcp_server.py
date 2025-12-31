from typing import Dict

class MCPToolServer:
    def list_tools(self):
        return {
            "estimate_budget": {
                "description": "Estimate bakery startup budget",
                "input_schema": {"city": "string", "size": "string"}
            }
        }

    def call_tool(self, name: str, args: Dict):
        if name == "estimate_budget":
            return {
                "estimated_cost": "25000 USD",
                "currency": "USD",
                "city": args["city"]
            }


server = MCPToolServer()
print(server.list_tools())
print(server.call_tool("estimate_budget", {"city": "Almaty", "size": "small"}))
