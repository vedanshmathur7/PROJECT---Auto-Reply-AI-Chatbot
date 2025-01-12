# **Auto-Reply AI Chatbot (Vedansh) 🤖**

This project automates the process of interacting with a chat application, analyzing chat history, and generating humorous "roast" responses using OpenAI's GPT-3.5-turbo model. The virtual assistant, named **Vedansh**, generates funny, roast-style responses based on the chat history.

## **Features 🚀**

- **Automated Chat Interaction**: Uses `pyautogui` to simulate mouse clicks and keyboard actions for interacting with the chat application.
- **Chat History Analysis**: Retrieves the chat history and analyzes it to determine the most recent message from a specific user.
- **Humorous Response Generation**: Integrates with OpenAI's GPT-3.5-turbo model to generate roast-style responses based on the chat history.
- **Clipboard Operations**: Uses `pyperclip` to copy and paste text between the chat application and the AI model.
- **Automatic Message Sending**: Automates the process of pasting and sending the generated response back into the chat.
- **Customizable AI Personality**: The assistant responds in both **Hindi** and **English**, with a humorous "roast" personality.

## **Libraries Used 📚**

- `pyautogui`: For automating mouse and keyboard interactions with the chat application.
- `time`: For adding delays between actions to ensure smooth execution.
- `pyperclip`: For clipboard operations (copying and pasting chat history and responses).
- `openai`: For interacting with OpenAI's GPT-3.5-turbo model to generate responses.
- `os`: For interacting with the system's file system and opening applications.

## **Setup 🛠️**

1. **Install Required Libraries**:
   - Make sure to install the required Python libraries by running the following command:

   ```bash
   pip install pyautogui pyperclip openai
   ```

2. **Get OpenAI API Key**:
   - You need to obtain an API key from [OpenAI](https://beta.openai.com/signup/). After getting the key, replace `<your api key>` with your actual OpenAI API key in the script.

3. **Browser Setup**:
   - The script uses the Brave browser to open ChatGPT. Ensure that the path to the browser's executable (`chrome_proxy.exe`) is correct. If you're using a different browser, update the `app_path` accordingly.

4. **Run the Script 🏃**:
   - After setting up everything, you can run the script using the following command:

   ```bash
   python your_script_name.py
   ```

   The script will open the browser, fetch chat history, generate a humorous response using OpenAI, and send the response back into the chat.

## **Workflow 🔄**

1. **Initialization**: The script launches the Brave browser and opens ChatGPT using the provided URL.
2. **Chat History Retrieval**: The script simulates mouse and keyboard actions to select and copy the chat history from the chat window.
3. **Response Generation**: It sends the chat history to OpenAI's GPT-3.5-turbo model to generate a roast-style response based on the context.
4. **Message Sending**: The generated response is copied to the clipboard and automatically pasted into the chat input field. The script simulates pressing the "Enter" key to send the message.
5. **Continuous Operation**: The script runs in a loop, periodically fetching chat history and responding to messages automatically.

## **Contributing 🤝**

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make changes, and submit a pull request.
