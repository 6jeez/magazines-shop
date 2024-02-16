class Journal:
    def __init__(self, db_manager) -> None:
        """
        initializes a Journal object

        args:
            db_manager (DBManager): The database manager object
        """
        self.db_manager = db_manager

    async def create_journal(self, title, content, price) -> None:
        """
        creates a new journal entry and adds it to the database

        args:
            title (str): The title of the journal
            content (str): The content of the journal

        returns:
            None
        """
        await self.db_manager.add_journal(title, content, price)
        print("the journal has been successfully added")

    async def display_all_journals(self) -> None:
        """
        displays all the journals in the database

        returns:
            None
        """
        journals = await self.db_manager.get_all_journals()
        if journals:
            print("List of all journals:")
            for journal in journals:
                print(f"ID: {journal[0]}\nTitle: {journal[1]}\nPrice: {journal[2]}")
        else:
            print("no magazines")

    async def search_journals(self, keyword) -> None:
        """
        searches for journals in the database based on a keyword

        args:
            keyword (str): The keyword to search for

        returns:
            None
        """
        journals = await self.db_manager.search_journals(keyword)
        if journals:
            print(f"Found magazines with the keyword '{keyword}':")
            for journal in journals:
                print(f"ID: {journal[0]}\nTitle: {journal[1]}\nPrice: {journal[2]}")
        else:
            print("no journals with the specified keyword were found")

    async def delete_journal(self, journal_id) -> None:
        """
        deletes a journal entry from the database

        args:
            journal_id (int): The ID of the journal to delete

        returns:
            None
        """
        await self.db_manager.delete_journal(journal_id)
        print("the magazine has been successfully deleted")
