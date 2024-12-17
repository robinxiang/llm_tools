import os
import json

def convert_json_to_txt(directory):
    # 遍历指定目录下的所有文件
    for filename in os.listdir(directory):
        # 只处理 .json 文件
        if filename.endswith('.json'):
            json_path = os.path.join(directory, filename)
            
            # 用于存储合并后的内容
            combined_contents = []

            # 逐行读取 JSON 文件内容
            with open(json_path, 'r', encoding='utf-8') as json_file:
                for line in json_file:
                    try:
                        data = json.loads(line.strip())
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON from line in file: {json_path}")
                        continue

                    # 提取字段内容
                    post_class = data.get('post_class', '')
                    post_title = data.get('post_title', '')
                    post_contentext = data.get('post_contentext', '')

                    # 如果 post_contentext 是一个列表，转换为字符串
                    if isinstance(post_contentext, list):
                        # 将列表元素连接成一个字符串，元素之间用 ',' 分割
                        post_contentext = ','.join(post_contentext)

                    # 替换逗号为换行符
                    post_contentext = post_contentext.replace(',', '\n')

                    # 合并内容
                    combined_content = f"{post_class}\n{post_title}\n{post_contentext}\n"
                    combined_contents.append(combined_content)

            # 设置输出文件路径和名称
            txt_filename = f"{os.path.splitext(filename)[0]}.txt"
            txt_path = os.path.join(directory, txt_filename)

            # 将内容保存为 .txt 文件
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write("\n".join(combined_contents))

            # 输出保存路径和文件名的提示
            print(f"Saved: {txt_path}")

# 指定要处理的目录路径
directory_path = './'

# 调用函数
convert_json_to_txt(directory_path)
