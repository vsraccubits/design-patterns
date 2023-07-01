# Streaming Service Factory

This code demonstrates the use of the Factory Method design pattern to create instances of different streaming services.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the Python script.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the following command to execute the script:

   ```bash
   python before.py
   ```
   ```bash
   python after.py
   ```

## Code Explanation

+ The code consists of the following components:

+ StreamingService (abstract base class): Defines the common interface for all streaming services. It has an abstract play() method that needs to be implemented by the concrete streaming service classes.

+ Spotify, AppleMusic, GooglePlayMusic (concrete classes): Implement the play() method according to their respective streaming service.

+ StreamerFactory: The factory class responsible for creating instances of different streaming services. It has a get_streaming_service() method that takes a service name as an argument and returns an instance of the corresponding streaming service.

## Extending the Code

To add a new streaming service:

1. Create a new class that extends StreamingService.
2. Implement the play() method for the new streaming service.
3. Update the StreamerFactory class:
    + Add a new condition in the get_streaming_service() method to handle the new streaming service.
    + Return an instance of the new streaming service class in the new condition.