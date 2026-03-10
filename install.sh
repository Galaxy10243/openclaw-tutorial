#!/bin/bash
# OpenClaw 安装脚本 (macOS / Linux)

set -e

echo "🦞 OpenClaw 安装脚本"
echo "===================="

# 1. 检查 Node.js
echo "📦 检查 Node.js..."
if ! command -v node &> /dev/null; then
    echo "❌ Node.js 未安装，请先安装 Node.js 18+"
    exit 1
fi

node_version=$(node -v)
echo "✅ Node.js 版本: $node_version"

# 2. 检查 Python
echo "📦 检查 Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 未安装，请先安装 Python 3.10+"
    exit 1
fi

python_version=$(python3 --version)
echo "✅ Python 版本: $python_version"

# 3. 安装 OpenClaw
echo "📦 安装 OpenClaw..."
npm install -g openclaw

# 4. 初始化
echo "⚙️ 初始化 OpenClaw..."
openclaw init

# 5. 启动网关
echo "🚀 启动 OpenClaw 网关..."
openclaw gateway start

echo ""
echo "===================="
echo "✅ 安装完成！"
echo "请运行: openclaw status"
echo "===================="
