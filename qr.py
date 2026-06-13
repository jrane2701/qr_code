import qrcode

#Data for QR
website_link='https://www.youtube.com/watch?v=Vp6-oqYQd6k&list=PLpNHpn2hLBEWOYokTEZINJE9O5yVqTSh7&index=4'

#Variable to import qrcode library functions
qr=qrcode.QRCode(version=1, box_size=5, border=2)

#Add data in the qr
qr.add_data(website_link)

#Make qr
qr.make()

#To create image 
img = qr.make_image(fill_color = 'black' , back_color='white')
img.save('yt_qr.png')