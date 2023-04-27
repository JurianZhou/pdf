# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import fitz,os
from os.path import abspath, dirname
import datetime
from pdfrw import  PdfWriter, PdfReader


if __name__ == '__main__':

    current_path = abspath(dirname(__file__))  # 获取当前目录

    entries = os.listdir('pdf')
    writer = PdfWriter() #合并器

    for entry in entries:

        filename = os.path.join(current_path, 'pdf', entry)
        #namet=filename[-3:]
        if filename[-3:] != 'pdf': continue
        pdfsplit1 = os.path.splitext(entry) # 获取扩展名
        pdfname1 = pdfsplit1[0]  # 获取不带扩展名的文件名

        filenameafter = os.path.join(current_path, 'pdf', pdfname1 +'after.pdf')
    # 这里需要改为你自己的pdf文件所在
        if pdfsplit1[0][0:3] != 'ppt':        #合并所有前三个字符不为ppt的文档
            doc = fitz.open(filename)

            for page in doc:  # 获取每一页的图片列表（每一页pdf可能有多个图片）

                imageList = page.get_images()
                if len(imageList) == 0:
                    continue
                rect = page.get_image_rects(imageList[0])
                if (rect[0].x0 < 0.1) & (rect[0].y0 <= 0.1):
                    doc._deleteObject(imageList[0][0])

            doc.save(filenameafter)

            pages = PdfReader(filenameafter).pages
            writer.addpages(pages)
            #file_merger.append(filenameafter)

            doc.close()

    today = datetime.date.today()
    date = str(today)
    writer.write(os.path.join(current_path, 'pdf', 'ppt'+ date[5:]+'.pdf')) #命名为ppt0427(当日日期)

    print("完成啦！！！")


