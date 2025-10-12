# 代码生成时间: 2025-10-12 21:39:49
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
import cv2
import numpy as np
import os
import glob

# 函数：加载人脸数据集
def load_dataset(dataset_path):
    dataset = []
    labels = []
    for label in os.listdir(dataset_path):
        path = os.path.join(dataset_path, label)
        for image in glob.glob(os.path.join(path, "*.jpg")):
            image_array = cv2.imread(image)
            image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
            image_array = cv2.resize(image_array, (100, 100))
            dataset.append(image_array.flatten())
            labels.append(int(label))
    return np.array(dataset), np.array(labels)

# 函数：训练人脸识别模型
def train_model(X_train, y_train):
    try:
        # 数据标准化
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train.reshape(-1, 100 * 100))
        
        # 降维
        pca = PCA(n_components=100)
        X_train_pca = pca.fit_transform(X_train)
        
        # 训练支持向量机模型
        model = SVC(kernel='linear')
        model.fit(X_train_pca, y_train)
        return model, pca
    except Exception as e:
        print(f"Error training model: {e}")

# 函数：评估模型性能
def evaluate_model(model, pca, X_test, y_test):
    try:
        # 数据标准化
        X_test = StandardScaler().fit_transform(X_test.reshape(-1, 100 * 100))
        
        # 降维
        X_test_pca = pca.transform(X_test)
        
        # 预测测试集
        y_pred = model.predict(X_test_pca)
        
        # 计算准确率
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model accuracy: {accuracy:.2f}")
    except Exception as e:
        print(f"Error evaluating model: {e}")

# 主程序
if __name__ == "__main__":
    dataset_path = "face_dataset"
    dataset, labels = load_dataset(dataset_path)
    X_train, X_test, y_train, y_test = train_test_split(dataset, labels, test_size=0.2, random_state=42)
    model, pca = train_model(X_train, y_train)
    evaluate_model(model, pca, X_test, y_test)
