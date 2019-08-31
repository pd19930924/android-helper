import copy_img as package

class UserInput:

    # 设置图片名称
    def setImgName(self):
        name = ""
        while (name == ""):
            name = input("请输入图片名称:")
            package.imgName = name + package.imgSuffix
            if (name == ""):
                print("图片名称不能为空")

    # 打印提示信息
    def printAlertInfo(self, fileName):
        print(fileName + "中包含同名文件")

    # 在目标文件中查找是否存在同名图片资源
    def __searchImgNameInTargetFiles__(self):
        imgOperator = package.img_reader.ImgOperator()

        result = False
        if (imgOperator.hasImgNameInTarget(package.imgName, package.hdpi)):
            result = True
            self.printAlertInfo("hdpi")
        if (imgOperator.hasImgNameInTarget(package.imgName, package.mdpi)):
            result = True
            self.printAlertInfo("mdpi")
        if (imgOperator.hasImgNameInTarget(package.imgName, package.xhdpi)):
            result = True
            self.printAlertInfo("xhdpi")
        if (imgOperator.hasImgNameInTarget(package.imgName, package.xxhdpi)):
            result = True
            self.printAlertInfo("xxhdpi")
        if (imgOperator.hasImgNameInTarget(package.imgName, package.xxxhdpi)):
            result = True
            self.printAlertInfo("xxxhdpi")
        return result

    #1,2,3表示
    def needOverwriter(self):
        if(self.__searchImgNameInTargetFiles__() == False):
            return 2
        overwriteAlert = ""
        while (overwriteAlert != "y" and overwriteAlert != "n"):
            overwriteAlert = input("是否覆盖这些图片?(y/n)")
            if (overwriteAlert != "y" and overwriteAlert != "n"):
                print("请输入y或n")
        if(overwriteAlert == "y"): return 1
        if(overwriteAlert == "n"): return 0