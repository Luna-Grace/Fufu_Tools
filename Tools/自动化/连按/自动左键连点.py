import pyautogui
import keyboard
import time
from colorama import init, Fore

init(autoreset=True)

while True:
    try:
        click_interval = float(input("请输入每次点击的间隔时间(秒)："))
        break
    except ValueError:
        print(f"{Fore.RED}✕{Fore.RESET} 输入的数据不合法，请重新输入。")

# 控制自动点击的开关
auto_clicking = False

# 控制提示消息
first_time = True

def toggle_auto_click():
    global auto_clicking
    global first_time
    # 切换自动点击状态
    auto_clicking = not auto_clicking
    if first_time:
        print("自动点击 已开始", end="")# 首次按下F8必定是开始自动点击
        first_time = False # 标记为非首次
    else:
        if auto_clicking:
            print("\r自动点击 已开始", end="")
        else:
            print("\r自动点击 已停止", end="")

def auto_click():
    while True:
        if auto_clicking:
            pyautogui.click()
            time.sleep(click_interval)
        # 这里稍微延迟一下，减少CPU使用率
        time.sleep(0.01)

# 绑定F8键，用于切换自动点击状态
keyboard.add_hotkey('F8', toggle_auto_click)

print(f"{Fore.GREEN}✓{Fore.RESET} 程序已启动，按下F8键开始/停止自动左键连续点击。")
print(f"{Fore.BLUE}[!]{Fore.RESET} 按Ctrl+C可结束程序...")
auto_click()
