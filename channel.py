class Channel: # Define the Channel class
    def __init__(self, name, is_voice=False): # Initialize the Channel with a name and whether it is a voice channel
        self.name = name # The name of the channel
        self.is_voice = is_voice # Whether the channel is a voice channel
        self.messages = [] # A list of messages in the channel