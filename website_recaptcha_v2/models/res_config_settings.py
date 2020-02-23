# Copyright 2019 Sunflower IT <https://www.sunflowerweb.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    display_recaptcha_settings = fields.Boolean(
        string="Set Recaptcha v2"
    )

    recaptcha_website_secret_key = fields.Char(
        string="Google Recaptcha v2 Secret Key"
    )
    recaptcha_website_site_key = fields.Char(
        string="Google Recaptcha v2 Secret Key"
    )

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        param.set_param('website_recaptcha_v2.recaptcha_website_secret_key',
                        self.recaptcha_website_secret_key)
        param.set_param('website_recaptcha_v2.recaptcha_website_site_key',
                        self.recaptcha_website_site_key)

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            recaptcha_website_secret_key=self.env[
                'ir.config_parameter'].sudo().get_param(
                'website_recaptcha_v2.recaptcha_website_secret_key'),
            recaptcha_website_site_key=self.env[
                'ir.config_parameter'].sudo().get_param(
                'website_recaptcha_v2.recaptcha_website_site_key')
        )
        return res
