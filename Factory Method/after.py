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

class StreamerFactory():
    def get_streaming_service(self, service: str) -> StreamingService:
        """Get a Streaming Service."""
        if service == "spotify":
            return Spotify()
        elif service == "apple music":
            return AppleMusic()
        elif service == "google play music":
            return GooglePlayMusic()
        else:
            print("Selected Service Not Available")
            return

def main():
    service: str = input("Enter desired streaming service (spotify, apple music, google play music): ")

    if service not in ["spotify", "apple music", "google play music"]:
        print("Selected Service Not Available")
        return

    stream: StreamingService = StreamerFactory().get_streaming_service(service)
    print(stream)
    stream.play()

if __name__ == "__main__":
    main()