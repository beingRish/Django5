from django.shortcuts import render
from .models import QRCode
import qrcode
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
from pathlib import Path
from PIL import Image
import numpy as np
import cv2

def generate_qr(request):
    qr_image_url = None
    if request.method == 'POST':
        mobile_number = request.POST.get('mobile_number')
        data = request.POST.get('qr_data')

        # Validate the mobile number
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request, 'scanner/generate.html', {'error': 'Invalid mobile number'})
        
        # Generate the QR code image with data and mobile number
        qr_content = f"{data}|{mobile_number}"
        qr = qrcode.make(qr_content)
        qr_image_io = BytesIO() #Create a ByteIO stream
        qr.save(qr_image_io, format='PNG')  # Save the QR code image to qr_image_io
        qr_image_io.seek(0) # Reset the position of the stream

        # Define the storage location for the QR code images
        qr_storage_path = settings.MEDIA_ROOT / 'qr_codes'
        fs = FileSystemStorage(location=qr_storage_path, base_url='/media/qr_codes/')
        filename = f"{data}_{mobile_number}.png"
        qr_image_content = ContentFile(qr_image_io.read(),name=filename)
        filepath = fs.save(filename, qr_image_content)
        qr_image_url = fs.url(filename)

        # Save the QR code data and mobile number in the database
        QRCode.objects.create(data=data, mobile_number=mobile_number)

    return render(request, 'scanner/generate.html', {'qr_image_url': qr_image_url})

def scan_qr(request):
    result = None
    if request.method == 'POST' and request.FILES.get('qr_image'):
        mobile_number = request.POST.get('mobile_number')
        qr_image = request.FILES['qr_image']

        # Validate mobile number
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request, 'scanner/scan.html', {'error': 'Invalid mobile number'})

        try:
            # Read image as OpenCV format
            image_bytes = qr_image.read()
            np_arr = np.frombuffer(image_bytes, np.uint8)
            image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            # Decode QR code using OpenCV
            detector = cv2.QRCodeDetector()
            data, points, _ = detector.detectAndDecode(image)

            if data:
                qr_data, qr_mobile_number = data.strip().split('|')

                qr_entry = QRCode.objects.filter(data=qr_data, mobile_number=qr_mobile_number).first()

                if qr_entry and qr_mobile_number == mobile_number:
                    result = "Scan Success: Valid QR Code for the provided mobile number"
                    qr_entry.delete()

                    # Delete the original QR image file
                    qr_image_path = Path(settings.MEDIA_ROOT) / 'qr_codes' / f"{qr_data}_{qr_mobile_number}.png"
                    if qr_image_path.exists():
                        qr_image_path.unlink()

                else:
                    result = "Scan Failed: Invalid QR Code or mobile number mismatch"
            else:
                result = "No QR Code detected in the image."

        except Exception as e:
            result = f"Error processing the image: {str(e)}"

    return render(request, 'scanner/scan.html', {'result': result})