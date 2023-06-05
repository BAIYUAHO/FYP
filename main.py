import tkinter as tk

def open_window1():
    # 这里是打开功能1的窗口的代码
    pass

def open_window2():
    # 这里是打开功能2的窗口的代码
    pass

# 创建主窗口
root = tk.Tk()
root.title("Preschool Mathematics Education Based on Image Detection")

# 创建按钮
button1 = tk.Button(root, text="物品数量检测", command=open_window1)
button2 = tk.Button(root, text="手写数字检测", command=open_window2)
# ... 创建更多的按钮

# 将按钮添加到主窗口
button1.pack()
button2.pack()
# ... 添加更多的按钮

# 运行主窗口
root.mainloop()
