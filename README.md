```markdown
# Twitter to WhatsApp Automation

This project contains code designed to automate the process of copying the latest tweet from a Twitter account and pasting it into a WhatsApp channel via WhatsApp Web. The code runs every 2 minutes without requiring any additional configuration on Windows. To prevent duplicate entries, a separate text file is used to track already posted tweets.

## Features

- Opens Twitter in Google Chrome.
- Selects the latest tweet from the specified Twitter account.
- Opens WhatsApp Web.
- Pastes the tweet text into a specified WhatsApp channel.
- Runs automatically every 2 minutes.
- Maintains a separate text file to avoid posting the same tweet multiple times.

## Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ghazayel/x2wp.git
   ```

2. **Install Dependencies**

   Make sure you have the necessary libraries installed. You may need packages like Selenium for browser automation. Install them using pip:

   ```bash
   pip install selenium
   ```

3. **Configure the Code**

   - Update the script with your Twitter account details and WhatsApp Web channel information.
   - Ensure Google Chrome is installed and the ChromeDriver executable is in your PATH.

4. **Run the Script**

   Execute the script using Python:

   ```bash
   python x2wp.py
   ```

5. **Automatic Execution**

   To ensure the script runs every 2 minutes, you can use Task Scheduler on Windows:
   
   - Open Task Scheduler.
   - Create a new task and set it to run the script every 2 minutes.

## Notes

- This script is designed to run on Windows and requires no additional configuration.
- Ensure your Twitter and WhatsApp Web sessions are logged in and accessible by the script.

## Contribution

This is the first working code generated from scratch by [@ghazayel](https://github.com/ghazayel). Contributions and feedback are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

Feel free to adjust any details to better fit your project!
