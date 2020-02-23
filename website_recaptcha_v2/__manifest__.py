# Copyright 2019 Kevin Kamau
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Web Recaptcha V2',
    'version': '12.0.1.0.0',
    'category': 'Website',
    'license': 'LGPL-3',
    'website': "www.odoo-kenya.co.ke",
    'author': "Kevin Kamau",
    'summary': "This modules adds recaptcha v2 features to Odoo",
    'license': 'LGPL-3',
    'depends': [
        'website',
    ],
    'data': [
        'views/res_config_settings.xml'
    ],
    # 'images': ['images/main_screenshot.png'],
    'installable': True,
}
