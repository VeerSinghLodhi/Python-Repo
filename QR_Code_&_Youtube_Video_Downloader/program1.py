
import segno
qrcode=segno.make_qr("Veer Singh Lodhi")
qrcode.save('C:\\Users\\Veersingh Lodhi\\Documents\\Qr_Code_Session\\veer.png',
            scale=5,
            light='lightblue',
            dark='darkblue',
            data_dark='green',
            data_light='lightblue')
print("Saved")
