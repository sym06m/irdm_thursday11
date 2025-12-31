class LocationTool:
    def analyze(self, city):
        return "High foot traffic area"


class PricingTool:
    def suggest(self):
        return "Mid-range pricing"


location_tool = LocationTool()
pricing_tool = PricingTool()

print(location_tool.analyze("Almaty"))
print(pricing_tool.suggest())
