'--main_page--'
from tkinter import StringVar

geometry = '600x500+650+200'
title = 'Enterprise Access Control System'
rzb_wh = False
rzb_ht = False

'config_frame'
f_wh = 600
f_ht = 500

'--main_frame--'

'config_label'
ml_tt ='Система пропускного контроля'
ml_ttc = '#48D1CC'
ml_ft = ('Helvetica', 24, 'bold')

'config_inputs'
id_wh = 400
id_ht = 40
in_phtt = 'Введите имя пользователя >> '
iz_phtt = 'Введите название зоны для доступа >> '
id_phttc = '#000000'
id_fgc = '#A9A9A9'
id_tc = '#000000'
id_ft = ('Helvetica', 15, 'bold')

'config_menu_btn'
en_wh = 150
en_ht = 40
en_tt = 'Войти'
en_ft = ('Helvetica', 17, 'bold')
en_ttc = 'black'
en_fgc = '#239689'

ex_wh = 150
ex_ht = 40
ex_tt = 'Выход'
ex_ft = ('Helvetica', 17, 'bold')
ex_ttc = 'black'
ex_fgc = '#239689'

cr_wh = 240
cr_ht = 40
cr_tt = 'Подтвердить'
cr_ft = ('Helvetica', 17, 'bold')
cr_ttc = 'black'
cr_fgc = '#239689'

cb_values = ['Добавить нового пользователя', 'Редактировать данные пользователя', 'Удалить пользователя']
cb_wh = 380
cb_ht = 45
cb_fgc = '#A9A9A9'
cb_dfgc = '#A9A9A9'
cb_tc = '#000000'
cb_dtc = '#000000'
cb_ft = ('Helvetica', 17, 'bold')
cb_df = ('Helvetica', 15, 'bold')
cb_jf = 'center'
var = cb_values[0]

sl_tt = '________________________________________________________________________'
sl_tc = '#696969'
sl_ft = ('Helvetica', 17, 'bold')