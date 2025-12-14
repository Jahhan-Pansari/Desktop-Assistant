# # # # from google import genai

# # # # client = genai.Client()

# # # # response = client.models.generate_content(
# # # #     model="gemini-2.5-flash",
# # # #     contents="Explain how AI works in a few words",
# # # # )

# # # # print(response.text)
# # # import google.generativeai as genai

# # # genai.configure(api_key="API_KEY_HERE")

# # # response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
# # #     "Explain how AI works in a few words"
# # # )

# # # print(response.text)
# # import google.generativeai as genai

# # genai.configure(api_key="...your API key...")

# # model = genai.GenerativeModel("gemini-2.0-flash-lite")

# # response = model.generate_content("Explain how AI works in a few words")

# # print(response.text)
# import google.generativeai as genai

# # Configure your API key
# genai.configure(api_key="API_KEY_HERE")

# # Choose a stable free model
# model = genai.GenerativeModel("gemini-2.0-flash-lite")

# # Send a prompt
# response = model.generate_content(
#     "you will just provide me with the website link, just provide the link. open youtube"
# )

# # Print the response
# print(response.text)

from groq import Groq

client = Groqclient = Groq(api_key="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")


response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "you will just provide me with the website link, just provide the link. open youtube"}
    ]
)

print(response.choices[0].message.content)

    # from groq import Groq

    # client = Groqclient = Groq(api_key="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")


    # response = client.chat.completions.create(
    #     model="llama-3.1-8b-instant",
    #     messages=[
    #         {"role": "user", "content": "When I give a command like ‘open youtube’, return only the official URL of that website. No explanation, no extra text, no formatting, no quotes — just the direct link. For example: If I say ‘open youtube’, reply only with https://www.youtube.com."}
    #     ]
    # )

    # responseontext = response.choices[0].message.content
    # print(responseontext)

    # response = client.chat.completions.create(
    #     model="llama-3.1-8b-instant",
    #     messages=[
    #         {"role": "user", "content": (f"now give me the only url to {query}")}
    #     ]
    # )

    # responseontext2 = response.choices[0].message.content
    # print(responseontext2)
    # webbrowser.open(responseontext2)
    # from groq import Groq

    # client = Groq()
    # completion = client.chat.completions.create(
    #     model="openai/gpt-oss-120b",
    #     messages=[
    #     {
    #         "role": "system",
    #         "content": "just give me the link of the app i ask for, just the link and nothing else"
    #     },
    #     {
    #         "role": "user",
    #         "content": query
    #     }
    #     ],
    #     temperature=1,
    #     max_completion_tokens=8192,
    #     top_p=1,
    #     reasoning_effort="medium",
    #     stream=True,
    #     stop=None
    # )

    # for chunk in completion:
    #     print(chunk.choices[0].delta.content or "", end="")
