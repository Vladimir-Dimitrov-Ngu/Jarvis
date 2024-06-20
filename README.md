# Project Name: bot_jarviis

## Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Demo](#demo)
6. [Contributing](#contributing)
7. [License](#license)
8. [Database](#database)
9. [Future features](#future-features)



## Description:
bot_jarviis is a powerful and versatile chatbot designed to assist users with various tasks. It is built using advanced natural language processing techniques and can understand and respond to user queries in a human-like manner. Whether you need help with information retrieval, task automation, or just want to have a friendly conversation, bot_jarviis is here to assist you.

## Features:
- Natural Language Processing: bot_jarviis utilizes  NLP algorithms to understand and interpret user queries accurately.
- Voice answer: bot_jarviis can provide voice answers to user queries, allowing for a more interactive and engaging experience.
- Voice cloning: bot_jarviis can generate voice clones of different personalities, allowing for a more personalized and unique user experience.
- Information Retrieval: bot_jarviis can search the web and retrieve relevant information based on user queries, providing quick and accurate answers.
- Conversation Mode: Engage in a friendly conversation with bot_jarviis and enjoy its witty and intelligent responses.
- Customization: bot_jarviis can be easily customized and extended to suit your specific needs. Add new functionalities or integrate it with other systems seamlessly.
### ML-Design
![system_design](https://github.com/Vladimir-Dimitrov-Ngu/Jarvis/blob/master/desing.png)
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
1. Start the bot_jarviis application: `python3 bot.py`
2. Open your telegram app and connect to the bot_jarviis server.
3. Begin interacting with bot_jarviis by sending messages and queries.

## Demo
[Demo](https://drive.google.com/file/d/1XTz1yZ9g7OL94bCzwl1c4HdYY-wlUuzk/view?usp=sharing)


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

### Structure

#### `bot_user` Table
This table stores information about the users of the chatbot. It has the following columns:
- `telegram_id` (INTEGER): The unique identifier for each user.
- `created_at` (TIMESTAMP): The timestamp indicating when the user was created.
- `count_prompt` (INTEGER): The number of prompts sent by the user.

#### `gpt_answer` Table
This table stores the generated answers from the GPT model. It has the following columns:
- `id` (INTEGER): The unique identifier for each answer.
- `created_at` (TIMESTAMP): The timestamp indicating when the answer was generated.
- `context` (JSON): The context of the conversation in JSON format.
- `gpt_answer` (TEXT): The generated answer from the GPT model.
- `telegram_id` (FOREIGN KEY): The foreign key referencing the `telegram_id` column in the `bot_user` table.

#### `analytics` Table
This table stores analytics data related to the chatbot. It has the following columns:
- `id` (INTEGER): The unique identifier for each analytics entry.
- `count_answers` (INTEGER): The total count of answers generated.
- `tokens_output` (INTEGER): The number of tokens output by the GPT model.
- `cost` (FLOAT): The cost associated with generating the answers.

## Future features
1. Multi-language Support: bot_jarviis will be able to understand and respond to queries in multiple languages, making it more accessible to a global audience.
2. Integration with External APIs: bot_jarviis will have the ability to integrate with external APIs, enabling it to fetch data from various sources and provide more comprehensive answers.
3. User Profiles: bot_jarviis will support user profiles, allowing users to save their preferences and personalize their interactions with the chatbot.
4. Sentiment Analysis: bot_jarviis will have the capability to analyze the sentiment of user queries, allowing it to respond with empathy and understanding.
5. Task Automation: bot_jarviis will be able to perform automated tasks based on user requests, such as sending emails, scheduling appointments, or performing system operations.
6. Documentation: bot_jarviis will have comprehensive documentation, including usage examples, API references, and tutorials to help users get started and make the most out of the chatbot.
