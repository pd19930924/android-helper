import copy_img as package

class ImgInit:

    # 获取图片的宽度和高度
    def __getImgSize__(self, img):
        return img.width * img.height

    # 依据尺寸，从小到大排序
    def __imgSizeCmp__(self, img1Path, img2Path):
        img1 = package.Image.open(img1Path)
        img2 = package.Image.open(img2Path)
        img1Size = self.__getImgSize__(img1)
        img2Size = self.__getImgSize__(img2)
        if (img1Size < img2Size):
            return -1
        if (img1Size > img2Size):
            return 1
        if (img1Size == img2Size):
            return 0

    def imgSortBySize(self, imgNames):
        imgList = []
        #获取图片资源
        for imgName in imgNames:
            imgList.append(package.iconSourcePath + "//" + imgName)
        #对图片资源进行排序
        imgList.sort(key=package.functools.cmp_to_key(self.__imgSizeCmp__))
        return imgList


#读取图片信息
class ImgOperator:

    imgList = []

    def print(self):
        print(package.imgSuffix)
        print("path =" + package.iconSourcePath)

    #拷贝文件
    def __copySource__(self,sourceImg, targetImg):
        package.shutil.copy2(sourceImg, targetImg)

    def __joinRoot__(self, prex, img):
        return package.os.path.join(prex, img)

    #读取图片信息
    def read(self):
        imgNames = package.os.listdir(package.iconSourcePath)  #获取图片名称
        imgInit = ImgInit()
        self.imgList = imgInit.imgSortBySize(imgNames) #获得排序后的数组

    #图片拷贝过程
    def copy2Target(self):
        imgList = self.imgList
        targetImgName = package.imgName
        #如果恰好是5张，那么就直接把所有图片塞过去
        if(len(imgList) == 5):
            self.__copySource__(imgList[0], self.__joinRoot__(package.mdpi, targetImgName))
            self.__copySource__(imgList[1], self.__joinRoot__(package.hdpi, targetImgName))
            self.__copySource__(imgList[2], self.__joinRoot__(package.xhdpi, targetImgName))
            self.__copySource__(imgList[3], self.__joinRoot__(package.xxhdpi, targetImgName))
            self.__copySource__(imgList[4], self.__joinRoot__(package.xxxhdpi, targetImgName))
        if(len(imgList) == 3):
            self.__copySource__(imgList[0], self.__joinRoot__(package.hdpi, targetImgName))
            self.__copySource__(imgList[1], self.__joinRoot__(package.xhdpi, targetImgName))
            self.__copySource__(imgList[2], self.__joinRoot__(package.xxhdpi, targetImgName))

        print("拷贝完成")

    # 在当前文件中是否存在同名文件
    def hasImgNameInTarget(self, name, path):
        imgNameList = package.os.listdir(path)
        if (imgNameList.__contains__(name)):
            return True
        else:
            return False

