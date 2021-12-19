from .user import CustomUser, CustomUserManager 
from .position_mst import PositionMst
from .occupation_mst import OccupationMst
from .industry_mst import IndustryMst
from .consult_window import ConsultWindow
from .category_mst import CategoryMst
from .category_consult_window_mapping import CategoryConsultWindowMapping
from .consult_apply import ConsultApply
from .user_specialize import UserSpecialize

"""
Modelファイル分割のためサブディレクトリを作成
makemigrationsで認識できるようにするための__init__.pyファイル
分割した各モデルのimport必須
"""