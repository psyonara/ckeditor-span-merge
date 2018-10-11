from bs4 import BeautifulSoup


def span_scan(span, level=0):
    if span.attrs.get("style") and len(span.attrs.items()) == 1:
        child = span.find("span")
        child_style = ""
        if child:
            child_style = span_scan(child, level+1).strip()
            if not child_style.endswith(";"):
                child_style += ";"

        this_style = span.attrs.get("style").strip()
        if not this_style.endswith(";"):
            this_style += ";"
        if level != 0:
            span.unwrap()

        return this_style + child_style


def ckeditor_span_merge(html_snippet):
    soup = BeautifulSoup(html_snippet, "html.parser")
    for tag in soup.find_all("span", recursive=False):
        all_styles = span_scan(tag)
        tag.attrs['style'] = all_styles

    return str(soup)
