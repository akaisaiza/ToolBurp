import requests

def extract_urls_from_burp_history(burp_api_url):
    history_url = burp_api_url + "scan/$ISSUE_ID/history"
    issues_url = burp_api_url + "scan/issues"

    # Lấy danh sách tất cả các vấn đề quét
    response = requests.get(issues_url)
    issues = response.json()

    urls = []

    # Lặp qua từng vấn đề và lấy lịch sử cho mỗi vấn đề
    for issue in issues:
        issue_id = issue["issueId"]
        issue_history_url = history_url.replace("$ISSUE_ID", str(issue_id))
        response = requests.get(issue_history_url)
        history = response.json()

        # Lặp qua từng lịch sử và lấy URL
        for entry in history:
            url = entry["url"]
            urls.append(url)

    return urls
