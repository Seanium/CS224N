# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

def main():
    accuracy = 0.0

    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    # 读取开发集数据
    dev_path = "birth_places_dev.tsv"
    
    # 创建全是"London"的预测列表
    with open(dev_path, encoding='utf-8') as f:
        lines = f.readlines()
        predictions = ["London"] * len(lines)
    
    # 计算准确率
    total, correct = utils.evaluate_places(dev_path, predictions)
    accuracy = (correct / total) * 100.0 if total > 0 else 0.0
    
    ### END YOUR CODE ###

    return accuracy

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
