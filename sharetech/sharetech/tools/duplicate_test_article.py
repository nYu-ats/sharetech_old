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

from sharetech.models import Article, Chapter, User


class DuplicateTestArticle:

    original_img_dir = './tools/original_img/'
    original_txt_dir = './tools/original_txt/'
    original_title_dir = './tools/original_title/'
    copied_folter_path = '../../sharetech/'
    txt_extension = '.txt'
    img_extension = '.png'

    def __init__(self, duplicate_count):
        self.duplicate_count = int(duplicate_count)
        self.target_article_chapter_dict = {}

        # 処理対象ファイル名抜き出し
        # 重複するファイル名はそもそも登録できないのでそこのチェック不要
        article_img_filename_set = {os.path.splitext(os.path.split(file_name)[1])[0] for file_name in glob.glob(self.original_img_dir + '*')}
        article_txt_filename_set = {os.path.splitext(os.path.split(file_name)[1])[0] for file_name in glob.glob(self.original_txt_dir + '*')}
        target_chapter_set = article_img_filename_set.intersection(article_txt_filename_set)
        pre_target_title_list = [os.path.splitext(os.path.split(file_name)[1])[0] for file_name in glob.glob(self.original_title_dir + '*')]
        pre_target_chapter_list = list(target_chapter_set)
        pre_target_article_list = list({txt.split('_')[0] for txt in pre_target_chapter_list})
        for article_id in pre_target_article_list:
            chapter_id_list = []
            for chapter_id in pre_target_chapter_list:
                if article_id in chapter_id and article_id in pre_target_title_list:
                    chapter_id_list.append(chapter_id)
            
            # 現状特に必要はないので、処理済み要素の削除は行わない
            if len(chapter_id_list) == 3:
                self.target_article_chapter_dict[article_id] = sorted(chapter_id_list)
        
    def execute(self):
        contoributor_id_list = list((User.objects.filter(role_id = 2)))
        for article_id, chapter_id_list in self.target_article_chapter_dict.items():
            target_title = ''
            # try:
                # ファイルのロード
            with open(self.original_title_dir + article_id + self.txt_extension) as f:
                target_title = f.read()

            for _ in range(self.duplicate_count):
                # 記事レコードinsert
                contoributor_index = random.randrange(0, len(contoributor_id_list))
                article = Article(
                    title = target_title,
                    contributor_id = contoributor_id_list[contoributor_index],
                    eyecatch_path = chapter_id_list[0] + self.img_extension,
                )
                article.save()

                article_pk =  list(Article.objects.filter(title = target_title).order_by('-pk'))
                    # try:
                        # 章レコードinsert
                for index, chapter_item in enumerate(chapter_id_list):
                    with open(self.original_txt_dir + chapter_item + self.txt_extension) as f:
                        sentense_txt = f.read()

                    chapter = Chapter(
                        article_id = article_pk[0],
                        chapter_idx = index + 1,
                        img_path = str(article_pk[0].pk).zfill(6)+ '_' + str(index + 1)   + self.img_extension,
                        sentence =sentense_txt,
                    )
                    chapter.save()

                    copied_file_name = str(article_pk[0].pk).zfill(6) + '_' + str(index + 1)  
                            # 配信用フォルダへファイルをコピー
                    target_img = Image.open(duplicate_test_article.original_img_dir + chapter_item + self.img_extension)
                    target_img.save(duplicate_test_article.copied_folter_path + copied_file_name + self.img_extension)

                        # 結果処理(処理完了ファイルの移動)

                    # except Exception as e:
                        # raise e

            # except Exception as e :
                # print(e)
        
if __name__ == '__main__':
    duplicate_test_article = DuplicateTestArticle(sys.argv[1])
    duplicate_test_article.execute()
