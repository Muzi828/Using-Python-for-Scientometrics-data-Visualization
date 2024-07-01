# -*- coding: utf-8 -*-
# @Author: xianli
# @Date:   2023-10-11 21:28:57
# @Last Modified by:   xianli
# @Last Modified time: 2023-10-11 21:50:46


#将密码保存到keyring中
api_key = 'xxx'



# 导入openai库
import openai 
import keyring 

# 设置openai库的API密钥
openai.api_key = keyring.get_password('gpt-4','api-key') 

# 定义一个名为generate_gpt的函数，该函数接受一个名为content的参数，该参数是要发送给GPT-3.5模型的内容
def generate_gpt(content): 
    # 创建一个ChatCompletion对象，并设置模型、消息、最大令牌数、生成数量、停止条件和温度等参数
    completion = openai.ChatCompletion.create(
        model="gpt-4",  # 指定使用的模型为gpt-4
        messages=[{"role": 'user', "content": content}],  # 设置消息内容和角色
        max_tokens=100,  # 设置最大令牌数为100
        n=1,  # 设置生成的选项数量为1
        stop=None,  # 不设置停止条件
        temperature=0.5,  # 设置温度为0.5，以控制文本生成的随机性
    ) 

    # 获取模型的响应，并从中提取消息内容
    message = completion.choices[0].message.content
    # 打印消息内容
    return print(message)

# 调用generate_gpt函数，并传递一个简单的问候消息"你好"
generate_gpt("你好")