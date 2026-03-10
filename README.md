# OpenClaw 完整配置教程

> 🦞 一个让 AI 帮你干活的智能助手框架

简体中文 | [English](./README_EN.md)

---

## 📖 目录

1. [简介](#1-简介)
2. [安装](#2-安装)
3. [快速开始](#3-快速开始)
4. [配置 Telegram](#4-配置-telegram)
5. [创建智能体](#5-创建智能体)
6. [技能安装](#6-技能安装)
7. [定时任务](#7-定时任务)
8. [小红书自动发布](#8-小红书自动发布)
9. [常见问题](#9-常见问题)

---

## 1. 简介

**OpenClaw** 是一个强大的 AI 助手框架，可以帮你：

- 🤖 管理多个 AI 智能体
- 📱 集成 Telegram、Discord 等通讯平台
- 🧩 安装各种技能（Skills）
- ⏰ 设置定时任务
- 🔄 自动化工作流程

---

## 2. 安装

### 环境要求

- Node.js 18+
- Python 3.10+
- Windows / macOS / Linux

### 安装步骤

```bash
# 1. 安装 OpenClaw
npm install -g openclaw

# 2. 初始化配置
openclaw init

# 3. 启动网关
openclaw gateway start
```

---

## 3. 快速开始

### 基础命令

```bash
# 查看状态
openclaw status

# 查看智能体列表
openclaw agents list

# 查看技能列表
openclaw skills list
```

### 配置文件

配置文件位于 `~/.openclaw/openclaw.json`：

```json
{
  "agents": {
    "list": [
      {
        "id": "main",
        "identity": {
          "name": "小管家",
          "emoji": "🏠"
        }
      }
    ]
  },
  "channels": {
    "telegram": {
      "dmPolicy": "open",
      "groupPolicy": "open"
    }
  }
}
```

---

## 4. 配置 Telegram

### 4.1 创建机器人

1. 打开 Telegram，搜索 @BotFather
2. 发送 `/newbot` 创建新机器人
3. 复制机器人 Token

### 4.2 配置 OpenClaw

```bash
openclaw config set channels.telegram.accounts.default.botToken "你的Token"
```

### 4.3 启动服务

```bash
openclaw gateway restart
```

---

## 5. 创建智能体

### 5.1 创建新的智能体

```bash
openclaw agents add my-agent --name "我的智能体" --emoji "🤖"
```

### 5.2 内置智能体

| 智能体 | 功能 |
|--------|------|
| main | 🏠 小管家 - 总管 |
| media-operations | 📱 自媒体运营 |
| office-worker | 📎 办公助手 |
| tech-engineer | 💻 技术工程师 |
| research-professor | 🔬 科研教授 |

---

## 6. 技能安装

### 6.1 搜索技能

```bash
clawhub search 小红书
clawhub search video
clawhub search marketing
```

### 6.2 安装技能

```bash
clawhub install xiaohongshu-mcp
clawhub install douyin-video-publish
clawhub install fanqie-masterclass
```

### 6.3 常用技能推荐

| 技能 | 功能 |
|------|------|
| xiaohongshu-mcp | 小红书自动发布 |
| douyin-video-publish | 抖音视频发布 |
| fanqie-masterclass | 番茄小说写作 |
| video-frames | 视频帧提取 |
| code | 代码开发 |
| web | Web开发 |
| productivity | 效率提升 |

---

## 7. 定时任务

### 7.1 Windows 创建定时任务

```bash
schtasks /create /tn "MyTask" /tr "python script.py" /sc minute /mo 30
```

### 7.2 查看任务

```bash
schtasks /query /tn "MyTask"
```

---

## 8. 小红书自动发布

### 8.1 配置 MCP 服务

1. 下载 xiaohongshu-mcp 工具
2. 扫码登录
3. 启动服务

```bash
# 登录
./xiaohongshu-login-windows-amd64.exe

# 启动服务
./xiaohongshu-mcp-windows-amd64.exe
```

### 8.2 发布笔记

```python
python auto_publish.py publish \
  --title "标题" \
  --content "内容" \
  --images "图片URL"
```

---

## 9. 常见问题

### Q1: Telegram 收不到消息？

检查配置：
```bash
openclaw channels status
```

### Q2: 技能安装失败？

使用 `--force` 参数：
```bash
clawhub install xxx --force
```

### Q3: 如何更新 OpenClaw？

```bash
npm update -g openclaw
```

---

## 📞 支持

- 📖 文档：https://docs.openclaw.ai
- 💬 Discord：https://discord.com/invite/clawd
- 🐙 GitHub：https://github.com/openclaw/openclaw

---

## 📝 更新日志

### 2026-03-10
- 初始版本发布
- 支持 Telegram 集成
- 支持多智能体管理
- 支持技能系统

---

*本教程由 OpenClaw 自动生成*
