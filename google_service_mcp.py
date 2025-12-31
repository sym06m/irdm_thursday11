class GoogleSearchMCPTool:
    def search(self, query: str):
        return {
            "query": query,
            "top_result": "Market demand for bakeries is increasing"
        }


search_tool = GoogleSearchMCPTool()
print(search_tool.search("bakery market trends"))
