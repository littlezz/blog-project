from django.conf import settings
__author__ = 'zz'



# copy from mezzanine ALLOW_XXX
_ALLOW_TAGS = ("a", "abbr", "acronym", "address", "area", "article", "aside",
        "b", "bdo", "big", "blockquote", "br", "button", "caption", "center",
        "cite", "code", "col", "colgroup", "dd", "del", "dfn", "dir", "div",
        "dl", "dt", "em", "fieldset", "figure", "font", "footer", "form",
        "h1", "h2", "h3", "h4", "h5", "h6", "header", "hr", "i", "img",
        "input", "ins", "kbd", "label", "legend", "li", "map", "menu",
        "nav", "ol", "optgroup", "option", "p", "pre", "q", "s", "samp",
        "section", "select", "small", "span", "strike", "strong",
        "sub", "sup", "table", "tbody", "td", "textarea",
        "tfoot", "th", "thead", "tr", "tt", "u", "ul", "var", "wbr")

_ALLOW_ATTRS = ("abbr", "accept", "accept-charset", "accesskey", "action",
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


_ALLOW_STYLES = ("margin-top", "margin-bottom", "margin-left", "margin-right",
        "float", "vertical-align", "border", "margin")





ALLOW_TAGS = getattr(settings, 'ALLOW_TAGS', _ALLOW_TAGS)
ALLOW_ATTRS = getattr(settings, 'ALLOW_ATTRS', _ALLOW_ATTRS)
ALLOW_STYLES = getattr(settings, 'ALLOW_STYLES', _ALLOW_STYLES)

