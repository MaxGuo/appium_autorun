#coding=utf-8
_author_ = "Maoge"

class Action(object):
    #初始化
    def __init__(self, se_driver: object) -> object:
        self.driver = se_driver

    #重写元素定位的方法
    def find_element(self,loc):
        try:
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print("未找到%s"%(self,loc))
