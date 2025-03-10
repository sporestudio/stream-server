<div align="center">
    <h1>Stream Server</h1>
</div>

<div align="center">
    <img src="./docs/.assets/stream-diag.png" alt="Stream server diagram" width="100%">
</div>

Deployment of a system to automate the download and preparation of multimedia content from YouTube through a Telegram bot using Docker containers and Nginx.


## Features

- **Real-time HLS Transcoding** - Automatically converts videos to HLS format for efficient streaming.  
- **Supports Multiple Input Formats** - Compatible with MP4, MKV, AVI, and more.  
- **Low-Latency Streaming** - Optimized settings for fast loading times.  
- **HLS Player Compatibility** - Works with VLC, HTML5 players, and mobile apps.  
- **HTTPS Support** - SSL certificates for secure streaming.      


## Requirements

- **Unix-based system**.
- **Docker** (20.10 or later recommended).
- **Docker Compose** (v1.29 or later recommended).
- **Python 3**.

## Documentation

To see documentation of the project you can [click here](https://github.com/sporestudio/stream-server/blob/main/docs/README.md) or see the docs/ directory.

## Previous configuration

We have to do some previous configurations to make the project work. First we have to create a .env file with some necessary variables:

```bash
## Telegram bot API Token
TELEGRAM_TOKEN=

# IONOS API Token
IONOS_TOKEN=

## Apache global vars
DOMAIN_NAME=
SERVER_ADMIN=
```

## Installation

### Clone the repository

Clone the repository from GitHub:

```bash
$ git clone https://github.com/sporestudio/stream-server
$ cd stream-server
```

### Deploy the project

#### Using makefile

- **Generating the certs**: We have the option to deploy the projects and generate the SSL certificates in an automated way with certbot.

    ```bash
    $ make all
    ```

- **Without generate the certs**: We can deploy the project without generate the SSL certificates.

    ```bash
    $ make deploy
    ```

#### Using docker compose

- We can deploy the project using Docker Compose launching the following command:

```bash
$ docker-compose up --build -d
```

## License

This project is licensed under the GNU General Public License - see the [LICENSE](https://github.com/sporestudio/stream-server/blob/main/LICENSE) file for details.

## Contributing

Want to contribute? There are multiple ways you can contribute to this project. Here are some ideas:

* [Translate the web into multiple languages!](/docs/CONTRIBUTING.md#translations)
* [Reporting Bugs](/docs/CONTRIBUTING.md#reporting-bugs) 
* [Check out some issues](https://github.com/sporestudio/stream-server/issues) (or translate them).

## Author

This repository was created by [sporestudio](https://github.com/sporestudio).