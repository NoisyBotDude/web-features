import pytesseract
from PIL import Image, ImageEnhance

print("To Begin With This Software, You Have To Put The Image In The Image-Test Folder In The Desktop\n"
              "And Put The Name of The Image Below")
n1 = str(input("Name Of The Image: "))

print("Do You Want To\n1. Recognize Text\n2. Convert The Image To PDF")

n3 = int(input())

global img
global img_edit

if n3 == 1:
            print("What File Is It\n1. PNG\n2. JPG\n3. JPEG")
            n2 = int(input())

            # global img
            # global img_edit

            if n2 == 1:
                img = Image.open(f'image-test/{n1}.png')
                enhancer1 = ImageEnhance.Sharpness(img)
                enhancer2 = ImageEnhance.Contrast(img)

                img_edit = enhancer1.enhance(30.0)
                # noinspection PyRedeclaration
                img_edit = enhancer2.enhance(5.25)

                img_edit.save(f'edited{n1}_image.png')
                # img_edit.show()

            elif n2 == 2:
                img = Image.open(f'image-test/{n1}.jpg')
                enhancer1 = ImageEnhance.Sharpness(img)
                enhancer2 = ImageEnhance.Contrast(img)

                img_edit = enhancer1.enhance(30.0)
                # noinspection PyRedeclaration
                img_edit = enhancer2.enhance(5.25)

                img_edit.save(f'edited{n1}_image.jpg')
                # img_edit.show()


            elif n2 == 3:
                img = Image.open(f'image-test/{n1}.jpeg')
                enhancer1 = ImageEnhance.Sharpness(img)
                enhancer2 = ImageEnhance.Contrast(img)

                img_edit = enhancer1.enhance(30.0)
                # noinspection PyRedeclaration
                img_edit = enhancer2.enhance(5.25)

                img_edit.save(f'edited{n1}_image.jpeg')
                # img_edit.show()

            else:
                print("No Such Option Available")
                # speak("No Such Option Available")
            # assigning an image from the source path
            # img = Image.open(f'image-test/{n1}.jpg')
            # img.show()

            # converts the image to result and saves it into result variables
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            results = pytesseract.image_to_string(img_edit)

            with open(f'{n1}.txt', mode='w') as file:
                file.write(results)
                print(f'Your File Is Located At C:\\Users\\ashis\\PycharmProjects\\jarvis\\{n1}.txt')

elif n3 == 2:
            print("What File Is It\n1. PNG\n2. JPG\n3. JPEG")
            n2 = int(input())

            # global img

            if n2 == 1:
                img = Image.open(f'image-test/{n1}.png')

            elif n2 == 2:
                img = Image.open(f'image-test/{n1}.jpg')

            elif n2 == 3:
                img = Image.open(f'image-test/{n1}.jpeg')

            else:
                print("No Such Option Available")

            # img = Image.open('image-test/test-image.jpg')

            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            results = pytesseract.image_to_pdf_or_hocr(img)

            with open(f'{n1}.pdf', mode='w+b') as file:
                file.write(results)
                print(f'Your File Is Located At C:\\Users\\ashis\\PycharmProjects\\jarvis\\{n1}.pdf')