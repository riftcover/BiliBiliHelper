# BiliBiliHelper Python Version
# Copy right (c) 2019 TheWanderingCoel
# 此代码没有任何实际用途,只是想表达下我对制作这个项目和人生的感慨
# 如果想要启动时没有这些句子,请在Conf中将对应项设置到False
# 感谢我的朋友,感谢你们陪伴着我,我爱你们!

import random

class Sentence():
    def get_sentence(self):
        sentence = [
            "生而为人，我很抱歉。",
            "理想很丰满，现实很骨感。",
            "愿我惦记的人岁岁平安，即使生生不见。",
            "曾经以为，伤心是会流很多眼泪的；原来真正的伤心，是流不出一滴眼泪。",
            "该笑的时候没有快乐，该哭泣的时候没有眼泪，该相信的时候没有诺言。",
            "孤单是一个人的狂欢，狂欢是一群人的孤单。",
            "浮华褪尽，人比烟花寂寞。",
            "如果我现在的存在，阻碍了你的生活，那么我消失在这灯光之下。",
            "没有人值得你流泪，值得让你这么做的人不会让你哭泣。",
            "人的烦恼就12个字：放不下，想不开，看不透，忘不了。",
            "如果心凉只需一瞬间，暖一颗心要多少年。",
            "无论这个世界对你怎样，都请你一如既往的努力、勇敢、充满希望。",
            "痛过之后就不会觉得痛了，有的只会是一颗冷漠的心。",
            "我每天都在笑，但过得好不好只有自己才知道。"
        ]
        return random.choice(sentence)