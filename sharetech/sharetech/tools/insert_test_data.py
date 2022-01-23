from PIL import Image
import glob
import os
import sys
import random
import django
from django.utils import timezone

sys.path.append('../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()

from sharetech.models.category_mst import CategoryMst
from sharetech.models.user import CustomUser
from sharetech.models.consult_window import ConsultWindow
from sharetech.models.category_consult_window_mapping import CategoryConsultWindowMapping
from abc import ABC, abstractmethod

class BaseTestDataClass(ABC):
    def __init__(self, count):
        self.create_count = count
        self.obj_list = []

    @abstractmethod
    def create(self):
        pass

# カテゴリテストデータ作成用クラス
class CategoryTestData(BaseTestDataClass):
    # カテゴリ名
    base_category_name = "テスト"

    def __init__(self, count):
        # 作成したいカテゴリ数
        super().__init__(count)

    def create(self):
        for i in range(self.create_count):
            category_obj = CategoryMst(
                category_name= self.base_category_name+str(i),
                )
            self.obj_list.append(category_obj)
        
        CategoryMst.objects.bulk_create(self.obj_list)

# 相談窓口テストデータ作成用クラス
class ConsultWindowTestData(BaseTestDataClass):
    # 相談窓口タイトル
    base_title = 'test'
    # 相談窓口概要
    base_overview = 'it is test'
    # 相談料金
    price = 0
    # timerex url
    scheduler_url = 'https://timerex.test/testtesttest/'
    # 実績
    archivement = '1950~1955年に「共産主義者と平和」を書く。¥n1956~1960年にはハンガリー事件に感銘を受け、「第三世界」の重要性を認識する。¥n'

    def __init__(self, count):
        # 作成したい記事数
        super().__init__(count)
        
    def create(self):
        user_id_list = list(CustomUser.objects.all())
        user_count = len(user_id_list)

        for i in range(self.create_count):
            user_id_index = i % user_count
            consult_window_obj = ConsultWindow(
                expert_user_id = user_id_list[user_id_index],
                consult_window_title = self.base_title + str(i),
                consult_window_overview = self.base_overview + str(i) + '.¥n',
                consult_price = self.price * i,
                scheduler_url = self.scheduler_url,
                archivement = self.archivement,
            )
            self.obj_list.append(consult_window_obj)
        
        ConsultWindow.objects.bulk_create(self.obj_list)

# 相談窓口カテゴリマッピングテストデータ
class ConsultWindowCategoryMappingTestData(BaseTestDataClass):
    def __init__(self, count):
        # 1記事に対してつけたいカテゴリ数
        super().__init__(count)
    
    def create(self):
        window_id_list = list(ConsultWindow.objects.all())
        window_count = len(window_id_list)
        category_id_list = list(CategoryMst.objects.all())
        category_count = len(category_id_list)

        for i in range(window_count):
            # カテゴリ数<記事数となっている前提
            base_category_id_index = i % (category_count - 2)
            category_mapping_obj = [
                CategoryConsultWindowMapping(
                    consult_window_id=window_id_list[i], 
                    category_id=category_id_list[base_category_id_index + j],
                    ) for j in range(self.create_count)
                ]
            self.obj_list.extend(category_mapping_obj)

        CategoryConsultWindowMapping.objects.bulk_create(self.obj_list)
