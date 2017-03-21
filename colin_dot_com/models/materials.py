
def get_options_as_array():
    array = []
    for m in Materials.OPTIONS:
        array.append({'value':m[0],'text':m[1]})
    return array


def get_display(key):
    d = dict(Materials.OPTIONS)
    return d[key]


class Materials:
    OPTIONS = (
        ("WOD", "Wood"),
        ("MTL", "Metal"),
        ("GLA", "Glass"),
        ("PRT", "Print"),
        ("CER", "Ceramic"),
        ("TEX", "Textile"),
        ("ADV", "Advanced Manufacturing"),
        ("OTH", "Other")
    )



