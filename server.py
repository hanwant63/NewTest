"""
Wrapper to run Telegram bot with Flask web server for Render deployment
This satisfies Render's port binding requirement while keeping the bot running
"""
import os
import sys
from multiprocessing import Process, set_start_method
from flask import Flask, jsonify, render_template, request
from ad_monetization import ad_monetization

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

@app.route('/watch-ad')
def watch_ad():
    session_id = request.args.get('session', '')
    verification_url = request.args.get('verification_url', '')
    ad1_url = request.args.get('ad1_url', '')
    ad2_url = request.args.get('ad2_url', '')
    ad3_url = request.args.get('ad3_url', '')
    
    return render_template('ad_verify.html', 
                         session=session_id,
                         verification_url=verification_url,
                         ad1_url=ad1_url, 
                         ad2_url=ad2_url, 
                         ad3_url=ad3_url)

@app.route('/api/verify-session', methods=['POST'])
def verify_session():
    """API endpoint to verify ad completion and get verification code"""
    data = request.get_json()
    session_id = data.get('session', '')
    
    success, code, message = ad_monetization.verify_ad_completion(session_id)
    
    return jsonify({
        'success': success,
        'code': code,
        'message': message
    })

def run_bot():
    """Run the Telegram bot in a separate process with long polling"""
    import main
    main.LOGGER(__name__).info("Starting Telegram bot from server.py (long polling)")
    main.bot.run()

if __name__ == '__main__':
    # Set multiprocessing start method for better compatibility
    try:
        set_start_method("spawn")
    except RuntimeError:
        pass
    
    # Start bot in background process (not daemon so it stays alive)
    bot_process = Process(target=run_bot)
    bot_process.start()
    
    # Start Flask server on port 5000 for Replit
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
