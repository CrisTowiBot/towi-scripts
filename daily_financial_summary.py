import json

def web_search_helper(query):
    try:
        result = default_api.web_search(query=query)
        if result and 'web_search_response' in result and 'content' in result['web_search_response']:
            content = result['web_search_response']['content']
            start_tag = 'Source: Web Search\\n---\\n'
            end_tag = '\\n<<<END_EXTERNAL_UNTRUSTED_CONTENT'
            if start_tag in content:
                content = content.split(start_tag, 1)[1]
            if end_tag in content:
                content = content.split(end_tag, 1)[0]
            return content.strip()
        return "N/A"
    except Exception as e:
        return f"Error fetching data: {e}"


nyse_data = web_search_helper('NYSE major indices performance today')
bmv_data = web_search_helper('Mexican Stock Exchange IPC performance today')
mxn_usd_data = web_search_helper('MXN to USD exchange rate today')
news_data = web_search_helper('top global financial news headlines today')

summary_message = f"""
Here's your daily financial summary:

**NYSE Major Indices:**\n{nyse_data}

**Mexican Stock Exchange (BMV) IPC:**\n{bmv_data}

**MXN vs USD Exchange Rate:**\n{mxn_usd_data}

**Top Global Financial News:**\n{news_data}
"""

def send_message(message_content):
    try:
        default_api.message(action="send", to="telegram:1017021201", message=message_content)
        print("Financial summary sent successfully.")
    except Exception as e:
        print(f"Error sending message: {e}")

send_message(summary_message)
