import sys
import os
import markdown2
import requests

def publish_to_medium(token, html_content, title, publish_status="draft"):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "title": title,
        "contentFormat": "html",
        "content": html_content,
        "publishStatus": publish_status
    }
    response = requests.post("https://api.medium.com/v1/users/me/posts", json=data, headers=headers)
    if response.status_code == 201:
        print("Successfully published to Medium:", response.json().get("data", {}).get("url", ""))
    else:
        print("Failed to publish:", response.status_code, response.text)

def main():
    token = sys.argv[1]
    file_path = sys.argv[2]
    publish_status = sys.argv[3] if len(sys.argv) > 3 else "draft"

    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    with open(file_path, "r") as f:
        markdown_content = f.read()

    html_content = markdown2.markdown(markdown_content)
    title = os.path.basename(file_path).replace(".md", "")

    publish_to_medium(token, html_content, title, publish_status)

if __name__ == "__main__":
    main()
