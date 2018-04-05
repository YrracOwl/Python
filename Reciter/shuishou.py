#-*- coding: UTF-8 -*-
from tkinter import ttk
import tkinter as tk


#用于查询各种税的计算Table中
#所有税收
taxsorts = ("增值税","消费税","关税","企业所得税","个人所得税","其他税")

#增值税
ZZ_YBNSR = ("应纳税额=销项税额-进项税","销项税额=销售额×税率  此处税率为17%","组成计税价格=成本×（1+成本利润率）","组成计税价格=成本×（1+成本利润率）÷（1-消费税税率）")
ZZ_JKHW = ("应纳税额 = 组成计税价格 × 税率","组成计税价格=关税完税价格+关税（+消费税）")
ZZ_XGMNSR = ("应纳税额=销售额×征收率","销售额=含税销售额÷（1+征收率）")
#消费税
XFS_YBQK = ("应纳税额=销售额×税率","不含税销售额=含税销售额÷（1+增值税税率或征收率）","组成计税价格=（成本 + 利润）÷（1 - 消费税率）","组成计税价格=成本×（1+成本利润率）÷（1-消费税税率）","组成计税价格=（材料成本+加工费）÷（1-消费税税率）","组成计税价格=（关税完税价格+关税）÷（1-消费税税率）")
XFS_CLJZ = ("应纳税额=销售数量×单位税额","                                       ")
#关税
GS_CJJZ = ("应纳税额=应税进口货物数量×单位完税价×适用税率","                                   ")
GS_CLJZ = ("应纳税额=应税进口货物数量×关税单位税额","                                       ")
GS_FHJZ = ("应纳税额=应税进口货物数量×关税单位税额+应税进口货物数量×单位完税价格×适用税率","                                    ")
#企业所得税
QYSDS = ("应纳税所得额=收入总额-准予扣除项目金额","应纳税所得额=利润总额+纳税调整增加额—纳税调整减少额","应纳税额=应纳税所得额×税率","月预缴额=月应纳税所得额×25%","月应纳税所得额=上年应纳税所得额×1/12","")
#个人所得税
GRSDS_GZXJ = ("应纳税额=应纳税所得额×使用税率 - 速算扣除数","                              ")
GRSDS_GC = ("应纳税额=应纳税所得额×使用税率×（1-30%）","                            ")
GRSDS_QTGX = ("应纳税额=应纳税所得额×使用税率","                                 ")
#其他税收
QT_CZTD = ("年应纳税额=计税土地面积（平方米）×使用税率","                                     ")
QT_FDC = ("年应纳税额=应税房产原值×（1 - 扣除比例）×1.2%","或年应纳税额=租金收入×12%")
QT_ZY = ("年应纳税额=课税数量×单位税额","                                     ")
QT_TDZZ =("增值税=转让房地产取得的收入 - 扣除项目","应纳税额=∑（每级距的土地增值额×适用税率）")
QT_QS = ("应纳税额计税依据×税率","                                            ")

def taxSorts():    
    return taxsorts

def stage2ndint(text):
    if text == 0:
        return ("一般纳税人         ","进口货物         ","小规模纳税人    ","              ","                  ")
    if text == 1:
        return ("一般情况          ","从量计征_1          ","                    ","              ","                  ")
    if text == 2:
        return ("从价计征          ","从量计征_2          ","复合计征            ","              ","                  ")
    if text == 3:
        return ("通用              ","                  ","                  ","                  ","                  ")
    if text == 4:
        return ("工资薪金所得  ","稿酬所得      ","其他各项所得  ","              ","                  ")
    if text == 5:
        return ("城镇土地使用税","房地产税      ","资源税        ","土地增值税    ","契税          ")        

def stage3rd(frames,text):
    text = text.split()[0]

    for counter in range(7):
        tk.Label(frames,text="                                                                                      ",width=160,height=2).grid(column=0,row=counter,sticky="WE")
    
    #增值税
    if text == "一般纳税人":
        for counter in range(4):
            ttk.Label(frames,text=ZZ_YBNSR[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
    
    if text == "进口货物":
        for counter in range(2):
            ttk.Label(frames,text=ZZ_JKHW[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
    
    if text == "小规模纳税人":
        for counter in range(2):
            ttk.Label(frames,text=ZZ_XGMNSR[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
    
    #消费税
    if text == "一般情况":
        for counter in range(6):
            ttk.Label(frames,text=XFS_YBQK[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
            
    if text == "从量计征_1":
        for counter in range(1):
            ttk.Label(frames,text=XFS_CLJZ[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
    
    #关税
    if text == "从价计征":
        for counter in range(1):
            ttk.Label(frames,text=GS_CJJZ[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
        
    if text == "从量计征_2":
        for counter in range(1):
            ttk.Label(frames,text=GS_CLJZ[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
            
    if text == "复合计征":
        for counter in range(1):
            ttk.Label(frames,text=GS_FHJZ[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
    
    #企业所得税
    if text == "通用":
        for counter in range(5):
            ttk.Label(frames,text=QYSDS[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
    
    #个人所得税
    if text == "工资薪金所得":
        for counter in range(1):
            ttk.Label(frames,text=GRSDS_GZXJ[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
    
    if text == "稿酬所得":
        for counter in range(1):
            ttk.Label(frames,text=GRSDS_GC[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")

    if text == "其他各项所得":
        for counter in range(1):
            ttk.Label(frames,text=GRSDS_QTGX[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")

    #其他税收
    if text == "城镇土地使用税":
        for counter in range(1):
            ttk.Label(frames,text=QT_CZTD[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
            
    if text == "房地产税":
        for counter in range(2):
            ttk.Label(frames,text=QT_FDC[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
            
    if text == "资源税":
        for counter in range(1):
            ttk.Label(frames,text=QT_ZY[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
            
    if text == "土地增值税":
        for counter in range(2):
            ttk.Label(frames,text=QT_TDZZ[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
            
    if text == "契税":
        for counter in range(1):
            ttk.Label(frames,text=QT_QS[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter,sticky="W")
            
    for child in frames.winfo_children():
        child.grid_configure(padx=8, pady=4)        
    

#用于查询应纳税额计算Table中
taxmoney = ("增值税","消费税","企业所得税","个人所得税","土地增值税","城市建设维护税","资源税","车船税","土地使用税","印花税","关税","房产税")
#增值税        
ZJ_JSF = ("应纳增值税额：＝增值额×增值税税率","增值额＝工资＋利息＋租金＋利润＋其他增值项目-货物销售额的全值-法定扣除项目购入货物金额")
JJ_JSF = ("扣除税额＝扣除项目的扣除金额×扣除税率","1.购进扣税法","    扣除税额＝本期购入扣除项目金额×扣除税率＋已由受托方代收代缴的税额","2.实耗扣税法","    扣除税额＝本期实际耗用扣除项目金额×扣除税率＋已由受托方代收代交的税额","    （1）一般纳税人应纳增值税额","        一般纳税人应纳增值税额＝当期销项税额－当期进项税额","          (一)销项税额＝销售额×税率","            销售额＝含税销售额/（1＋税率）","            组成计税价格＝成本×（1＋成本利润率）","          (二)进项税额","            不得抵扣的进项税额＝当月全部进项税额×当月免税项目销售额、非应税项目营业额合计/当月全部销售额、营业额合计","    （2）小规模纳税人应纳增值税额","        小规模纳税人应纳增值税额＝销售额×征收率","        销售额＝含税销售额/（1＋征收率）","        销售额＝含税收入（1＋增值税征收率）","    （3）进口货物应纳增值税额","        进口货物应纳增值税额＝组成计税价格×税率","        组成计税价格＝关税免税价格＋关税＋消费税")
#消费税
CJDLDJS = ("实行从价定率办法计算的应纳消费税额＝销售额×税率","1.应税消费品的销售额＝含增值税的销售额/(1＋增值税税率或征收率)","2.组成计税价格＝（成本＋利润）/（1-消费税率）","3.组成计税价格＝（材料成本＋加工费）/（1-消费税率）","4.组成计税价格＝关税完税价格＋关税＋应纳消费税税额","5.组成计税价格＝（关税完税价格＋关税）/（1-消费税税率）")
CLDEDJS = ("实行从量定额办法计算的应纳消费税额＝销售数量×单位数额","")
#企业所得税
GYQY = ("工业企业应纳税所得额＝利润总额＋（－）税收调整项目金额","利润总额＝营业利润＋投资收益＋营业外收入－营业外支出","营业利润＝产品销售利润＋其他业务利润－管理费用－财务费用","产品销售利润＝产品销售收入－产品销售成本－产品销售费用－产品销售税金及附加","其他业务利润＝其他业务收入－其他业务成本－其他销售税金及附加","本期完工产品成本＝期初在产品自制半成品成本余额＋本期产品成本会计－期末在产品自制半成品成本余额","本期产品成本会计＝材料＋工资＋制造费用")
SPLTQY = ("应纳税所得额＝利润总额＋（－）税收调整项目金额","利润总额＝营业利润＋投资收益＋营业外收入－营业外支出","营业利润＝主营业务利润＋其他业务利润－管理费用－财务费用－汇兑损失","主营业务利润＝商品销售利润＋代购代销收入","商品销售利润＝商品销售净额－商品销售成本－经营费用－商品销售税金及附加","商品销售净额＝商品销售收入－销售折扣与折让")
YFQY = ("应纳税所得额＝利润总额＋（－）税收调整项目金额","利润总额＝营业利润＋投资收益＋营业外收入－营业外支出","营业利润＝经营利润＋附营业务收入－附营业务成本","经营利润＝营业收入－营业成本－营业费用－营业税金及附加","营业成本＝期初库存材料、半成品产成（商）品盘存余额＋本期购进材料、商品金额金额－期末库存材料、半成品、产成（商）品盘存余额")
#个人所得税额
GZXZSD = ("工资、薪金所得应纳个人所得税额＝应纳水所得额×适用税率－速算扣除数","应纳税所得额＝每月收入额－800","应纳税额＝应纳税所得额×适用税率－速算扣除数","应纳税所得额＝（不含税所得额－速算扣除数）/(1-税率)")
GTGSH = ("应纳所得税额＝应纳税所得额×适用税率－速算扣除数","1.将当月累计应纳税所得额换算成全年应纳税所得额","    全年应纳税所得额＝当月累计应纳税所得额×12/当月累计经营月份数","2.计算全年应纳所得税额","    全年应纳所得税额＝全年应纳税所得额×适用税率－速算扣除数","3.计算当月累计应纳所得税额","    当月应纳所得税额＝全年应纳所得税额×当月累计经营月份数/12","4.计算本月应纳所得税额","    本月应纳所得税额＝当月累计应纳所得税额－累计已缴所得税额")
GCSD = ("应纳所得税额＝应纳税所得额×20%×（1-30%）＝应纳税所得额×20%×70%","")
LWBCSD = ("1.一次收入在20000元以下时","    应纳所得税额＝应纳税所得额×20%","2.一次收入20000～50000时","    应纳所得税额＝应纳税所得额×20%＋应纳税所得额×20%×50%＝应纳税所得额×（20%＋10%）","3.一次收入超过50000时","应纳所得税税额＝应纳税所得额×20%＋应纳税所得额×20%×100%＝应纳税所得额×（20%＋20%）")
CCZR = ("财产转让应纳所得税额＝应纳税所得额×20%","应纳税所得额＝转让财产收入额－财产原值－合理费用")
LXGXHLSD = ("应纳所得税额＝应纳税所得额×20%","")
JYGRSDSK = ("境外个人所得税税款扣除限额＝境内、境外所得按税法计算的应纳税总额×来源于某外国的所得额/境内、外所得总额","")
ZFGKKYWR = ("手续费金额＝扣缴的个人所得税额×2%","")
#土地增值税
YBJSFF = ("应纳税总额＝∑各级距土地增值额×适用税率","某级距土地增值额×适用税率","土地增值率＝土地增值额×100%/扣除项目金额","土地增值额＝转让房地产收入－扣除项目金额")
JBJSFF = ("1.土地增值额未超过扣除项目金额金额50%的","    应纳税额＝土地增值额×30%","2.土地增值额超过扣除项目金额50%，未超过100%的","    应纳税额＝土地增值额×40%－扣除项目金额×0.05","3.土地增值额超过扣除项目金额100%、未超过200%的","    应纳税额＝土地增值额×50%－扣除项目金额×0.15","4.土地增值额超过项目金额200%","    应纳税额＝土地增值额×60%－扣除项目金额×0.35")
#城市建设维护税
TY1 = ("应纳城市维护建设税额＝（产品销售收入额＋营业收入额＋其他经营收入额）×地区适用税率 ","应补交税额=实际营业收入额×地区适用税率－已纳税额","应退税额＝已交税额－核实后的应纳税额")
#资源税
TY2 = ("应纳税额＝课税数量×单位税额","")
#车船税
FJDCLD = (" 乘人车、二轮摩托车、三轮摩托车、畜力车、人力车、自行车等车辆的年应纳税额的计算公式为：","    年应纳税额＝车辆拥有量×适用的年税额")
ZHC = ("年应纳税额=载货汽车净吨位×适用的年税额","")
KHLYC = ("年应纳税额=载人部分年应纳税额+载货部分年应纳税额","载人部分年应纳税额=载人车适用年税额×50%","载货部分年应纳税额=载货部分的净吨位数×适用的年税额")
JDC = ("机动船年应纳税额=机动船的净吨位×适用的年税额","")
FJDC = ("非机动船应纳税额=非机动船的载重吨位×适用的年税额","")
XGMDCL = ("新购买的车辆按购期年内的余月数比例征收车船税，其计算公式为：","    新购买车船应纳车船税额=各种车船的吨位（或辆数）×购进起始月至征期终了的余月数/征期月数","    补交本期漏报漏缴税额=漏报漏缴车船税的数量(或净吨位、载重吨位)×适用税额/按规定缴库的次数","    补交本期少交的税款=[应缴车船税的数量（或净吨位、载重吨位）×适用税额/按规定缴库的次数]－已缴税款","    退还误交的税款＝已缴的误交税款","    退还应计算错误而多交的税款＝已入库的税款－重新核实后的应纳税额")
#房产税
FCSE = ("年应纳房产税税额＝房产评估值×税率","月应纳房产税税额=年应纳房产税额/12","季应纳房产税税额=年应纳房产税额/4")
#土地使用税额
TDSYSE = ("年应纳土地使用税税额=使用土地的平方米总数×每平方米土地年税额","月或季应纳土地使用税税额=年应纳土地使用税额/12（或）4")
#印花税
GXHT = ("应纳税额=购销金额×3/1000","")
JSGCKWSJ = ("应纳税额=收取的费用×5/10000","")
JGCL = ("应纳税额=加工及承揽收入×5/10000","")
JZAZGCCB = ("应纳税额=承包金额×3/10000","")
CCZL = ("应纳税额=租赁金额×1/1000","")
CCBG = ("应纳税额=仓储保管费用×1/1000","")
JK = ("应纳税额=借款金额×0.5/10000","")
CCBX = ("应纳税额=保险费收入×1/1000","")
CQZYSJ = ("应纳税额=书据所载金额×6/10000","")
JSHT = ("应纳税额=合同所载金额×3/10000","")
HWYSHT = ("应纳税额=运输费用×5/10000","")
YYZP = ("1.记载资金账簿应纳印花税的计算公式为：","    应纳税额=[（固定资产原值年初数－上年已计算缴纳印花税固定资产原值）＋（自有流动资金年初数－上年已计算缴纳印花税自有流动资金总额）]×5/10000","2.其他账簿应纳税额的计算公式为：","    应纳税额=证照件数×5")
#关税
GS_JKGS = ("应纳关税税额=完税价格×进口税率","完税价格=离岸价格+运输费、保险费等=国内批发价/（1+进口税率+费用和利润率（20%））")
GS_CKGS = ("出口关税应纳税额=完税价格×出口税率","完税价格=离岸价格/（1+出口税率）")


def taxMoney():
    return taxmoney
    
def money2ndint(text):
    if text == 0:
        return ("直接计税法         ","间接计税法         ")
    if text == 1:
        return ("从价定率的计算          ","从量定额的计算          ")
    if text == 2:
        return ("工业企业          ","商品流通企业          ","饮服企业            ")
    if text == 3:
        return ("工资、薪金所得              ","个体工商户                 ","稿酬所得                 ","劳务报酬所得                  ","财产转让                  ","利息、股息红利所得","境外个人所得税款扣除限额","支付给扣缴义务人手续费的计算")
    if text == 4:
        return ("一般计算方法         ","简便计税方法                    ")
    if text == 5:
        return ("通用1             ","                        ")
    if text == 6:
        return ("通用2             ","                        ") 
    if text == 7:
        return ("乘非机动车等车辆             ","载货车                        ","客货两用的车                           ","机动船                       ","非机动船                          ","新购买的车辆                          ") 
    if text == 8:
        return ("通用3             ","                        ") 
    if text == 9:
        return ("购销合同             ","建设工程勘察设计合同                        ","加工承揽合同                           ","建筑安装工程承包合同                       ","财产租赁合同                          ","仓储保管合同                          ","借款合同                          ","财产保险合同                          ","产权转移书据                          ","技术合同                          ","货物运输合同                          ","营业账簿                          ") 
    if text == 10:
        return ("进口关税","出口关税")
    if text == 11:
        return ("通用4","                        ")        

   
def money3rd(frames,text):
    text = text.split()[0]
    
    for counter in range(20):
        tk.Label(frames,text="                                                                                                                                                                                                                                                                                                                                                                                ",width=160,height=1).grid(column=0,row=counter,sticky="W")
    
    #增值税
    if text == "直接计税法":
        for counter in range(len(ZJ_JSF)):
            tk.Label(frames,text=ZJ_JSF[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")
            
    if text == "间接计税法":
        for counter in range(len(JJ_JSF)):
            tk.Label(frames,text=JJ_JSF[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")
    
    #消费税
    if text == "从价定率的计算":
        for counter in range(len(CJDLDJS)):
            tk.Label(frames,text=CJDLDJS[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")
            
    if text == "从量定额的计算":
        for counter in range(len(CLDEDJS)):
            tk.Label(frames,text=CLDEDJS[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")     

    #企业所得税
    if text == "工业企业":
        for counter in range(len(GYQY)):
            tk.Label(frames,text=GYQY[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")    
            
    if text == "商品流通企业":
        for counter in range(len(SPLTQY)):
            tk.Label(frames,text=SPLTQY[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")       

    if text == "饮服企业":
        for counter in range(len(YFQY)):
            tk.Label(frames,text=YFQY[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")
            
    #个人所得税额
    if text == "工资、薪金所得":
        for counter in range(len(GZXZSD)):
            tk.Label(frames,text=GZXZSD[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")
            
    if text == "个体工商户":
        for counter in range(len(GTGSH)):
            tk.Label(frames,text=GTGSH[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")     

    if text == "稿酬所得":
        for counter in range(len(GCSD)):
            tk.Label(frames,text=GCSD[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")
            
    if text == "劳务报酬所得":
        for counter in range(len(LWBCSD)):
            tk.Label(frames,text=LWBCSD[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")
            
    if text == "财产转让":
        for counter in range(len(CCZR)):
            tk.Label(frames,text=CCZR[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")            
            
    if text == "利息、股息红利所得":
        for counter in range(len(LXGXHLSD)):
            tk.Label(frames,text=LXGXHLSD[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")

    if text == "境外个人所得税款扣除限额":
        for counter in range(len(JYGRSDSK)):
            tk.Label(frames,text=JYGRSDSK[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W") 

    if text == "支付给扣缴义务人手续费的计算":
        for counter in range(len(ZFGKKYWR)):
            tk.Label(frames,text=ZFGKKYWR[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")

    #土地增值税        
    if text == "一般计算方法":
        for counter in range(len(YBJSFF)):
            tk.Label(frames,text=YBJSFF[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")

    if text == "简便计税方法":
        for counter in range(len(JBJSFF)):
            tk.Label(frames,text=JBJSFF[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")

    #城市建设维护税       
    if text == "通用1":
        for counter in range(len(TY1)):
            tk.Label(frames,text=TY1[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W") 

    #资源税        
    if text == "通用2":
        for counter in range(len(TY2)):
            tk.Label(frames,text=TY2[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")  

    #车船税        
    if text == "乘非机动车等车辆":
        for counter in range(len(FJDCLD)):
            tk.Label(frames,text=FJDCLD[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W") 

    if text == "载货车":
        for counter in range(len(ZHC)):
            tk.Label(frames,text=ZHC[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")   

    if text == "客货两用的车":
        for counter in range(len(KHLYC)):
            tk.Label(frames,text=KHLYC[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")

    if text == "机动船":
        for counter in range(len(JDC)):
            tk.Label(frames,text=JDC[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W") 

    if text == "非机动船":
        for counter in range(len(FJDC)):
            tk.Label(frames,text=FJDC[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")   

    if text == "新购买的车辆":
        for counter in range(len(XGMDCL)):
            tk.Label(frames,text=XGMDCL[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")

    #房产税
    if text == "通用4":
        for counter in range(len(FCSE)):
            tk.Label(frames,text=FCSE[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")

    #土地使用税额
    if text == "通用3":
        for counter in range(len(TDSYSE)):
            tk.Label(frames,text=TDSYSE[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")   

    #印花税
    if text == "购销合同":
        for counter in range(len(GXHT)):
            tk.Label(frames,text=GXHT[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W") 

    if text == "建设工程勘察设计合同":
        for counter in range(len(JSGCKWSJ)):
            tk.Label(frames,text=JSGCKWSJ[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")   

    if text == "加工承揽合同":
        for counter in range(len(JGCL)):
            tk.Label(frames,text=JGCL[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W") 

    if text == "建筑安装工程承包合同":
        for counter in range(len(JZAZGCCB)):
            tk.Label(frames,text=JZAZGCCB[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")  

    if text == "财产租赁合同":
        for counter in range(len(CCZL)):
            tk.Label(frames,text=CCZL[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")  

    if text == "仓储保管合同":
        for counter in range(len(CCBG)):
            tk.Label(frames,text=CCBG[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")    

    if text == "借款合同":
        for counter in range(len(JK)):
            tk.Label(frames,text=JK[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")   

    if text == "财产保险合同":
        for counter in range(len(CCBX)):
            tk.Label(frames,text=CCBX[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")     

    if text == "产权转移书据":
        for counter in range(len(CQZYSJ)):
            tk.Label(frames,text=CQZYSJ[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")        

    if text == "技术合同":
        for counter in range(len(JSHT)):
            tk.Label(frames,text=JSHT[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W") 

    if text == "货物运输合同":
        for counter in range(len(HWYSHT)):
            tk.Label(frames,text=HWYSHT[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")  

    if text == "营业账簿":
        for counter in range(len(YYZP)):
            tk.Label(frames,text=YYZP[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")  

    if text == "进口关税":
        for counter in range(len(GS_JKGS)):
            tk.Label(frames,text=GS_JKGS[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")   

    if text == "出口关税":
        for counter in range(len(GS_CKGS)):
            tk.Label(frames,text=GS_CKGS[counter],font=("Microsoft YaHei",12)).grid(column=0,row=counter+1,sticky="W")            