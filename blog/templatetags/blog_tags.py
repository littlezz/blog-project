from django.template import Library
from markdown2 import markdown
from bleach import clean
__author__ = 'zz'

register = Library()

# copy from mezzanine
ALLOW_TAGS = ("a", "abbr", "acronym", "address", "area", "article", "aside",
        "b", "bdo", "big", "blockquote", "br", "button", "caption", "center",
        "cite", "code", "col", "colgroup", "dd", "del", "dfn", "dir", "div",
        "dl", "dt", "em", "fieldset", "figure", "font", "footer", "form",
        "h1", "h2", "h3", "h4", "h5", "h6", "header", "hr", "i", "img",
        "input", "ins", "kbd", "label", "legend", "li", "map", "menu",
        "nav", "ol", "optgroup", "option", "p", "pre", "q", "s", "samp",
        "section", "select", "small", "span", "strike", "strong",
        "sub", "sup", "table", "tbody", "td", "textarea",
        "tfoot", "th", "thead", "tr", "tt", "u", "ul", "var", "wbr")

ALLOW_ATTRS = ("abbr", "accept", "accept-charset", "accesskey", "action",
        "align", "alt", "axis", "border", "cellpadding", "cellspacing",
        "char", "charoff", "charset", "checked", "cite", "class", "clear",
        "cols", "colspan", "color", "compact", "coords", "datetime", "dir",
        "disabled", "enctype", "for", "frame", "headers", "height", "href",
        "hreflang", "hspace", "id", "ismap", "label", "lang", "longdesc",
        "maxlength", "media", "method", "multiple", "name", "nohref",
        "noshade", "nowrap", "prompt", "readonly", "rel", "rev", "rows",
        "rowspan", "rules", "scope", "selected", "shape", "size", "span",
        "src", "start", "style", "summary", "tabindex", "target", "title",
        "type", "usemap", "valign", "value", "vspace", "width", "xml:lang")


ALLOW_STYLES = ("margin-top", "margin-bottom", "margin-left", "margin-right",
        "float", "vertical-align", "border", "margin")

HTML_ClASSES = {
        'img': 'img-responsive center-block',
}

@register.filter
def markdown_render(value):
    extras = {
            'fenced-code-blocks': True,
            'html-classes': HTML_ClASSES,
    }
    return clean(markdown(value, extras=extras),
                 tags=ALLOW_TAGS, attributes=ALLOW_ATTRS, styles=ALLOW_STYLES)


