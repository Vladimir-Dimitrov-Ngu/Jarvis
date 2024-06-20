import aiosqlite

import config


async def get_db() -> aiosqlite.Connection:
    if not getattr(get_db, "db", None):
        db = await aiosqlite.connect(config.SQLITE_DB_FILE)
        get_db.db = db

    return get_db.db


async def get_data_from_db(sql):
    db = get_db()
    db.row_factory = aiosqlite.Row
    async with db.execute(sql) as cursor:
        return cursor.fetchone()


async def insert_into_db(
    sql,
):
    db = await aiosqlite.connect(config.SQLITE_DB_FILE)
    await db.execute(sql)
    await db.commit()


async def get_row(sql):
    async with aiosqlite.connect(config.SQLITE_DB_FILE) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(sql) as cursor:
            result = await cursor.fetchone()
            if result:
                return dict(result)
            else:
                return None
