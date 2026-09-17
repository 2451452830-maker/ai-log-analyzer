import os
from openai import OpenAI

def analyze_log(file_path):
    """
    读取本地日志文件，调用大模型API生成运维巡检报告
    """
    # 1. 读取日志文件
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            log_content = f.read()
        print(f"--- 已成功读取日志文件: {file_path}，正在分析 ---")
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        return None

    # 2. 初始化API客户端
    client = OpenAI(
        api_key=os.environ.get("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com"
    )

    # 3. 构造Prompt
    prompt = f"我是一名运维工程师，这是一段设备日志：\n{log_content}\n请帮我分析这段日志，找出潜在的系统风险，并生成一段简短的运维巡检报告。"

    # 4. 发送请求并获取结果
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个专业的运维开发助手"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"API调用失败: {e}")
        return None

# --- 主程序运行入口 ---
if __name__ == "__main__":
    result = analyze_log("app.log")
    if result:
        print("\n" + "="*30 + " 报告结果 " + "="*30 + "\n")
        print(result)
