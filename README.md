# Stock-DM-Notifier

Stock-DM-Notifier is a Python script that aims to notify users when it would be a good time to invest, providing a slight edge with long-term passive investing. The script utilises the Relative Strength Index (RSI) indicator to identify oversold conditions in stock assets.

## Installation

To set up Stock-DM-Notifier, perform the following steps:

1. Clone the repository:
```git clone https://github.com/<username>/stock-dm-notifier.git```
2. Navigate to the project directory:
```cd stock-dm-notifier```
3. Configure the script by editing the "config.json" file
4. Build the docker image:
```docker build -t <name> .```
5. Run the Docker container:
```docker run <name>```

## Configuration & Usage
The script will continuously check the specified stock asset once per day at 5am using the RSI indicator. When the RSI value falls below the defined threshold (indicating an oversold condition), the script will send a DM notification on Discord.

```
{
  "discord_token": "YOUR_DISCORD_TOKEN",
  "discord_user_id": "YOUR_DISCORD_USER_ID",
  "stock_symbol": "SPY",
  "rsi_period": 10,
  "rsi_threshold": 30
}
```
discord_token: Your Discord bot token. You can create a bot and obtain the token by following the Discord Developer Portal instructions.
discord_user_id: Your Discord user ID. This is the user ID to which the DM notifications will be sent. To find your user ID, enable Developer Mode in Discord's Appearance settings and right-click on your profile to copy your ID.
stock_symbol: The symbol of the stock asset you want to monitor (e.g., "SPY" for S&P 500).
rsi_period: The period length used for calculating the Relative Strength Index (RSI). The default is 10.
rsi_threshold: The RSI threshold value below which an asset is considered oversold. The default is 30.

## Future Enhancements
The following enhancements may be considered for future versions of Stock-DM-Notifier:

- Support for other messaging platforms such as WhatsApp or Telegram.
- Integration of several additional technical indicators beyond RSI to provide a more comprehensive investment strategy.

## Legal Disclaimer
This project and its associated script, Stock-DM-Notifier, are provided for informational purposes only. The script's aim is to assist users in making informed investment decisions, but it should not be considered financial advice. The notifications generated by the script should not be solely relied upon for investment decisions, and users are encouraged to conduct their own research and consult with a qualified financial advisor before making any investment choices.

Use Stock-DM-Notifier at your own risk. The developer(s) of this project and script assume no responsibility or liability for any financial losses or damages incurred as a result of using this tool.

Please exercise caution and make investment decisions responsibly.
