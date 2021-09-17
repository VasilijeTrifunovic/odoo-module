from odoo import api, fields, models, SUPERUSER_ID


class Users(models.Model):
    _inherit = 'res.users'

    employee_identification = fields.Char(string='Employee Identification', required=False)
    user_login = fields.Char(string='User Login Count', compute='_get_user')

    def _get_user(self):
        current_user = self.id
        login_count = self._cr.execute(f"""SELECT * FROM res_users_log WHERE create_uid = {str(current_user)};""")
        res = self.env.cr.fetchall()
        self.user_login = len(res)

    def login_button(self):
        user = self.id
        change_user = self.with_user(user)
        return change_user
