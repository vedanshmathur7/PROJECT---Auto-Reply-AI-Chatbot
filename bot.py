import pyautogui 
import time 
import pyperclip
from openai import OpenAI
# import os

client = OpenAI(
  api_key="<your api key>",
)

import os

def open_chatgpt():
    try:
        # Path to launch Brave browser with ChatGPT
        app_path = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\chrome_proxy.exe'
        url = 'https://chatgpt.com/'
        os.startfile(f'{app_path} --profile-directory="Default" --ignore-profile-directory-if-not-exists {url}')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    open_chatgpt()



pyautogui.click(982, 1049)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.click(215, 242)
    pyautogui.moveTo(448, 141)
    pyautogui.dragTo(486, 901, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1707, 442)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a person named Vedansh who speaks hindi as well as english. You are from India. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
        {"role": "system", "content": "Do not start like this "},
        {"role": "user", "content": chat_history}
    ]
    )

    response = completion.choices[0].message.content
    pyperclip.copy(response)

    # Step 5: Click at coordinates (1808, 1328)
    pyautogui.click(1363, 955)
    time.sleep(1)  # Wait for 1 second to ensure the click is registered

    # Step 6: Paste the text
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

    # Step 7: Press Enter
    pyautogui.press('enter')