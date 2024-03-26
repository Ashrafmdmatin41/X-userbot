from pyrogram import Client, filters
import requests

@Client.on_message(filters.command("repo", prefixes=[".", "/"]))
async def repo(client, message):
    if len(message.command) > 1:
        query = ' '.join(message.command[1:])
        try:
            response = requests.get(f"https://api.github.com/search/repositories?q={query}")
            response.raise_for_status()  

            data = response.json()
            if data['total_count'] > 0:
                repo = data['items'][0]
                description = repo.get('description', 'No description provided')

                reply = f"**{repo['name']}**\n\n" \
                       f"** Description:** <code>{description}</code>\n" \
                       f"** URL:** {repo['html_url']}\n" \
                       f"**✨ Stars:** <code>{repo['stargazers_count']}</code>\n" \
                       f"** Forks:** <code>{repo['forks_count']}</code>"

                await message.reply_text(f"{reply}", disable_web_page_previews=False)
            else:
                await message.reply_text("No results found for your query.")

        except requests.exceptions.RequestException as error:
            await message.reply_text(f"An error occurred= {error}")
    else:
        await message.reply_text("Usage: /repo {repo_name} or .repo {repo_name}")
