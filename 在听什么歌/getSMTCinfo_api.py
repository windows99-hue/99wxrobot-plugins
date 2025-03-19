import subprocess
import os

path = os.path.abspath("plugin/getSMTCinfo.plugin")

def getSMTC():

    # 运行命令并捕获输出
    result = subprocess.run(["python", path], capture_output=True, text=True)

    # 获取标准输出
    output = result.stdout
    #print("Output:", output)

    return output

def main(last_msg):
    # 修正条件判断逻辑
    if "什么" in last_msg and "歌" in last_msg:
        return getSMTC()  # 调用获取媒体信息的函数

if __name__ == "__main__":
    main("什么歌")