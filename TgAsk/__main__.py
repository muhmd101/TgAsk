from pyrogram.types import BotCommand
from TgAsk.Client import app
from TgAsk.logger import LOGGER
import os, shutil, asyncio

log = LOGGER(__name__)

class pycache:
	def __init__(self, root_dir):
		self.root_dir = root_dir
	def remove_folder(self, folder_path):
		if os.path.exists(folder_path):
			try:
				shutil.rmtree(folder_path)
			except:
				pass
	def delete(self):
		for dirpath, dirnames, filenames in os.walk(self.root_dir):
			for dirname in dirnames:
				if dirname == "__pycache__":
					pycache_dir = os.path.join(dirpath, dirname)
					self.remove_folder(pycache_dir)

async def run():
	await app.start()
	await app.set_bot_commands(
		[
			BotCommand("start", "Start the bot"),
			BotCommand("support", "Support me"),
		]
	)
	pycache("./").delete()
	log.info("Bot started successfully")

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.run_forever()