CREATE TABLE bot_user (
    telegram_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    count_prompt INTEGER
);

CREATE TABLE gpt_answer (
    id INTEGER PRIMARY KEY NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    context JSON,
    gpt_answer TEXT,
    FOREIGN KEY(id) REFERENCES bot_user(telegram_id)
);



CREATE TABLE analytics  (
    id INTEGER PRIMARY KEY NOT NULL,
    count_answers INTEGER,
    tokens_output INTEGER,
    cost FLOAT
);