import time
import os
import random
import sys
from datetime import datetime

# ANSI 颜色代码
class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    """清空终端屏幕"""
    os.system('clear' if os.name == 'posix' else 'cls')

def get_random_color():
    """生成随机颜色"""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def rgb_to_ansi(r, g, b, background=False):
    """将RGB颜色转换为ANSI颜色代码"""
    mode = 48 if background else 38
    return f"\033[{mode};2;{r};{g};{b}m"

def generate_gradient(start_color, end_color, length):
    """生成颜色渐变序列"""
    colors = []
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    
    for i in range(length):
        r = int(r1 + (r2 - r1) * i / (length - 1) if length > 1 else r1)
        g = int(g1 + (g2 - g1) * i / (length - 1) if length > 1 else g1)
        b = int(b1 + (b2 - b1) * i / (length - 1) if length > 1 else b1)
        colors.append((r, g, b))
    
    return colors

def print_gradient_text(text, start_color, end_color, bold=False):
    """打印渐变颜色文本"""
    gradient = generate_gradient(start_color, end_color, len(text))
    colored_text = Colors.BOLD if bold else ""
    for i, char in enumerate(text):
        r, g, b = gradient[i]
        colored_text += f"{rgb_to_ansi(r, g, b)}{char}"
    colored_text += Colors.RESET
    print(colored_text)

def print_gradient_line(text, start_color, end_color, bold=False):
    """打印渐变颜色文本（整行渐变）"""
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    
    # 计算文本长度
    text_length = len(text)
    if text_length == 0:
        return
        
    # 生成渐变色
    gradient = generate_gradient(start_color, end_color, text_length)
    
    # 构建带颜色的文本
    colored_text = (Colors.BOLD if bold else "")
    for i, char in enumerate(text):
        r, g, b = gradient[i]
        colored_text += f"{rgb_to_ansi(r, g, b)}{char}"
    colored_text += Colors.RESET
    
    print(colored_text)

def print_logo():
    """打印ASCII艺术Logo（靠左显示）"""
    logo_lines = [
        "██████╗ ███████╗ ██╗███████╗██╗  ██╗",
        "██╔═══██╗██╔════╝███║╚══███╔╝╚██╗██╔╝",
        "██║   ██║███████╗╚██║  ███╔╝  ╚███╔╝",
        "██║▄▄ ██║╚════██║ ██║ ███╔╝   ██╔██╗",
        "╚██████╔╝███████║ ██║███████╗██╔╝ ██╗",
        " ╚══▀▀═╝ ╚══════╝ ╚═╝╚══════╝╚═╝  ╚═╝"
    ]
    
    # 生成随机渐变色
    start_color = get_random_color()
    end_color = get_random_color()
    
    # 为每行生成渐变色
    line_colors = generate_gradient(start_color, end_color, len(logo_lines))
    
    # 打印Logo（靠左显示，不加居中空格）
    print("\n")  # 添加一些空行
    for i, line in enumerate(logo_lines):
        # 获取当前行的颜色
        r, g, b = line_colors[i]
        # 打印靠左并着色的行
        print(f"{rgb_to_ansi(r, g, b)}{line}{Colors.RESET}")
    print("\n")  # 添加一些空行

def get_random_rainbow_color():
    """获取随机彩虹色"""
    colors = [
        (255, 0, 0),    # 红
        (255, 165, 0),  # 橙
        (255, 255, 0),  # 黄
        (0, 255, 0),    # 绿
        (0, 0, 255),    # 蓝
        (75, 0, 130),   # 靛
        (238, 130, 238) # 紫
    ]
    r, g, b = random.choice(colors)
    return rgb_to_ansi(r, g, b)

def run(command):
    """运行命令"""
    os.system(command)

def display_loading_bar():
    """显示加载条动画"""
    clear_screen()
    
    # 生成随机渐变色
    start_color = get_random_color()
    end_color = get_random_color()
    
    print_gradient_line("正在启动工具...", start_color, end_color, bold=True)
    print_gradient_line("+" + "-" * 40 + "+", start_color, end_color)
    
    # 加载动画
    for i in range(41):
        progress = "█" * i + " " * (40 - i)
        gradient = generate_gradient(start_color, end_color, 40)
        colored_progress = ""
        for j in range(40):
            r, g, b = gradient[j]
            if j < i:
                colored_progress += f"{rgb_to_ansi(r, g, b)}█"
            else:
                colored_progress += f"{rgb_to_ansi(r, g, b)} "
        
        print(f"\r|{colored_progress}{Colors.RESET}|", end='')
        time.sleep(0.05)  # 控制加载速度
    
    print_gradient_line("\n正在连接服务器...", start_color, end_color, bold=True)
    time.sleep(1.5)
    print_gradient_line("连接成功!", start_color, end_color, bold=True)
    time.sleep(1)

def print_gradient_menu(title, options, start_color, end_color):
    """打印渐变菜单"""
    # 计算总行数
    total_lines = 1 + len(options)  # 标题 + 选项
    
    # 为每一行生成颜色
    line_colors = generate_gradient(start_color, end_color, total_lines)
    
    # 打印标题
    r, g, b = line_colors[0]
    print(f"{rgb_to_ansi(r, g, b)}{Colors.BOLD}{title}{Colors.RESET}")
    
    # 打印选项
    for i, option in enumerate(options, 1):
        r, g, b = line_colors[i]
        print(f"{rgb_to_ansi(r, g, b)}{option}{Colors.RESET}")

def main_menu():
    """主菜单界面"""
    while True:
        clear_screen()
        
        # 显示Logo
        print_logo()
        
        # 生成随机渐变色
        start_color = get_random_color()
        end_color = get_random_color()
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 使用渐变菜单
        title = f"欢迎使用权少工具\n({current_time})"
        options = ["1.进入工具", "2.退出"]
        
        print_gradient_menu(title, options, start_color, end_color)
        
        choice = input(Colors.CYAN + "请输入选项: " + Colors.RESET)
        
        if choice == '1':
            tool_ui()
        elif choice == '2':
            print_gradient_line("感谢使用，再见!", start_color, end_color, bold=True)
            break
        else:
            print_gradient_line("无效选项，请重新输入!", start_color, end_color)
            time.sleep(1)

def tool_ui():
    """工具界面"""
    while True:
        clear_screen()
        
        # 显示Logo
        print_logo()
        
        # 生成随机渐变色
        start_color = get_random_color()
        end_color = get_random_color()
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 使用渐变菜单
        title = f"({current_time})\n------------作者：权少--------\n--------TG@QS6NB-------"
        options = [
            "1.PAK处理区",
            "2.mini_obb.pak处理区",
            "3.mini_obbzsdic_obb.pak处理区",
            "4.第一次启动点我",
            "5.退出工具"
        ]
        
        print_gradient_menu(title, options, start_color, end_color)
        
        choice = input(Colors.CYAN + "请输入选项: " + Colors.RESET)
        
        try:
            choice = int(choice)
            if choice == 1: 
                run("python /data/user/0/com.termux/files/home/4.0工具/权少/PAK解包.py")
            elif choice == 2: 
                run("python /data/user/0/com.termux/files/home/4.0工具/权少/mini_obb.pak.py")
            elif choice == 3: 
                run("python /data/user/0/com.termux/files/home/4.0工具/权少/mini_obbzsdic_obb.pak.py")
            elif choice == 4: 
                run("python 权限.py")
            elif choice == 5:
                print(f"{Colors.RED}退出程序成功!{Colors.RESET}")
                sys.exit(0)
            else:
                print(f"{Colors.RED}无效选项，请重新选择!{Colors.RESET}")
                
            # 执行完工具后暂停，等待用户按键继续
            input(f"{get_random_rainbow_color()}按回车键返回主菜单...{Colors.RESET}")
            
        except ValueError:
            print(f"{Colors.RED}请不要瞎鸡8⃣️ 乱选{Colors.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    display_loading_bar()
    main_menu()
