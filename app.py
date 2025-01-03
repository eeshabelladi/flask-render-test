from flask import Flask, jsonify, request
import asyncio
from async_crawler import fetch_data

app = Flask(__name__)

@app.route('/crawl', methods=['GET'])
def crawl():
    try:
        # Get the URL from the request arguments
        url = request.args.get('url', default="https://docs.npmjs.com/cli/v9/commands/npm-install")
        
        # Run the async function in an event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(fetch_data(url))
        truncated_result = result[:1000] + "..." if len(result) > 1000 else result
        # Return the result as JSON
        return jsonify({"data": truncated_result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run()
