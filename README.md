# Ecosystem Simulation

這是一個基於 Python 與 Pygame 開發的生態系統模擬器。
在這個虛擬世界中，生物（綿羊與狼）會根據環境互動、覓食、繁殖，並透過**基因演化**機制，篩選出最適合生存的個體。

## 主要特色 (Features)

* **程序化地圖生成**：使用 **Perlin Noise** 生成獨一無二的地形（海洋、沙地、草原）。
* **動態食物鏈**：
    * **牧草**：隨時間生長，供綿羊食用。
    * **綿羊**：尋找牧草，逃離狼群。
    * **狼**：追捕綿羊，維持體力。
* **基因演化系統 (New!)**：
    * 生物會將**速度**、**感知範圍**、**代謝率**等基因遺傳給後代。
    * 子代會發生**基因重組**與**隨機突變**。

## 安裝與需求 (Installation)
請確保您的電腦已安裝 Python 3.x。
1.  **複製專案**
    ```bash
    git clone https://github.com/Babo126/Conway-s-Game-of-Life
    cd Conway-s-Game-of-Life
    ```

2.  **安裝依賴套件**
    ```bash
    pip install -r requirements.txt
    ```
    *(主要依賴：`pygame`, `numpy`, `perlin-noise`)*

## 如何執行 (How to Run)
在專案根目錄下執行以下指令：
```bash
python src/main.py

## 操作說明 (Controls)
- W / A / S / D 或 方向鍵：移動攝影機視角。
- 滑鼠移動：靠近生物可查看詳細基因數值（如速度、感知距離）。
- 關閉視窗：結束程式。

## 演化機制說明
本模擬器模擬了真實的自然選擇：
- 優勝劣汰：跑得太慢的羊會被吃掉；抓不到羊的狼會餓死。
- 繁殖遺傳：存活下來的強者才有機會繁殖，將優秀基因傳給下一代。
- 突變：後代有機率產生突變，可能變得更強（如速度爆發），也可能變弱。
- 觀察重點： 試著放著程式跑一段時間（約 5~10 分鐘），你會發現畫面上的生物開始出現紅色或藍色的光環，這代表該族群已經演化出了特定的優勢性狀。

## 參數調整 (Configuration)
你可以自由調整 src/constants.py 來改變世界規則：
- MUTATION_RATE：調整突變發生的機率。
- MUTATION_SCALE：調整突變的劇烈程度。
- MAP_WIDTH / MAP_HEIGHT：調整地圖大小。
- SHEEP_SPEED / WOLF_SPEED：調整生物基礎數值。

## 專案結構
- src/main.py：程式入口點。
- src/worlds.py：管理世界循環（更新、繪製）。
- src/creatures.py：生物行為、基因遺傳邏輯。
- src/tilemap.py：地圖生成與繪製。
- src/tools.py：Perlin Noise 工具。
- src/constants.py：全域參數設定。
