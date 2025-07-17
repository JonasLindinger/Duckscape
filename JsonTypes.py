class StoryNode:
    def __init__(self, data):
        self.dialog = data.get("dialog", "")
        self.choices = data.get("choices", [])
        self.type = data.get("type", "normal")
        self.outcome = data.get("outcome", None)