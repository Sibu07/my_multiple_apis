from flask import Blueprint, jsonify, render_template_string


show_color_blueprint = Blueprint('show_color', __name__)

html_template = '''
    <div style="width: 100px; height: 100px; background-color: {{ color }};"></div>
    <p>Color Code: {{ color }}</p>
'''

@show_color_blueprint.route('/api/show-color/<string:color_code>')
def show_color(color_code):
    color = {
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
    'black': '#000000',
    'white': '#FFFFFF',
    'orange': '#FFA500',
    'purple': '#800080',
    'pink': '#FFC0CB',
    'turquoise': '#40E0D0',
    'magenta': '#FF00FF',
    'lavender': '#E6E6FA',
    'maroon': '#800000',
    'olive': '#808000',
    'teal': '#008080',
    'navy': '#000080',
    'gold': '#FFD700',
    'silver': '#C0C0C0',
    'gray': '#808080',
    'khaki': '#F0E68C',
    'beige': '#F5F5DC',
    'brown': '#A52A2A',
    'coral': '#FF7F50',
    'crimson': '#DC143C',
    'fuchsia': '#FF00FF',
    'indigo': '#4B0082',
    'ivory': '#FFFFF0',
    'lime': '#00FF00',
    'mustard': '#FFDB58',
    'peach': '#FFE5B4',
    'periwinkle': '#CCCCFF',
    'plum': '#DDA0DD',
    'salmon': '#FA8072',
    'tan': '#D2B48C',
    'violet': '#EE82EE',
    'apricot': '#FFB347',
    'baby blue': '#89CFF0',
    'baby pink': '#F4C2C2',
    'baby purple': '#CA9BF7',
    'baby yellow': '#FFFFC2',
    'beet': '#8E354A',
    'brick': '#8C3D3D',
    'bronze': '#CD7F32',
    'bubblegum': '#FFC1CC',
    'burgundy': '#800020',
    'burnt orange': '#CC5500',
    'camel': '#C19A6B',
    'charcoal': '#36454F',
    'cherry': '#DE3163',
    'chocolate': '#D2691E',
    'cinnamon': '#D2691E',
    'copper': '#B87333',
    'cream': '#FFFDD0',
    'crimson red': '#990000',
    'dark blue': '#00008B',
    'dark brown': '#654321',
    'dark green': '#006400',
    'dark gray': '#A9A9A9',
    'dark pink': '#E75480',
    'dark purple': '#4B0082',
    'deep purple': '#7E5E9B',
    'denim': '#1560BD',
    'dusty pink': '#D8BFD8',
    'eggplant': '#614051',
    'emerald': '#50C878',
    'forest green': '#228B22',
    'frost': '#EDE7F6',
    'goldenrod': '#DAA520',
    'grape': '#6F2DA8',
    'grass green': '#7CFC00',
    'grey': '#808080',
    'hot pink': '#FF69B4',
    'hunter green': '#355E3B',
    'mauve': '#E0B0FF',
    'midnight blue': '#191970',
    'mint': '#3EB489',
    'navajo white': '#FFDEAD',
    'neon green': '#39FF14',
    'ochre': '#CC7722',
    'olive drab': '#6B8E23',
    'pale blue': '#AFEEEE',
    'pale green': '#98FB98',
    'pale pink': '#FADADD',
    'pea green': '#8EBA42',
    'pear': '#D1E231',
    'pearl': '#F0EAD6',
    'periwinkle blue': '#8F99FB',
    'pewter': '#8BA8B7',
    'pine': '#01796F',
    'powder blue': '#B0E0E6',
    'raspberry': '#E30B5D',
    'rose': '#FF007F',
    'ruby': '#E0115F',
    'rust': '#8B3103',
    'saffron': '#F4C430',
    'sage': '#BCB88A',
    'sapphire': '#0F52BA',
    'scarlet': '#FF2400',
    'sea green': '#2E8B57',
    'sepia': '#704214',
    'sienna': '#A0522D',
    'slate': '#708090',
    'smoke': '#738276',
    'steel blue': '#4682B4',
    'strawberry': '#FC5A8D',
    'sunflower': '#FFC512',
    'tangerine': '#F28500',
    'taupe': '#483C32',
    'terracotta': '#E2725B',
    'thistle': '#D8BFD8',
    'tomato': '#FF6347',
    'turquoise blue': '#00CED1',
    'umber': '#635147',
    'vanilla': '#F3E5AB',
    'vermilion': '#E34234',
    'violet blue': '#324AB2',
    'viridian': '#40826D',
    'wheat': '#F5DEB3',
    'wild strawberry': '#FF43A4',
    'wine': '#722f37',
    'zucchini': '#4CBB17',
    }
    if color_code in color:
        color_hex = color[color_code]
        rendered_template = render_template_string(html_template, color=color_hex)
        response = jsonify({'html': rendered_template})
        response.status_code = 200
        return response
    else:
        response = jsonify({'message': 'Invalid color code'})
        response.status_code = 400
        return response
