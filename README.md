# mediabot

A simple chatbot test for federated social media it sends a note when running `startup.sh --note "This is a test"`.

## Features

- Posts a note to a Misskey instance
- Configurable via `config.txt`

## Installation

1. Clone this repository

2. Configure your Misskey instance and API token in `config.txt`:

    ```plaintext
    MISSKEY_INSTANCE_URL=https://your-misskey-instance
    MISSKEY_API_TOKEN=your_api_token
    ```

3. Make `startup.sh` executable:

    ```bash
    chmod +x startup.sh
    ```


## Usage

Post a note by running:

    ```bash
    ./startup.sh --note "This is a test"
    ```
