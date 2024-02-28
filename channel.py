class Channel:
    def __init__(self, name, is_voice=False):
        self.name = name
        self.is_voice = is_voice
        self.messages = []