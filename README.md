# Prynix Discord Bot

> **Built by [Prynix](https://github.com/prynixdevs)** - A collaborative community of passionate high school developers exploring the world of technology through hands-on projects and continuous learning.

A smart Discord bot with intelligent chat capabilities, moderation tools, and essential server utilities. Created by [Prasoon Kandel](https://github.com/prasoonkandel) and the Prynix team, this bot brings AI-powered assistance and useful features to your Discord server.

## About Prynix

Prynix is a team of ambitious high school students who share a common passion for technology and innovation. Founded and led by Prasoon Kandel, our community brings together young minds from around the world to collaborate, learn, and build the future together. We're proudly affiliated with the [Hack Club](https://hackclub.com/) network.

## Add to Your Server

[Invite Prynix Bot](https://discord.com/oauth2/authorize?client_id=1419939758246989884&scope=bot%20applications.commands&permissions=8)

Click the link above to add the bot to your Discord server.

## Features

### AI Chat Integration

- AI-powered direct message responses
- Intelligent conversation handling with context awareness
- Custom personality and knowledge about the developer

### Moderation Commands

- `/kick4 <member>` - Kick a member from the server (requires Administrator or Moderator role)
- `/spam <times> <text>` - Send repeated messages (requires Administrator or Moderator role)
- `/notifyall <title> <description>` - Send notifications to all server members via DM (requires Administrator or Moderator role)
- `/announcement <title> <description>` - Post an announcement in the current channel (requires Administrator or Moderator role)

### Utility Commands

- `/calc <expression>` - Calculate mathematical expressions
- `/chat <message>` - Chat with the AI bot in any channel
- `/notify <member> <title> <description>` - Send a notification to a specific member
- `/mathquote` - Get an inspirational mathematics quote

### Automatic Features

- Welcome messages sent via DM when members join
- Goodbye messages sent via DM when members leave
- AI-powered DM conversations

## Requirements

- Python 3.8 or higher
- Discord.py 2.0.0 or higher
- python-dotenv 1.0.0 or higher
- requests 2.31.0 or higher

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd "Discord Bot"
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following variables:

```env
DISCORD_TOKEN=your_discord_bot_token
AI_KEY=your_ai_api_key
```

4. Run the bot:

```bash
python main.py
```

## Configuration

### Environment Variables

- `DISCORD_TOKEN` - Your Discord bot token from the Discord Developer Portal
- `AI_KEY` - Your AI API key for AI chat functionality

### Bot Permissions

The bot requires the following Discord permissions:

- Send Messages
- Embed Links
- Kick Members
- Read Message History
- Send Messages in DM
- View Channels
- Read Messages/View Channels

### Intents

The bot uses the following Discord intents:

- Message Content Intent
- Server Members Intent
- All standard intents

## Project Structure

```
Discord Bot/
├── main.py              # Main bot file with commands and events
├── back.py              # AI chat backend and API integration
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not included)
└── README.md           # This file
```

## Usage

### Setting Up Bot Permissions

Ensure your bot has Administrator permissions or create a "Moderator" role for users who should access moderation commands.

### AI Chat

Users can send direct messages to the bot to have AI-powered conversations.

### Example Commands

```
/calc 2 + 2 * 5
/chat What is Python?
/announcement "Server Update" "We have new rules!"
/notify @User "Reminder" "Don't forget about the event!"
```

## Developer

Developed by **[Prasoon Kandel](https://github.com/prasoonkandel)**

Prasoon is a passionate student developer from Nepal, currently studying Grade 9 (Technical Education - Computer Engineering) at Kalika Manavgyan Secondary School. Skilled in multiple programming languages including Python, JavaScript, C/C++, C#, JAVA, and Arduino, with a focus on building innovative solutions and continuous learning.

## Community

This bot is developed as part of the **[Prynix](https://github.com/prynixdevs)** community - a collaborative team of ambitious high school students who share a common passion for technology and innovation. We believe that age is just a number when it comes to creating meaningful solutions and pushing the boundaries of what's possible in tech.

### Connect With Us

- **Organization**: [Prynix Developers](https://github.com/prynixdevs)
- **Team Leader**: [Prasoon Kandel](https://github.com/prasoonkandel)
- **Affiliation**: Proud member of [Hack Club](https://hackclub.com/) network
- **Contact**: prynixdevelopment@gmail.com
- **Location**: Nepal

### What We Do

At Prynix, we:

- Build and collaborate on real-world projects
- Learn new technologies and frameworks
- Connect with peers who share similar interests
- Participate in hackathons and coding challenges
- Turn ideas into reality with mentorship and support

## Logging

The bot creates a `discord.log` file that records all bot activity and errors for debugging purposes.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page or submit a pull request.

## License

This project is open source and available for educational purposes.

## Acknowledgments

- Special thanks to all Prynix team members who contribute their time, skills, and passion
- Grateful to [Hack Club](https://hackclub.com/) for connecting student developers worldwide
- Built with passion by the upcoming generation of developers
- Powered by discord.py and AI technology

- Discord.py library for the excellent Discord API wrapper
- The Prynix community for support and collaboration

---

Built with dedication by the next generation of developers at Prynix.
