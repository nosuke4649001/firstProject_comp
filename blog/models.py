from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
# Create your models here.

class BlogPost(models.Model):
    '''モデルクラス
    '''
    # カテゴリに設定する項目を入れ子のタプルとして定義
    # 最初の要素はモデルが使用する値、2番目の要素は選択メニューに表示する文字列
    CATEGORY = (('Python', 'Python'), ('プログラミング', 'プログラミング'), ('その他', 'その他'))

    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル', # フィールドのタイトル
        max_length=200        # 最大文字数は200
        )
    # 本文用のフィールド
    content = MarkdownxField('本文')
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', # フィールドのタイトル
        auto_now_add=True       # 日時を自動追加
        )
    # カテゴリのフィールド
    category = models.CharField(
        verbose_name='カテゴリ', # フィールドのタイトル
        max_length=50,        # 最大文字数は50
        choices=CATEGORY
        )
    def convert_markdown_to_html(self):
        return markdownify(self.main_text)
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):投稿記事のタイトル
        '''
        return self.title
    
