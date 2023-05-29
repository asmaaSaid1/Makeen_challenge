# -*- coding: utf-8 -*-
"""
Created on Sat May 20 22:13:18 2023

@author: Asma
"""
import openai
openai.api_key = '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'
messages = [ {"role": "system", "content":
			"You are a intelligent assistant."} ]
while True:
	message = input("User : ")
	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)
	reply = chat.choices[0].message.content
	print(f"ChatGPT: {reply}")
	messages.append({"role": "assistant", "content": reply})




