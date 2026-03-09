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

# Fetch tech news data
tech_headlines = web_search_helper('top tech news headlines today')
ai_ml_news = web_search_helper('latest AI ML advancements news')
cloud_updates = web_search_helper('AWS Azure GCP cloud computing updates news')
programming_trends = web_search_helper('programming language framework trends news')
cybersecurity_news = web_search_helper('latest cybersecurity news')
big_tech_news = web_search_helper('major tech company news today')

# Format the summary message
summary_message = f"""
Here's your daily Tech News Briefing:

**Top Tech Headlines:**
{tech_headlines}

**AI/ML Advancements:**
{ai_ml_news}

**Cloud Computing Updates:**
{cloud_updates}

**Programming Language & Framework Trends:**
{programming_trends}

**Cybersecurity News:**
{cybersecurity_news}

**Big Tech Company News:**
{big_tech_news}
"""

# Send the message
def send_message(message_content):
    try:
        default_api.message(action="send", to="telegram:1017021201", message=message_content)
        print("Tech news briefing sent successfully.")
    except Exception as e:
        print(f"Error sending message: {e}")

send_message(summary_message)
