from journal import Journal


class Menu:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.journal = Journal(db_manager)

    async def main_menu(self) -> None:
        while True:
            print("\nMain menu:")
            print("1. add a new magazine")
            print("2. view a list of all journals")
            print("3. search for magazines")
            print("4. delete magazine")
            print("5. exit")
            choice = input("Select an action: ")

            if choice == '1':
                await self.add_journal_menu()
            elif choice == '2':
                await self.display_all_journals_menu()
            elif choice == '3':
                await self.search_journals_menu()
            elif choice == '4':
                await self.delete_journal_menu()
            elif choice == '5':
                print("exit from program")
                break
            else:
                print("wrong choice")

    async def add_journal_menu(self) -> None:
        title = input("enter the title of the magazine: ")
        content = input("enter the content of the magazine: ")
        price = float(input("enter the price of the magazine: "))
        await self.journal.create_journal(title, content, price)

    async def display_all_journals_menu(self) -> None:
        await self.journal.display_all_journals()

    async def search_journals_menu(self) -> None:
        keyword = input("enter a keyword for your search: ")
        await self.journal.search_journals(keyword)

    async def delete_journal_menu(self) -> None:
        journal_id = input("enter the ID of the magazine to be deleted: ")
        await self.journal.delete_journal(journal_id)
