# Python
## 记录
### pyinstaller
在pyinstaller打包过程中，使用命令：
    python pyinstaller-script.py -F -w -i YinYang.ico BaGua.py LiuShiSiGua.py OutToLableFrame.py SanJingGua.py SearchForAnswer.py tooltips.py YueRi.py
将.py的python文件打包成exe，而需要包括的文件用如下方法（懒得打字直接copy了...）：
When you use pyinstaller, it outputs a .spec file which is a configuration file. If you wanted to build your program again using the same options, you can just use 'pyinstaller myprogram.spec' instead of 'pyinstaller myprogram.py'
So open up the spec file in a text editor, and put your images in the 'datas' list like this.
    datas=[('my_image1.gif', ''),
       ('my_image2.gif', ''),
       ('my_image3.gif', ''),
       ('my_image4.gif', '')],
During the execution of a onefile program created with pyinstaller the data files are unpacked to a temp directory. So to access your img files from within your program use a function like this.
    def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    (return os.path.join(base_path, relative_path)
Now build your program using your edited spec file. 'pyinstaller myProgram.spec'