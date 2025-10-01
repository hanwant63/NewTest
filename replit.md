# Restricted Content Downloader Telegram Bot

## Overview
Advanced Telegram bot that downloads restricted content (photos, videos, audio files, documents) from Telegram private chats or channels. Now features user authentication, database management, admin controls, and usage limits.

## Project Setup (Completed)
- **Language**: Python 3.11
- **Database**: SQLite for user management
- **Dependencies**: Pyrofork, TgCrypto, Pyleaves, python-dotenv, psutil, pillow, uvloop
- **Bot Type**: Backend Telegram Bot (Console Application)
- **Deployment**: VM deployment (stateful, always running)
- **Performance**: Optimized for fast downloads/uploads with uvloop and parallel transfers

## Current State (2025-10-01)
✅ Python 3.11 installed  
✅ All dependencies installed (including uvloop for speed)
✅ Database system integrated (SQLite)
✅ Phone authentication system added
✅ Access control & user management
✅ Admin commands implemented
✅ Premium/Free tier system
✅ Workflow configured to run `python main.py`  
✅ Bot starts successfully  
✅ Deployment configuration set for VM target  
✅ .gitignore properly configured
✅ **Performance optimizations implemented:**
  - uvloop for 2-4x faster async operations
  - Parallel file transfers (max_concurrent_transmissions=8)
  - Optimized worker threads (workers=8)
  - TgCrypto for faster cryptographic operations

## Configuration Required
1. **Set up API credentials** (via Replit Secrets or `config.env`):
   - `API_ID`: Your Telegram API ID from [my.telegram.org](https://my.telegram.org)
   - `API_HASH`: Your Telegram API Hash from [my.telegram.org](https://my.telegram.org)
   - `BOT_TOKEN`: Bot token from [@BotFather](https://t.me/BotFather)
   - `OWNER_ID`: Your Telegram user ID (auto-added as admin on first start)
   - `SESSION_STRING`: (Optional) Fallback session string

2. **First Time Setup**:
   - Bot automatically creates `bot_database.db` on first run
   - Owner (set via OWNER_ID) is automatically added as admin
   - Users must login with their phone numbers to use the bot

## Key Features

### 🔐 User Authentication System
- **Phone Number Login**: Users login with their own phone numbers
- **OTP Verification**: Secure OTP-based authentication
- **2FA Support**: Full support for two-factor authentication
- **Personal Sessions**: Each user gets their own Telegram session
- **No Shared Credentials**: Eliminates SESSION_STRING conflicts

### 👥 User Management & Access Control
- **Free Users**: 5 downloads per day
- **Premium Users**: Unlimited downloads + batch features
- **Admin Users**: Full access + management commands
- **Ban System**: Ban/unban users from the bot
- **User Tracking**: Track downloads, activity, and subscriptions

### 📊 Database System
- **SQLite Database**: Stores user data, sessions, and statistics
- **User Profiles**: Track username, join date, activity
- **Daily Limits**: Automatic reset of daily download quotas
- **Subscription Management**: Premium expiry tracking
- **Broadcast History**: Log all broadcasts sent

### 🎯 Download Features
- Download media (photos, videos, audio, documents)
- Support for single media posts and media groups
- Real-time progress bars during downloads
- Copy text messages or captions from Telegram posts
- Batch download (Premium only)
- Personal user sessions for restricted content

## User Commands

### Basic Commands
- `/start` - Welcome message and setup instructions
- `/help` - Detailed help and examples
- `/myinfo` - View account info, limits, and subscription
- `/stats` - View bot system statistics

### Authentication Commands
- `/login +1234567890` - Start login with phone number
- `/verify 1 2 3 4 5` - Enter OTP code (with spaces)
- `/password <2FA_password>` - Enter 2FA password if enabled
- `/logout` - Logout from account
- `/cancel` - Cancel pending authentication

### Download Commands
- `/dl <post_URL>` - Download media from Telegram post
- `/bdl <start_link> <end_link>` - Batch download (Premium only)
- Just paste a link - Auto-download without command

## Admin Commands

### User Management
- `/addadmin <user_id>` - Add new administrator
- `/removeadmin <user_id>` - Remove admin privileges
- `/setpremium <user_id> [days]` - Grant premium (default 30 days)
- `/removepremium <user_id>` - Remove premium subscription
- `/ban <user_id>` - Ban user from bot
- `/unban <user_id>` - Unban user
- `/userinfo` - Get user information

### Bot Management
- `/adminstats` - Detailed bot statistics
- `/broadcast <message>` - Send message to all users
- `/logs` - Download bot logs (admin only)
- `/killall` - Cancel all pending downloads

## Usage Limits
- **Free Users**: 5 downloads per day
- **Premium Users**: Unlimited downloads
- **Admin Users**: Unlimited downloads + management access

## Recent Changes (2025-10-01)
- ✅ Integrated database system (SQLite)
- ✅ Added phone authentication (no more shared SESSION_STRING)
- ✅ Implemented user management & access control
- ✅ Added premium/free tier system with daily limits
- ✅ Created admin command suite
- ✅ Added broadcast functionality
- ✅ Implemented ban/unban system
- ✅ Added user statistics tracking
- ✅ Fixed SESSION_STRING conflict issues
- ✅ **Performance Optimizations (Latest):**
  - Installed uvloop for 2-4x faster async event loop
  - Configured parallel file transfers (max_concurrent_transmissions=8)
  - Optimized worker count from 1000 to 8 for better resource utilization
  - All client creation points updated with optimal settings

## Architecture

### Core Files
- **main.py** - Bot initialization, command handlers, and routing
- **config.py** - Environment variable handling and configuration
- **database.py** - SQLite database manager for user data
- **phone_auth.py** - Phone number authentication handler
- **access_control.py** - Decorators for permissions and limits
- **admin_commands.py** - Admin command implementations

### Helper Modules
- **helpers/files.py** - File operations and size handling
- **helpers/msg.py** - Message parsing and link processing  
- **helpers/utils.py** - Media processing and upload utilities
- **logger.py** - Structured logging configuration

### Database Schema
- **users** - User profiles, sessions, subscriptions
- **admins** - Administrator privileges
- **daily_usage** - Download limits tracking
- **broadcasts** - Broadcast history

## Security Features
- Encrypted session storage in database
- Individual user sessions (no shared credentials)
- Admin-only commands with decorators
- Ban system to prevent abuse
- Daily rate limiting for free users
- Secure OTP and 2FA authentication