import fitz


def image_parser(file, numOfPages):
    pdf = fitz.open(stream=file, filetype="pdf")
    for page in range(numOfPages):
        image_list = pdf.get_page_images(page)
        print(len(image_list))
        for image in image_list:
            xref = image[0]
            pix = fitz.Pixmap(pdf, xref)
            pix.save(f'{page}.png')
            pix = None
