"""
Wrapper to run Telegram bot with Flask web server for Render deployment
This satisfies Render's port binding requirement while keeping the bot running
"""
import os
import asyncio
import threading
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'status': 'online',
        'message': 'Telegram Bot is running!',
        'bot': 'Restricted Content Downloader'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

def run_bot():
    """Run the Telegram bot in a separate thread with its own event loop"""
    # Create a new event loop for this thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # Now import and run the bot
    import main  # This imports and runs the bot

if __name__ == '__main__':
    # Start bot in background thread
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # Start Flask server (satisfies Render's port requirement)
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
