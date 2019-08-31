import copy_img as package

class InitConfig:

    __configTxtPath__ = "config.txt"
    __iconSource__ = "source_icon"

    # 初始化配置文件
    # 这个是使用一个配置文件来初始化一些信息，目前还在慢慢做
    # 如果返回True，就继续执行
    # 如果返回False, 就不再执行
    def initConfigTxt(self):
        # 创建config配置文件，以后可以在config配置文件中修改某些参数
        if (package.os.path.exists(InitConfig.__configTxtPath__)):
            self.__readConfigTxt__()
        else:
            self.__createConfigTxt__()
            self.__createIconSource__()
            self.__readConfigTxt__()

    #如果不存在config.txt,那么就创建config.txt
    def __createConfigTxt__(self):
        print("初始化配置文件")
        # 不存在config文档的情况下初始化当前文件夹
        configTxt = open(self.__configTxtPath__, "w")
        configTxt.write("icon_format=png\n")  # 当前图片的格式
        configTxt.write("source_path=" + self.__iconSource__ + "\n")  # 当前图片路径
        #目标路径,需要用户填写
        configTxt.write("hdpi=\n")
        configTxt.write("mdpi=\n")
        configTxt.write("xhdpi=\n")
        configTxt.write("xxhdpi=\n")
        configTxt.write("xxxhdpi=\n")
        configTxt.close()

        self.__setTargetPath__()

    #创建资源文件夹
    def __createIconSource__(self):
        if(package.os._exists(self.__iconSource__) == False):
            package.os.makedirs(self.__iconSource__)

    #设置目标文件夹的路径
    def __setTargetPath__(self):
        print("配置文件配置完成")
        #开始输入配置文件信息
        print("您可以按照提示进行文件配置/关闭此窗口，在config.txt文本中进行配置，再运行txt文件")
        print("请在 = 后输入下面文件夹的路径，您可以直接复制导航栏的路径")
        print("在windows下,一个正确路径的格式样例：D:\\android\\test")
        hdpi = input("hdpi=")
        mdpi = input("mdpi=")
        xhdpi = input("xhdpi=")
        xxhdpi = input("xxhdpi=")
        xxxhdpi = input("xxxhdpi=")

        #开始写入文件
        file_data = ""
        config = open(self.__configTxtPath__, "r")
        lines = config.readlines()
        #第一行和第二行默认写入
        file_data += lines.__getitem__(0)
        file_data += lines.__getitem__(1)

        #目标路径
        hdpiPath = self.__joinDpiPath__(lines.__getitem__(2), hdpi)
        mdpiPath = self.__joinDpiPath__(lines.__getitem__(3), mdpi)
        xhdpiPath = self.__joinDpiPath__(lines.__getitem__(4), xhdpi)
        xxhdpiPath = self.__joinDpiPath__(lines.__getitem__(5), xxhdpi)
        xxxhdpiPath = self.__joinDpiPath__(lines.__getitem__(6), xxxhdpi)
        file_data += hdpiPath + mdpiPath + xhdpiPath + xxhdpiPath+ xxxhdpiPath
        config.close()

        # 写入文件夹
        config = open(self.__configTxtPath__, "w")
        config.write(file_data)
        config.close()

    #windows读进来的路径只有一个\，在进行转义时会出现问题，因此需要对路径进行重新解析
    def __dpiPath__(self, dpiPath):
        dividePath = dpiPath.split("\\")
        if(len(dividePath) == 1): return
        finalPath = ""
        for path in dividePath:
            finalPath = package.os.path.join(finalPath, path)
        print(finalPath)

    #合并hdpi的路径
    def __joinDpiPath__(self, str, dpiPath):
        dpiName = str.split("\n")[0]
        targetPath = dpiName + dpiPath + "\n"
        return targetPath

    # 如果配置文件存在，那么每次开始都获取一下配置文件的信息
    def __readConfigTxt__(self):
        configTxt = open(self.__configTxtPath__, "r")
        configContent = configTxt.readlines()
        #读取配置文件信息
        package.imgSuffix = "." + self.__parseData__(configContent[0])  # 获取图片格式
        package.iconSourcePath = self.__parseData__(configContent[1])  # 获取图片路径
        package.hdpi = self.__parseData__(configContent[2])
        package.mdpi = self.__parseData__(configContent[3])
        package.xhdpi = self.__parseData__(configContent[4])
        package.xxhdpi = self.__parseData__(configContent[5])
        package.xxxhdpi = self.__parseData__(configContent[6])
        configTxt.close()

    def __parseData__(self, str):
        res = str.split("=")[1].split("\n")[0]
        return res










