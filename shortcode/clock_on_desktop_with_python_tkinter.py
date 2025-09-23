import tkinter as tk
import time
import math

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        self.root.overrideredirect(True)  # 移除視窗邊框
        self.root.wm_attributes("-topmost", True)  # 永遠置頂
        self.root.wm_attributes("-transparentcolor", "white")  # 白色透明（Windows 支援）
        self.root.configure(bg="white")

        self.canvas_size = 600
        self.center = self.canvas_size // 2
        self.clock_radius = self.center - 10

        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="white", highlightthickness=0)
        self.canvas.pack()

        # 位置移動
        self.canvas.bind("<Button-1>", self.start_move)
        self.canvas.bind("<B1-Motion>", self.do_move)


        self.update_clock()

    def draw_clock_face(self):
        self.canvas.delete("all")
        self.canvas.create_oval(
            self.center - self.clock_radius, self.center - self.clock_radius,
            self.center + self.clock_radius, self.center + self.clock_radius,
            fill="black", outline="gray"
        )

        # 表心
        self.canvas.create_oval(
            self.center - 5, self.center - 5,
            self.center + 5, self.center + 5,
            fill="gold", outline=""
        )


        for i in range(12):
            angle = math.radians(i * 30)
            x_outer = self.center + self.clock_radius * 0.9 * math.sin(angle)
            y_outer = self.center - self.clock_radius * 0.9 * math.cos(angle)
            x_inner = self.center + self.clock_radius * 0.75 * math.sin(angle)
            y_inner = self.center - self.clock_radius * 0.75 * math.cos(angle)
            self.canvas.create_line(x_inner, y_inner, x_outer, y_outer, fill="gray", width=2) # 刻度

    def draw_hand(self, angle_deg, length, width, color):
        angle_rad = math.radians(angle_deg)
        x = self.center + length * math.sin(angle_rad)
        y = self.center - length * math.cos(angle_rad)
        self.canvas.create_line(self.center, self.center, x, y, fill=color, width=width)

    def update_clock(self):
        self.draw_clock_face()

        t = time.localtime()
        second = t.tm_sec
        minute = t.tm_min + second / 60
        hour = t.tm_hour % 12 + minute / 60

        self.draw_hand(hour * 30, self.clock_radius * 0.5, 6, "blue")   # 時針
        self.draw_hand(minute * 6, self.clock_radius * 0.7, 4, "lightblue")  # 分針
        self.draw_hand(second * 6, self.clock_radius * 0.9, 2, "red")    # 秒針

        self.root.after(1000, self.update_clock)

    # 移動位置
    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def do_move(self, event):
        x = event.x_root - self._x
        y = event.y_root - self._y
        self.root.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()
