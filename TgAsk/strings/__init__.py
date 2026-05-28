from yaml import safe_load
import os

languages = {}

for filename in os.listdir("./TgAsk/strings/langs/"):
	if filename.endswith(".yml"):
		base_name = os.path.basename(filename)
		language_code, ext = os.path.splitext(base_name)
		with open(f"./TgAsk/strings/langs/{filename}", encoding="utf-8") as lang:
			languages[language_code.lower()] = safe_load(lang)


def get_string(
	lang: str | None = None,
	value: str | None = None,
) -> str:
	lang = lang.lower()
	context = languages.get(lang, languages.get("en"))
	string = context[value]
	return str(string)