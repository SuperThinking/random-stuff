from pdf2image import convert_from_path  # https://github.com/Belval/pdf2image

PATH_TO_PDF = "./pdfs/"  # Relative/Absolute path to pdf dir. File will be searched in this dir eg. ./pdfs/xyz.pdf, ./pdfs/abc.pdf

def convert(item):
    path = PATH_TO_PDF + item
    n = item.split(".pdf")[0]
    images = convert_from_path(path)

    for i in range(len(images)):
        images[i].save(f"{n}_page{str(i)}.jpg", 'JPEG')  # Files are saved in the current dir with page formatting eg xyz_page1.jpg, xyz_page2.jpg etc

pdfs = ["xyz.pdf", "abc.pdf"]

for pdf in pdfs:
    print(pdf)
    convert(pdf)
