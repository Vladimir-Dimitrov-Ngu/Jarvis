# Project Name: bot_jarviis

## Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [Database](#database)
4. [Installation](#installation)

## Description:
bot_jarviis is a powerful and versatile chatbot designed to assist users with various tasks. It is built using advanced natural language processing techniques and can understand and respond to user queries in a human-like manner. Whether you need help with information retrieval, task automation, or just want to have a friendly conversation, bot_jarviis is here to assist you.

## Features:
- Natural Language Processing: bot_jarviis utilizes state-of-the-art NLP algorithms to understand and interpret user queries accurately.
- Task Automation: With bot_jarviis, you can automate repetitive tasks, such as sending emails, scheduling appointments, or fetching data from external sources.
- Information Retrieval: bot_jarviis can search the web and retrieve relevant information based on user queries, providing quick and accurate answers.
- Conversation Mode: Engage in a friendly conversation with bot_jarviis and enjoy its witty and intelligent responses.
- Customization: bot_jarviis can be easily customized and extended to suit your specific needs. Add new functionalities or integrate it with other systems seamlessly.

## Installation:
1. Clone the repository: `git clone https://github.com/vladimirdimitrov/bot_jarviis.git`
2. Navigate to the project directory: `cd bot_jarviis`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Create sqlite database `cat database/init.sql | sqlite3 db.sqlite3`
5. Create config.py in root directory and add this variables:
    - secret_key: used for API Yandex
    - API_TOKEN: This is the bot token used for interacting with the Telegram Bot API.
    - system_prompt: variable is used in service/yandex_gpt.py, and it's a prompt used for the Yandex GPT API to generate responses.
    - catalog_id: variable is also used in service/yandex_gpt.py. It is an identifier for a specific catalog used with the Yandex GPT API.
    - SQLITE_DB_FILE: : this is the path to the SQLite database file used in your project. It's used in database/database_manager.py to establish a connection to the database.

## Usage:
1. Start the bot_jarviis application: `npm start`
2. Open your preferred chat client and connect to the bot_jarviis server.
3. Begin interacting with bot_jarviis by sending messages and queries.

## Contributing:
We welcome contributions from the community to enhance the functionality and performance of bot_jarviis. To contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add your feature description'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request.

## License:
This project is licensed under the MIT License. See the [LICENSE](https://github.com/vladimirdimitrov/bot_jarviis/blob/main/LICENSE) file for more details.

## Database:

This project uses SQLite as its primary data store. 

### Setup:

SQLite comes pre-installed with Python. The database file is typically stored in the project directory.

### Migrations:

If your project uses a migration tool (like Alembic or Django's built-in migrations), you can add instructions on how to run migrations here.

### Seeding:

If your project uses seed data, you can add instructions on how to seed the database here.

Remember to never include sensitive information such as database credentials in your README. These should be securely stored and accessed through environment variables.