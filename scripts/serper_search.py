#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import urllib.error

def search(query, search_type="web"):
    api_key = os.environ.get("SERPER_API_KEY")
    if not api_key:
        return {"error": "SERPER_API_KEY environment variable not set"}

    endpoint = "https://google.serper.dev/search" if search_type == "web" else "https://google.serper.dev/images"

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    data = json.dumps({"q": query}).encode("utf-8")

    try:
        req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: serper_search.py <query> [web|images]")
        sys.exit(1)

    query = sys.argv[1]
    search_type = sys.argv[2] if len(sys.argv) > 2 else "web"

    result = search(query, search_type)
    print(json.dumps(result, indent=2, ensure_ascii=False))
