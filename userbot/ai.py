from pyrogram import Client as user, filters
from pyrogram.types import Message
import requests
import google.generativeai as genai

genai.configure(api_key="AIzaSyD214hhYJ-xf8rfaWX044_g1VEBQ0ua55Q")

@user.on_message(filters.command("ai",prefixes="."))
async def ai_generate(client, message):
    user_input = message.text.split()[1:]

    if not user_input:
        await message.reply_text("Please provide your question after .ai")
        return

    user_input = " ".join(user_input)

    if user_input.lower() in ["who is your owner", "what is your owner name"]:  
        await message.reply_text(text=f"Me")
        return
        
    s = await message.reply_text("<code>processing.</code>")
    t = await s.edit("<code>processing..</code>")
    u = await t.edit("<code>processing...</code>")       
      
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config=generation_config,
        safety_settings=safety_settings
    )

    prompt_parts = [user_input]
    response = model.generate_content(prompt_parts)
    response = model.generate_content(prompt_parts)
    await message.reply_text(response.text)

    await u.delete()

