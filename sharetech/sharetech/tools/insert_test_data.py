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
from abc import ABC, abstractmethod

class BaseTestDataClass(ABC):
    @abstractmethod
    def create(self):
        pass

# テストデータ作成用クラス
class CategoryTestData(BaseTestDataClass):
    base_category_name = "テスト"
    category_obj_list = []
    def __init__(self, count):
        self.create_count = count

    def create(self):
        for i in range(self.create_count):
            category_obj = CategoryMst(
                category_name= self.base_category_name+str(i),
                )
            category_obj_list.append(category_obj)
        
        CategoryMst.bulk_crete(category_obj_list)