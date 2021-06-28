# OpenCV
## opencv_pratice1
* Use DLib、Knn、Mog2
* DLib
> Dlib 使用的人臉偵測演算法是以方向梯度直方圖 Histogram of Oriented Gradients（HOG）的特徵加上線性分類器（linear classifier）、影像金字塔（image pyramid）與滑動窗格（sliding window）來實作的
* Knn
> k是一個使用者定義的常數。一個沒有類別標籤的向量（查詢或測試點）將被歸類為最接近該點的k個樣本點中最頻繁使用的一類。換句話說就是找出和新數據附近的K個鄰居（資料），這些鄰居是哪一類（標籤）的它就是哪一類。另外Knn方法主要靠周圍有限的鄰近的樣本，而不是靠判別類域的方法來確定所屬類別的，因此對於類域的交叉或重疊較多的待分樣本集來說，Knn方法較其他方法更為適合。


* MOG2 : 高斯混合模型分離演算法,是 MOG 的改進演算法 Geometric Multigid
> MOG2 的特點是它為每一個圖元選擇一個合適數量的高斯分佈。它能更好地適應光照不同等各種場景。 在此需要創建一個背景物件，但可以選擇是否檢測陰影。如果 detectShadows = True（預設值），它就會檢測並將影子標記出來，但這樣做將會降低處理速度。影子會被標記為灰色。

> 主要通過影片中的背景進行建模，實現背景消除，生成mask圖像，通過對mask二值圖像分析實現對前景活動物件的區域的提取，整個步驟如下： 
> * 初始化背景建模物件 GMM 
> * 讀取影片每一幀 
> * 使用背景建模消除生成 mask 
> * 對 mask 進行輪廓分析提取 ROI 
> * 繪製 ROI 對象

* 比較 Mog, Mog2, Knn, GMG
  
|method | 說明                                | 語法                    |
|-------|-------------------------------------|------------------------|
|MOG    | 基於混合高斯進行背景建模               |BackgroundSubtractorMOG|
|MOG2   | 基於混合高斯進行背景建模，MOG的升級版本 |BackgroundSubtractorMOG2|
|KNN    | 基於K最近鄰進行背景建模                |BackgroundSubtractorKNN|
|GMG    | 基於畫素顏色進行背景建模               |BackgroundSubtractorGMG|
