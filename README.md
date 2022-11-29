# Latency Measurement

This python repository contains the basic code to read audio from 2 wav files and calculate the latency between them using a full cross correlation (zero padding)

## Author: Federico G. Roux (rouxfederico@gmail.com)

## Installation

Must have docker and docker compose installed.

Build and get inside the container executing:

```bash
docker-compose up -d
docker exec -it  latency bash
```

## Usage

```bash

./main.py -s <path to signal file> -r <path to response file>

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
