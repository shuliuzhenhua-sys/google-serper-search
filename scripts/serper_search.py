#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import urllib.error
import argparse

def search(query, search_type="web", gl=None, hl=None, tbs=None):
    api_key = os.environ.get("SERPER_API_KEY")
    if not api_key:
        return {"error": "SERPER_API_KEY environment variable not set"}

    # Type 映射
    type_map = {
        "search": "search",
        "images": "images",
        "videos": "videos",
        "places": "places",
        "maps": "maps",
        "reviews": "reviews",
        "news": "news",
        "shopping": "shopping",
        "lens": "lens",
        "scholar": "scholar",
        "patents": "patents",
        "autocomplete": "autocomplete"
    }
    
    # 确定 Endpoint
    st = type_map.get(search_type.lower(), "search")
    endpoint = f"https://google.serper.dev/{st}"

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    # 构建 Payload
    payload = {"q": query}
    if gl: payload["gl"] = gl
    if hl: payload["hl"] = hl
    if tbs: payload["tbs"] = tbs

    data = json.dumps(payload).encode("utf-8")

    try:
        req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Serper.dev Search CLI')
    parser.add_argument('query', help='Search query')
    parser.add_argument('--type', default='search', help='Search type (search, images, videos, news, etc.)')
    parser.add_argument('--gl', help='Country code (e.g. us, cn, jp)')
    parser.add_argument('--hl', help='Language code (e.g. en, zh-cn)')
    parser.add_argument('--tbs', help='Date range (qdr:h, qdr:d, qdr:w, qdr:m, qdr:y)')

    args = parser.parse_args()

    # 处理 Date range 映射
    tbs_map = {
        "any time": None,
        "past hour": "qdr:h",
        "past 24 hours": "qdr:d",
        "past week": "qdr:w",
        "past month": "qdr:m",
        "past year": "qdr:y"
    }
    tbs_val = tbs_map.get(args.tbs.lower()) if args.tbs else args.tbs

    result = search(args.query, args.type, args.gl, args.hl, tbs_val)
    print(json.dumps(result, indent=2, ensure_ascii=False))
