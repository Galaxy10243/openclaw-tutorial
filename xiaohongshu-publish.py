#!/usr/bin/env python3
"""
小红书自动发布脚本示例
用于 OpenClaw 技能：xiaohongshu-mcp
"""
import requests
import sys
import os

BASE_URL = "http://localhost:18060"

def publish_note(title, content, images):
    """发布笔记"""
    payload = {
        "title": title[:30],  # 标题最多30字
        "content": content,
        "images": images.split(",") if images else []
    }
    
    resp = requests.post(
        f"{BASE_URL}/api/v1/publish",
        json=payload,
        timeout=60
    )
    
    result = resp.json()
    if result.get("success"):
        print(f"✅ 发布成功!")
        return True
    else:
        print(f"❌ 发布失败: {result}")
        return False

def search_notes(keyword, limit=10):
    """搜索笔记"""
    resp = requests.post(
        f"{BASE_URL}/api/v1/feeds/search",
        json={"keyword": keyword, "page": 1},
        timeout=30
    )
    
    result = resp.json()
    if result.get("success"):
        feeds = result.get("data", {}).get("feeds", [])[:limit]
        return feeds
    return []

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='小红书发布工具')
    parser.add_argument('command', choices=['publish', 'search'], help='命令')
    parser.add_argument('--title', '-t', help='标题')
    parser.add_argument('--content', '-c', help='内容')
    parser.add_argument('--images', '-i', help='图片URL，用逗号分隔')
    parser.add_argument('--keyword', '-k', help='搜索关键词')
    
    args = parser.parse_args()
    
    if args.command == "publish":
        if not args.title or not args.content:
            print("❌ 请提供标题和内容")
            sys.exit(1)
        publish_note(args.title, args.content, args.images or "")
    
    elif args.command == "search":
        keyword = args.keyword or "热门"
        results = search_notes(keyword)
        print(f"🔍 找到 {len(results)} 篇笔记:")
        for i, feed in enumerate(results, 1):
            note = feed.get("noteCard", {})
            print(f"[{i}] {note.get('displayTitle', '无标题')[:60]}")
