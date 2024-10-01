import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm

# 設定字型
font_path = 'C:/Windows/Fonts/YuGothB.ttc'  # 調整為您的字型路徑
plt.rcParams['font.family'] = fm.FontProperties(fname=font_path).get_name()

# 定義任務數據
tasks = {
    '任務名稱': [
        '研擬計畫', 
        '任務分配', 
        '取得硬體', 
        '程式開發', 
        '安裝硬體', 
        '程式測試', 
        '撰寫使用手冊', 
        '轉換檔案', 
        '系統測試', 
        '使用者訓練', 
        '使用者測試'
    ],
    '開始時間': [0, 1, 1, 5, 18, 75, 28, 28, 105, 53, 130],
    '結束時間': [1, 5, 18, 75, 28, 105, 53, 48, 130, 73, 155]
}

# 創建 DataFrame
df = pd.DataFrame(tasks)
df['持續時間'] = df['結束時間'] - df['開始時間']

# 繪製甘特圖
plt.figure(figsize=(10, 6))
plt.barh(df['任務名稱'], df['持續時間'], left=df['開始時間'], color='skyblue')
plt.xlabel('時間 (天)')
plt.ylabel('任務名稱')
plt.title('專案甘特圖')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.xticks(range(0, 160, 10))  # 調整 X 軸刻度
plt.yticks()  # 調整 Y 軸刻度

# 反轉 Y 軸
plt.gca().invert_yaxis()

plt.show()
