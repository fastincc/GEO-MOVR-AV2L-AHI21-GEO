#!/usr/bin/env python3
import time
import subprocess
import os

DESKTOP_FILE = os.path.expanduser('~/Desktop/domain.txt')

def get_clipboard_text():
    """获取 macOS 系统的当前剪贴板内容"""
    try:
        res = subprocess.run(['pbpaste'], capture_output=True, text=True, check=True)
        return res.stdout
    except Exception:
        return ""

def main():
    print(f"[*] 剪贴板监听脚本已启动...")
    print(f"[*] 检测到新内容将自动追加到: {DESKTOP_FILE}")
    print(f"[*] 按 Ctrl+C 退出监听\n")

    last_text = get_clipboard_text()

    try:
        while True:
            time.sleep(0.5)
            current_text = get_clipboard_text()

            # 如果剪贴板发生变化且不为空
            if current_text and current_text != last_text:
                last_text = current_text
                cleaned = current_text.strip()
                if cleaned:
                    with open(DESKTOP_FILE, 'a', encoding='utf-8') as f:
                        f.write(cleaned + '\n')
                    print(f"[+] 捕获新内容并写入 ({len(cleaned.splitlines())} 行):")
                    for line in cleaned.splitlines()[:3]:
                        print(f"    - {line}")
                    if len(cleaned.splitlines()) > 3:
                        print("    ...")
    except KeyboardInterrupt:
        print("\n[*] 监听已退出。")

if __name__ == '__main__':
    main()
