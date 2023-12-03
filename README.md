# telegram-bot-message-processor

## Table of Contents
 1. [Introduction](#introduction)
 2. [Requirements](#requirements)
 3. [Installation](#installation)
 4. [Used technologies](#used-technologies)
 5. [Usage](#usage)
 7. [License](#license) 


## Introduction
This project leverages a Telegram bot, utilizing RabbitMQ to establish a command queue for handling incoming messages.
The bot captures incoming messages and processes them through a structured queue.
The system supports commands that enable the display of messages in the console or the option to send a post request. 

## Requirements
* python 3.8
* pip
* Docker

## Installation
1. Clone this repository:

    ```
    git clone https://github.com/Altahoma/telegram-bot-message-processor.git
    ```
 2. Create .env file and define environmental variables following .env.example or use default:
    ```
    TELEGRAM_TOKEN=telegram token
    EXTERNAL_API_URL=api url endpoint
    AMQP_USER=user
    AMQP_PASSWORD=pass
    AMQP_ADDRESS=rabbitmq
    AMQP_VHOST=/
    AMQP_PORT=5672
    ```
### 3. To run it from docker
1. Run command:
      ```
      docker-compose up --build
      ```

## Used technologies
    - Telegram API
    - RabbitMQ
    - Docker

## Usage
    1. On mac run: chmod +x wait-for-it.sh
    2. Launch project in docker.
    3. Use producer.py to test commands.


# License
This project is licensed under the MIT License.
Feel free to use and modify the codebase as needed.
