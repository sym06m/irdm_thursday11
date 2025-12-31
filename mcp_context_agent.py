class ContextAwareAgent:
    def __init__(self):
        self.context = []

    def add_context(self, text):
        self.context.append(text)

    def run(self):
        return " | ".join(self.context)


agent = ContextAwareAgent()
agent.add_context("Bakery business")
agent.add_context("Low budget")
agent.add_context("High demand")

print(agent.run())
