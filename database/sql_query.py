INSERT_GPT_ANSWER_JSON = """
INSERT OR REPLACE INTO gpt_answer(id, created_at, context, gpt_answer)
VALUES ({id}, CURRENT_TIMESTAMP, '{context}', '{gpt_answer}');
"""

INSERT_TOTAL_TOKENS = """
INSERT OR REPLACE INTO analytics(id, count_answers, tokens_output, cost, toxic_rating)
VALUES ({telegram_id}, '{count}', '{tokens}', '{cost}', '{toxic_rating}');
"""

UPDATE_TOXIC_RATING = """
UPDATE analytics
SET toxic_rating = toxic_rating + 1
WHERE id = {telegram_id};
"""

SELECT_CONTEXT = """
SELECT context FROM gpt_answer
WHERE id={telegram_id};
"""

SELECT_COUNT_ANSWERS = """
SELECT tokens_output, count_answers, cost, toxic_rating FROM analytics
WHERE id={telegram_id};
"""

DELETE_CONTEXT = """
DELETE FROM gpt_answer WHERE id = {id};
"""
