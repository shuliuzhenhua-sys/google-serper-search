---
name: google-serper-search
description: 使用 Serper API 进行网页搜索和图片搜索。当用户需要搜索最新信息、查找网页内容或搜索图片时使用此 skill。
---

# Google Serper Search

使用 Serper API 进行网页搜索和图片搜索。当用户需要搜索最新信息、查找网页内容或搜索图片时使用此 skill。

## 配置

需要设置环境变量：
```bash
export SERPER_API_KEY="your_api_key_here"
```

获取 API key：访问 https://serper.dev 注册并获取免费 API key。

## 使用方法

### 网页搜索

使用 `scripts/serper_search.py` 进行网页搜索：

```bash
python scripts/serper_search.py "搜索关键词" web
```

返回结果包含：
- 知识图谱信息
- 有机搜索结果（标题、链接、摘要）
- 相关问题（People Also Ask）
- 相关搜索

### 图片搜索

```bash
python scripts/serper_search.py "搜索关键词" images
```

返回结果包含图片 URL、缩略图、尺寸等信息。

## 示例

搜索 Apple Inc 的信息：
```bash
python scripts/serper_search.py "apple inc" web
```

搜索苹果的图片：
```bash
python scripts/serper_search.py "apple" images
```

## 参考

API 响应格式详见 `references/api_response.md`。
