"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：周科志
日期：2021.11.29
"""
import random
def name_to_number(name):
 """
 将游戏对象对应到不同的整数
 """
 if name=="石头":
     return 0
 if name=="史波克":
     return 1
 if name =="纸":
     return 2
 if name =="蜥蜴":
     return 3
 if name =="剪刀":
     return 4
 else:
     print("Error:NoCorrectName")
def number_to_name(comp_number):
    """
    将整数(0,1,2,3,or4)对应到游戏的不同对象
    """
    if comp_number==0:
        return "石头"
    elif comp_number==1:
        return "史波克"
    elif comp_number ==2:
        return "纸"
    elif comp_number ==3:
        return "蜥蜴"
    elif comp_number ==4:
        return "剪刀"
def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    print("-------------")
    print("您的选择为:%s"%player_choice)
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randint(0,4)
    computer_result=number_to_name(comp_number)
    print("计算机的选择为:%s"%computer_result)
    numbers=player_choice_number-comp_number
    if numbers==1 or numbers==2 or numbers==-3 or numbers==-4:
        print("您赢了")
    elif numbers==0:
        print("您和计算机出的一样呢！")
    else:
        print("机器赢了!")
"""
由"剪刀裁剪纸；纸包裹石头；石头砸碎剪刀；石头砸死蜥蜴；蜥蜴毒死史波克；史波克打碎剪刀；剪刀腰斩蜥蜴；蜥蜴吃掉布；纸反驳史波克；史波克蒸发石头"得
"""
print("欢迎使用RPSLS游戏")
print("--------------")
print("请输入您的选择：")
player_choice=input()
rpsls(player_choice)






