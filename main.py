import copy_img as package

if __name__ == '__main__':
    #初始化配置文件
    initConfig = package.copy_init.InitConfig()
    initConfig.initConfigTxt()

    #这样就不会关闭
    while(True):
        # 输入提示
        userInput = package.input_info.UserInput()
        userInput.setImgName()
        tag = userInput.needOverwriter() #状态判断

        #需要覆写
        if (tag == 1 or tag == 2):
            # 图片操作
            imgOperator = package.img_reader.ImgOperator()
            imgOperator.read()
            imgOperator.copy2Target()
        if(tag == 0):
            print("取消拷贝")