from pyrogram import Client
import config
from ..logging import LOGGER

# Global lists to be used by other modules
assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        self.clients = []
        # List of session strings from config
        session_strings = [
            config.STRING1, config.STRING2, config.STRING3, 
            config.STRING4, config.STRING5
        ]

        for i, session in enumerate(session_strings, start=1):
            if session:
                client = Client(
                    name=f"DilXAss{i}",
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    session_string=str(session),
                    no_updates=True,
                )
                # Setting dynamic attributes self.one, self.two etc for backward compatibility
                setattr(self, self._get_attr_name(i), client)
                self.clients.append((i, client))

    def _get_attr_name(self, index):
        mapping = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
        return mapping.get(index)

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")
        
        for i, client in self.clients:
            try:
                await client.start()
                
                # Join support chat
                try:
                    await client.join_chat("NOBITA_SUPPORT")
                except Exception:
                    pass

                # Check Log Group Access
                try:
                    await client.send_message(config.LOGGER_ID, f"Assistant {i} Started")
                except Exception:
                    LOGGER(__name__).error(
                        f"Assistant Account {i} failed to access the Log Group. "
                        "Ensure it is an admin in your log group!"
                    )
                    # Optional: exit() if you want the bot to stop completely on failure
                    # exit() 

                # Set metadata
                client.id = client.me.id
                client.name = client.me.mention
                client.username = client.me.username
                
                assistants.append(i)
                assistantids.append(client.id)
                
                LOGGER(__name__).info(f"Assistant {i} Started as {client.me.first_name}")
                
            except Exception as e:
                LOGGER(__name__).error(f"Assistant {i} failed to start: {str(e)}")

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        for i, client in self.clients:
            try:
                await client.stop()
                LOGGER(__name__).info(f"Assistant {i} stopped.")
            except Exception:
                pass
