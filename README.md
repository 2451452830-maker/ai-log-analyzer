# AI日志分析助手 (AI Log Analyzer)

## 项目简介
这是一个基于 Python 和 DeepSeek API 开发的运维提效工具。它读取本地的日志文件（`app.log`），通过调用大模型API自动分析系统风险，并生成包含 P0/P1 优先级处置建议的巡检报告。

## 技术栈
- Python 3.14
- OpenAI SDK (DeepSeek API)
- 文件I/O与异常处理

## 核心功能
- 读取本地 `app.log` 日志文件，自动提取 ERROR 和 WARNING 级别信息。
- 动态拼接 Prompt，调用大模型API进行智能根因分析。
- 输出带优先级的运维巡检报告（如识别出“磁盘92%可能诱发数据库超时”的因果链）。

## 如何运行
1. 克隆本仓库，确保本地有 Python 环境。
2. 安装依赖：`pip3 install openai`
3. 设置环境变量：`export DEEPSEEK_API_KEY="你的密钥"`
4. 运行脚本：`python3 test_deepseek.py`
