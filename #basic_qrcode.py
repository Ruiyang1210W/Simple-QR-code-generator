#basic_qrcode.py
import qrcode
import os
#Save directory here
save_directory = r"C:\Users\wangr\OneDrive\Desktop\qr code"

def generate_qr_code(link, file_name = "CSSA3_qr_code.png", save_path = save_directory):
    qr = qrcode.QRCode(
        version = 1, #Size of the QR code
        box_size=10,   #Size of each box in the QR code grid
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code instance, can DIY your color
    img = qr.make_image(fill='black', back_color='white')
    
    if save_path:
        # Create the directory if it doesn't exist
        os.makedirs(save_path, exist_ok=True)
        file_name = os.path.join(save_path, file_name)

    img.save(file_name) #save image
    print(f"QR code saved as {file_name}")

#put your url here
link = "https://docs.google.com/forms/d/1dJwHM-a2zqdL3zTOdY80RqGfk4Xp41RFt1rOyBAKrhM/viewform?edit_requested=true"

generate_qr_code(link)
