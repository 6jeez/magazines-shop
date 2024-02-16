from menu import Menu
from database import DatabaseManager


async def main():
    password = input("enter the administrator's password: ")

    admin_password = "228"
    if password != admin_password:
        print("invalid password, access denied.")
        return

    db_manager = DatabaseManager("journals.db")
    await db_manager.connect()
    await db_manager.create_table()

    menu = Menu(db_manager)
    await menu.main_menu()

    await db_manager.close()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
