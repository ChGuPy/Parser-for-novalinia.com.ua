# -*- coding: utf-8 -*-
import wx
from bs4 import BeautifulSoup
import urllib
import os
import glob
from prettytable import PrettyTable
from prettytable import ALL

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.basicGUI()

    def parser(self, event, filename, *urls):
        for url in urls:
            urllib.urlretrieve(url=url, filename="data/%s" % filename)
            soup = BeautifulSoup(open("data/%s" % filename), "html.parser")
            table = soup.find_all("div", "item-good bx_catalog_item double")
            x = PrettyTable()
            x.hrules = ALL
            x.field_names = [u"Наименование", u"Цена"]
            for item in table:
                name = item.find("div", "title").getText(strip=True)
                price = item.find("div", "price").getText(strip=True)
                x.add_row([name, price])
            x = x.get_string()
            self.text.AppendText(x)
            self.text.AppendText("\n")

    def basicGUI(self):
        panel = wx.Panel(self)
        # Кнопки тела приложения
        arma = wx.Button(panel, -1, u"Арматура", (0, 3), size=(156, 26))
        profile = wx.Button(panel, - 1, u"Профили алюминиевые", (0, 30), style=wx.BU_EXACTFIT)
        profile2 = wx.Button(panel, -1, u"Профили", (0, 57), size=(156, 26), style=wx.BU_EXACTFIT)
        metall_list = wx.Button(panel, - 1, u"Листовой металл", (0, 84), size=(156, 26), style=wx.BU_EXACTFIT)
        truba = wx.Button(panel, - 1, u"Труба профильная", (0, 111), size=(156, 26), style=wx.BU_EXACTFIT)
        ugolok = wx.Button(panel, - 1, u"Уголки", (0, 138), size=(156, 26), style=wx.BU_EXACTFIT)
        kirpich = wx.Button(panel, - 1, u"Кирпич", (0, 165), size=(156, 26), style=wx.BU_EXACTFIT)
        pesok_sheb = wx.Button(panel, - 1, u"Песок и щебень", (0, 192), size=(156, 26), style=wx.BU_EXACTFIT)
        cement = wx.Button(panel, - 1, u"Цемент", (0, 219), size=(156, 26), style=wx.BU_EXACTFIT)
        osb_qsb = wx.Button(panel, - 1, u"Плиты ОСБ", (0, 246), size=(156, 26), style=wx.BU_EXACTFIT)
        dsp_dvp = wx.Button(panel, - 1, u"Плиты ДСП, ДВП", (0, 273), size=(156, 26), style=wx.BU_EXACTFIT)
        doska = wx.Button(panel, - 1, u"Доски строительные", (0, 300), size=(156, 26), style=wx.BU_EXACTFIT)
        profnastil = wx.Button(panel, - 1, u"Профнастил", (160, 3), size=(156, 26), style=wx.BU_EXACTFIT)
        gipsokarton = wx.Button(panel, - 1, u"Гипсокартон", (160, 30), size=(156, 26), style=wx.BU_EXACTFIT)
        prof_gips = wx.Button(panel, - 1, u"Проф. для гипсокартона", (160, 57), size=(156, 26), style=wx.BU_EXACTFIT)
        ugli = wx.Button(panel, - 1, u"Углы и рейки", (160, 84), size=(156, 26), style=wx.BU_EXACTFIT)
        krepleniya = wx.Button(panel, - 1, u"Крепления", (160, 111), size=(156, 26), style=wx.BU_EXACTFIT)
        mayaki = wx.Button(panel, - 1, u"Маяки штукатурные", (160, 138), size=(156, 26), style=wx.BU_EXACTFIT)
        shtucaturka = wx.Button(panel, - 1, u"Штукатурка", (160, 165), size=(156, 26), style=wx.BU_EXACTFIT)
        gruntovka = wx.Button(panel, - 1, u"Грунтовка", (160, 192), size=(156, 26), style=wx.BU_EXACTFIT)
        ceresit = wx.Button(panel, - 1, u"Клей Ceresit для плитки", (160, 219), size=(156, 26), style=wx.BU_EXACTFIT)
        smrz_krvln = wx.Button(panel, - 1, u"Саморезы кровельные", (160, 246), size=(156, 26), style=wx.BU_EXACTFIT)
        brus = wx.Button(panel, - 1, u"Брус", (160, 273), size=(156, 26), style=wx.BU_EXACTFIT)
        zat = wx.Button(panel, - 1, u"Затирки Ceresit", (160, 300), size=(156, 26), style=wx.BU_EXACTFIT)
        clear = wx.Button(panel, -1, u"Очистисть поле", (550, 360), style=wx.BU_EXACTFIT)
        # Привязка кнопок
        # Меню окна c привязкой к функциям
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        infoButton = wx.Menu()
        exitButton = wx.Menu()
        ####################################################
        saveItem = fileButton.Append(101, u'Сохранить в файл')
        aboutItem = infoButton.Append(102, u'О программе')
        exit_b = exitButton.Append(wx.ID_EXIT, u"Завершение работы")
        ############################################################
        menuBar.Append(fileButton, u'Файл')
        menuBar.Append(infoButton, u'Инфо')
        menuBar.Append(exitButton, u'Выход')
        ############################################################
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exit_b)
        self.Bind(wx.EVT_MENU, self.OnSimple, aboutItem)
        self.Bind(wx.EVT_MENU, self.save, saveItem)
        font = wx.Font(9, wx.MODERN, wx.NORMAL, wx.NORMAL, False)
        self.text = wx.TextCtrl(panel, wx.VERTICAL, pos=(340, 0), size=(590, 350),
                                style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_DONTWRAP)
        self.text.SetFont(font)
        self.Bind(wx.EVT_BUTTON, self.clear, clear)
        # Название приложения
        self.SetTitle(u'Укрстройкомпани 0.1138')
        self.Show(True)

        ###### Передаем  функции parser нужные агументы в замвисимости от кнопки #######
        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'arma', "http://www.nl.ua/ru/"\
                                                                            "stroimaterialy/metall/armatura"),
                  arma)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'profile', "http://www.nl.ua/ru/"\
                                                                            "stroimaterialy/metall/"\
                                                                             "profili_alyuminievye",
                                                                            "http://www.nl.ua/ru/"\
                                                                            "stroimaterialy/metall/"\
                                                                            "profili_alyuminievye?PAGEN_1=2",),
                  profile)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'profile2', "http://www.nl.ua/ru/"\
                                                                                "stroimaterialy/metall/"\
                                                                                "profili",),
                  profile2)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'metal_list', "http://www.nl.ua/ru/" \
                                                                                "stroimaterialy/metall/armatura"),
                  metall_list)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'truba', "http://www.nl.ua/ru/" \
                                                                            "stroimaterialy/metall/truby",
                                                                            "http://www.nl.ua/ru/" \
                                                                            "stroimaterialy/metall/truby?PAGEN_1=2"),
                  truba)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'ugolok', "http://www.nl.ua/ru/" \
                                                                            "stroimaterialy/metall/ugolki",),
                  ugolok)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'kirpich', "http://www.nl.ua/ru/" \
                                                                            "stroimaterialy/betonnye_izdeliya/kirpich",
                                                                            "http://www.nl.ua/ru/" \
                                                                            "stroimaterialy/betonnye_izdeliya/"\
                                                                            "kirpich?PAGEN_1=2"),
                  kirpich)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'pesok_sheb', "http://www.nl.ua/ru/" \
                                                                      "stroimaterialy/stroitelnye_smesi/pesok_shcheben"),
                  pesok_sheb)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'cement', "http://www.nl.ua/ru/" \
                                                                            "stroimaterialy/stroitelnye_smesi/tsement"),
                  cement)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'osb_qsb', "http://www.nl.ua/ru/" \
                                                                             "stroimaterialy/derevo/OSB_QSB"),
                  osb_qsb)
        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'dsp_dvp', "http://www.nl.ua/ru/" \
                                                                                "stroimaterialy/derevo/dsp_dvp"),
                  dsp_dvp)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'doska', "http://www.nl.ua/ru/" \
                                                                             "stroimaterialy/derevo/doski_stroitelnye"),
                  doska)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'profnastil', "http://www.nl.ua/ru/" \
                                                                                "stroimaterialy/krovlya/profnastil"),
                  profnastil)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'gipsokarton', "http://www.nl.ua/ru/" \
                                                                                "otdelochnye_materialy/"\
                                                                                 "gipsokartonnye_sistemy/gipsokarton"),
                  gipsokarton)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'prof_gips', "http://www.nl.ua/ru/" \
                                                                             "otdelochnye_materialy/" \
                                                                             "gipsokartonnye_sistemy/profili"),
                  prof_gips)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'ugli', "http://www.nl.ua/ru/" \
                                                                            "otdelochnye_materialy/" \
                                                                            "gipsokartonnye_sistemy/ugly_reiki"),
                  ugli)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'krepleniya', "http://www.nl.ua/ru/" \
                                                                                "otdelochnye_materialy/" \
                                                                                "gipsokartonnye_sistemy/krepleniya",
                                                                                "http://www.nl.ua/ru/" \
                                                                                "otdelochnye_materialy/" \
                                                                                "gipsokartonnye_sistemy/krepleniya?"\
                                                                                "PAGEN_1=2"),
                  krepleniya)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'mayaki', "http://www.nl.ua/ru/" \
                                                                                "otdelochnye_materialy/" \
                                                                                "gipsokartonnye_sistemy/mayaki"),
                  mayaki)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'shtucaturka', "http://www.nl.ua/ru/" \
                                                                            "otdelochnye_materialy/" \
                                                                            "smesi/shtukaturka"),
                  shtucaturka)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'gruntovka', "http://www.nl.ua/ru/" \
                                                                                 "otdelochnye_materialy/" \
                                                                                 "smesi/gruntovka",
                                                                                "http://www.nl.ua/ru/" \
                                                                                "otdelochnye_materialy/" \
                                                                                "smesi/gruntovka?PAGEN_1=2",
                                                                                "http://www.nl.ua/ru/" \
                                                                                "otdelochnye_materialy/" \
                                                                                "smesi/gruntovka?PAGEN_1=3",
                                                                                "http://www.nl.ua/ru/" \
                                                                                "otdelochnye_materialy/" \
                                                                                "smesi/gruntovka?PAGEN_1=4",
                                                                                "http://www.nl.ua/ru/" \
                                                                                "otdelochnye_materialy/" \
                                                                                "smesi/gruntovka?PAGEN_1=5",
                                                                                "http://www.nl.ua/ru/" \
                                                                                "otdelochnye_materialy/" \
                                                                                "smesi/gruntovka?PAGEN_1=6"),
                  gruntovka)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'ceresit', "http://www.nl.ua/ru/" \
                                                                                 "otdelochnye_materialy/" \
                                                                                 "klei/klei_dlya_plitki?set_filter="\
                                                                                "y&arrFilter_5154_4098072539=Y"),
                  ceresit)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'smrz_krvln', "http://www.nl.ua/ru/stroimaterialy/"\
                                                                                "krepezh/samorezy?set_filter=y&arr"\
                                                                                "Filter_5156_1780637391=Y"),
                  smrz_krvln)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'brus', "http://www.nl.ua/ru/" \
                                                                            "stroimaterialy/derevo/brus"),
                  brus)

        self.Bind(wx.EVT_BUTTON, lambda event: self.parser(event, 'zat', "http://www.nl.ua/ru/otdelochnye_materialy/"
                                                                        "smesi/zatirki?set_filter="\
                                                                          "y&arrFilter_5154_4098072539=Y",
                                                                        "http://www.nl.ua/ru/otdelochnye_materialy/" \
                                                                        "smesi/zatirki?set_filter=" \
                                                                        "y&arrFilter_5154_4098072539=Y&PAGEN_1=2",
                                                                        "http://www.nl.ua/ru/otdelochnye_materialy/" \
                                                                        "smesi/zatirki?set_filter=" \
                                                                        "y&arrFilter_5154_4098072539=Y&PAGEN_1=3"),
                  zat)


    def OnSimple(self, event):
        wx.MessageBox(u"Пх’нглуи мглв’нафх Ктулху Р’льех вгах’нагл фхтагн")  # Восславим Ктулху!

    def Quit(self, e):
        for hgx in glob.glob('data/*'):
            os.remove(hgx)
        self.Close()

    # Очистка текстового поля
    def clear(self, e):
        self.text.Clear()

    # Сохранение данных текстового поля
    def save(self, e):
        text = self.text.GetValue()
        text = text.encode('utf-8')
        savefile = open('prices.txt', 'w')
        savefile.write(text)
        savefile.close()

def main():
    app = wx.App()
    windowClass(None, size=(950, 470), style=wx.SYSTEM_MENU | wx.CAPTION)
    app.MainLoop()

main()