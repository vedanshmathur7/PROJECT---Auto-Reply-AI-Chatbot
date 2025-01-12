import pyautogui 
import time 
import pyperclip
import os

def open_chatgpt():
    try:
        # Path to launch Brave browser with ChatGPT
        app_path = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\chrome_proxy.exe'
        url = 'https://chatgpt.com/'
        os.startfile(f'{app_path} --profile-directory="Default" --ignore-profile-directory-if-not-exists {url}')
    except Exception as e:
        print(f"Error: {e}")

def copycontent():
    pyautogui.click(982, 1049)

    time.sleep(1)  # Wait for 1 second to ensure the click is registered
    while True:
        time.sleep(5)
        # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
        pyautogui.click(202, 357)
        pyautogui.moveTo(448, 141)
        pyautogui.dragTo(486, 901, duration=2.0, button='left')  # Drag for 1 second

        # Step 3: Copy the selected text to the clipboard
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
        
        chat_history = pyperclip.paste()
        print (chat_history)
if __name__ == "__main__":
    # copycontent()
    open_chatgpt()
