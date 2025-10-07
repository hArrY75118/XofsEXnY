# 代码生成时间: 2025-10-07 21:33:51
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
import numpy as np

"""
商品推荐引擎
使用Pandas和sklearn框架实现
"""

class ProductRecommendationEngine:
    def __init__(self, data):
        """
        初始化商品推荐引擎
        :param data: 包含商品信息和用户评分的DataFrame
        """
        self.data = data
        self.user_ratings = self._get_user_ratings()
        self.item_similarity = self._calc_item_similarity()

    def _get_user_ratings(self):
        """
        从原始数据中提取用户评分信息
        :return: 用户评分DataFrame
        """
        try:
            user_ratings = self.data[['user_id', 'item_id', 'rating']]
            return user_ratings
        except Exception as e:
            print(f"Error extracting user ratings: {e}")
            return None

    def _calc_item_similarity(self):
        """
        计算商品相似度
        :return: 商品相似度矩阵
        """
        try:
            ratings_matrix = self._build_ratings_matrix()
            item_similarity = cosine_similarity(ratings_matrix)
            return pd.DataFrame(item_similarity, columns=self.data['item_id'].unique(), index=self.data['item_id'].unique())
        except Exception as e:
            print(f"Error calculating item similarity: {e}")
            return None

    def _build_ratings_matrix(self):
        """
        构建评分矩阵
        :return: 评分矩阵
        """
        try:
            user_ratings = self.user_ratings.pivot_table(index='user_id', columns='item_id', values='rating')
            user_ratings = user_ratings.fillna(0)
            return user_ratings
        except Exception as e:
            print(f"Error building ratings matrix: {e}")
            return None

    def get_recommendations(self, user_id, num_recommendations=5):
        """
        获取商品推荐
        :param user_id: 用户ID
        :param num_recommendations: 推荐数量
        :return: 推荐商品列表
        """
        try:
            user_ratings = self.user_ratings[self.user_ratings['user_id'] == user_id]
            liked_items = list(user_ratings['item_id'])
            
            # 使用余弦相似度找到相似商品
            similar_items = self.item_similarity.loc[liked_items].mean().sort_values(ascending=False).head(num_recommendations)
            recommended_items = list(similar_items.index)
            
            return recommended_items
        except Exception as e:
            print(f"Error getting recommendations: {e}")
            return []

# 示例用法
if __name__ == '__main__':
    # 读取数据
    data = pd.read_csv('ratings.csv')
    
    # 初始化商品推荐引擎
    engine = ProductRecommendationEngine(data)
    
    # 获取推荐商品
    user_id = 1
    recommendations = engine.get_recommendations(user_id)
    print(f"Recommended items for user {user_id}: {recommendations}")