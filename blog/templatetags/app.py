<<<<<<< HEAD
=======
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

>>>>>>> b0254daaf1feb3a7a4673f4c3cbb6ebbd8bfd450
from django import template
from django.utils.safestring import mark_safe
import markdown
from markdownx.utils import markdownify
from markdownx.settings import (
<<<<<<< HEAD
            MARKDOWNX_MARKDOWN_EXTENSIONS,
                MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS
                )
=======
    MARKDOWNX_MARKDOWN_EXTENSIONS,
    MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS
)
>>>>>>> b0254daaf1feb3a7a4673f4c3cbb6ebbd8bfd450
from markdown.extensions import Extension

register = template.Library()


@register.filter
def markdown_to_html(content):
<<<<<<< HEAD
    return mark_safe(markdownify(content))

=======
    """マークダウンをhtmlに変換する。"""
    return mark_safe(markdownify(content))


>>>>>>> b0254daaf1feb3a7a4673f4c3cbb6ebbd8bfd450
class EscapeHtml(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.deregister('html_block')
        md.inlinePatterns.deregister('html')

@register.filter
def markdown_to_html_with_escape(text):
<<<<<<< HEAD
    extensions = MARKDOWNX_MARKDOWN_EXTENSIONS + [EscapeHtml()]
    html = markdown.markdown(text, extensions=extensions, extension_configs=MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS)
    return mark_safe(html)

=======
    """マークダウンをhtmlに変換する。

    生のHTMLやCSS、JavaScript等のコードをエスケープした上で、マークダウンをHTMLに変換します。
    公開しているコメント欄等には、こちらを使ってください。

    """
    extensions = MARKDOWNX_MARKDOWN_EXTENSIONS + [EscapeHtml()]
    html = markdown.markdown(text, extensions=extensions, extension_configs=MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS)
    return mark_safe(html)
>>>>>>> b0254daaf1feb3a7a4673f4c3cbb6ebbd8bfd450
