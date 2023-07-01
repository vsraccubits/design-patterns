from abc import ABC, abstractmethod

class StreamingService(ABC):
    """A Streaming Service."""
    @abstractmethod
    def play(self):
        """Play an Audio."""

class Spotify(StreamingService):
    def play(self):
        print("Play a song from Spotify.")

class AppleMusic(StreamingService):
    def play(self):
        print("Play a song from Apple Music.")

class GooglePlayMusic(StreamingService):
    def play(self):
        print("Play a song from Google Play Music.")

def main():
    service: str = input("Enter desired streaming service (spotify, apple music, google play music): ")

    if service not in ["spotify", "apple music", "google play music"]:
        print("Selected Service Not Available")
        return

    stream: StreamingService
    if service == "spotify":
        stream = Spotify()
    elif service == "apple music":
        stream = AppleMusic()
    elif service == "google play music":
        stream = GooglePlayMusic()
    
    stream.play()

if __name__ == "__main__":
    main()