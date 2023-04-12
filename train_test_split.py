import os
import random
import shutil

data_dir = './data' # 数据集目录
split_dir = './data_split' # 分割后的数据集目录
split_ratio = 0.8 # 训练集和测试集的比例

for class_name in os.listdir(data_dir):
    class_dir = os.path.join(data_dir, class_name)
    if not os.path.isdir(class_dir):
        continue # 忽略非文件夹类型的文件

    # 获取该类别下所有的图片文件名
    image_filenames = os.listdir(class_dir)
    num_images = len(image_filenames)
    if num_images == 0:
        continue # 忽略没有图片的文件夹

    # 将图片文件名随机打乱
    random.shuffle(image_filenames)

    # 将前 split_ratio 比例的图片放入 train 文件夹，剩余的图片放入 test 文件夹
    split_index = int(split_ratio * num_images)
    train_filenames = image_filenames[:split_index]
    test_filenames = image_filenames[split_index:]

    # 创建该类别在 train 和 test 文件夹下的子文件夹
    train_class_dir = os.path.join(split_dir, 'train', class_name)
    test_class_dir = os.path.join(split_dir, 'test', class_name)
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(test_class_dir, exist_ok=True)

    # 将图片复制到对应的子文件夹中
    for filename in train_filenames:
        src_path = os.path.join(class_dir, filename)
        dst_path = os.path.join(train_class_dir, filename)
        if os.path.isfile(src_path):
            shutil.copyfile(src_path, dst_path)
    for filename in test_filenames:
        src_path = os.path.join(class_dir, filename)
        dst_path = os.path.join(test_class_dir, filename)
        if os.path.isfile(src_path):
            shutil.copyfile(src_path, dst_path)