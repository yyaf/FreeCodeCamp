import re

def calculate_progress(md_file):
    # 读取 Markdown 文件
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 匹配任务复选框
    total_tasks = len(re.findall(r"- 

\[.\]

", content))
    completed_tasks = len(re.findall(r"- 

\[x\]

", content, re.IGNORECASE))

    # 计算进度
    remaining_tasks = total_tasks - completed_tasks
    completion_rate = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    # 生成进度条（20 格）
    bar_length = 20
    filled_length = int(bar_length * completed_tasks // total_tasks)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)

    # 输出结果
    print(f"总任务数：{total_tasks}")
    print(f"已完成：{completed_tasks}")
    print(f"剩余：{remaining_tasks}")
    print(f"完成率：{completion_rate:.2f}%")
    print(f"[{bar}] 完成率：{completion_rate:.2f}%")

# 使用方法：把你的 Markdown 打卡表保存为 readme.md，然后运行：
# calculate_progress("readme.md")
