import aiosqlite
from typing import Any


class DatabaseManager:
    """
    class that manages the database operations for journals
    """

    def __init__(self, db_name) -> None:
        """
        initializes a new instance of the DatabaseManager class

        args:
            db_name (str): The name of the database file
        """
        self.db_name = db_name

    async def connect(self) -> None:
        """
        connects to the database.
        """
        self.connection = await aiosqlite.connect(self.db_name)

    async def close(self) -> None:
        """
        closes the database connection.
        """
        await self.connection.close()

    async def create_table(self) -> None:
        """
        ceates the 'journals' table if it doesn't exist
        """
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS journals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    content TEXT,
                    price INTEGER
                )
                '''
            )
            await self.connection.commit()

    async def add_journal(self, title, content, price) -> None:
        """
        adds a new journal to the 'journals' table

        args:
            title (str): The title of the journal
            content (str): The content of the journal
        """
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                '''
                INSERT INTO journals (title, content, price) VALUES (?, ?, ?)
                ''',
                (title, content, price)
            )
            await self.connection.commit()

    async def get_all_journals(self) -> Any:
        """
        retrieves all journals from the 'journals' table

        returns:
            list: A list of tuples containing the id and title of each journal
        """
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                '''
                SELECT id, title, price FROM journals
                '''
            )
            return await cursor.fetchall()

    async def search_journals(self, keyword) -> Any:
        """
        searches for journals in the 'journals' table based on a keyword

        args:
            keyword (str): The keyword to search for in the journal content

        returns:
            list: A list of tuples containing the id and title of each matching journal
        """
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                '''
                SELECT id, title, price FROM journals WHERE content LIKE ?
                ''',
                ('%' + keyword + '%',)
            )
            return await cursor.fetchall()

    async def delete_journal(self, journal_id) -> None:
        """
        deletes a journal from the 'journals' table

        args:
            journal_id (int): The ID of the journal to delete
        """
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                '''
                DELETE FROM journals WHERE id=?
                ''',
                (journal_id,)
            )
            await self.connection.commit()
