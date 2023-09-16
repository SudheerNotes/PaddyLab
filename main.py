import sys, os
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import requests
import base64


base_dir = os.path.dirname(__file__)

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("MainGUI.ui",self)

        self.filename = ""
        icon_file = QtGui.QPixmap(os.path.join(base_dir,"icons","paddy.svg")).scaled(110,110)
        self.lbl_main_icon.setPixmap(icon_file)
        self.btn_browse.clicked.connect(self.file_dailog)
        self.btn_clear.clicked.connect(self.clear_canvas)
        self.btn_predict.clicked.connect(self.prediction)
        

    def file_dailog(self):
        self.clear_canvas()
        filename,_ = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select your Image file',
            directory=os.getcwd(),
            filter ="jpg/png(*.jpg *.jpeg *.png)")
        pixmap = QtGui.QPixmap(filename).scaled(450,280) 
        self.lbl_img_view.setPixmap(pixmap)
        self.filename = filename 

    # image_to_bse64 function credit gradio_client
    def image_to_bse64(self,file_path):
        with open (file_path,'rb') as img_file:
            img = base64.b64encode(img_file.read())
            base64_str = str(img, "utf-8")
        return ("data:" + "" + ";base64,"+ base64_str)

    def prediction(self):
        if not self.filename == "":
            try:
                API ='https://sudheernotes-paddylab1.hf.space/api/predict'
                r = requests.post(API,json={"data":[self.image_to_bse64(self.filename)]},timeout=15)
                output = r.json()
                for items in output['data']:
                    for j in items['confidences']:
                        prediction = j['label']
                        probability = j['confidence']

                pred_txt = f"Prediction ==> {prediction} \n Confidence level ==> {format(float(probability)*100,'.4f')}"
                self.lbl_message.setText(pred_txt)

            except requests.exceptions.Timeout:
                self.lbl_message.setText("[Timed out] Server not responding \n please try after sometime")
                
            except requests.exceptions.ConnectionError:
                self.lbl_message.setText("Please check your internet connection..")

        else:
            self.lbl_message.setText("Please select an Image")
        
    def clear_canvas(self):
        self.lbl_img_view.clear()
        self.lbl_message.clear()
        self.filename = ""

# Main
app = QApplication(sys.argv)
widget = WelcomeScreen()
widget.setFixedHeight(630)
widget.setFixedWidth(950)
widget.setWindowTitle(" ")
widget.setWindowIcon(QtGui.QIcon(os.path.join(base_dir,"icons","paddy.svg")))
widget.show()

try:
    sys.exit(app.exec_())

except:
    print("exiting") 