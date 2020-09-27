### **開發環境:**  

Python 3.7.5 x64  

IDE: JetBrains PyCharm Community Edition 2020.2.2 x64  

### **額外擴充(需用pip install安裝):**  

- discord.py

### **使用前須知:**  

拿到專案要先自行建立虛擬環境，並安裝package，且確認其他開發環境正確。    

### **資料夾內容:**  

Bot: 內含程式碼及部分資料  

Bot\api: 內含程式庫程式碼  

Bot\cogs: cogs的程式碼，指令和事件都集中於此  

已知常見問題: 監聽on_message會讓同模組的指令失效是正常現象，官方文檔有說明)  

Bot\data: 儲存資料  

Bot\data\statusList: 存放Bot顯示的狀態訊息，會定時切換，可以在程式碼中修改時間  

Bot\data\token: 用來存放登入token 

