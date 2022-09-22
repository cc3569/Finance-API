class dupont:
    
    def fw_calc(self, profitMargin:float, totalAssetTurnover:float, finLeverage:float):
        self.profitMargin = profitMargin
        self.totalAssetTurnover = totalAssetTurnover
        self.finLeverage = finLeverage
        return profitMargin * totalAssetTurnover * finLeverage

    def calc_profitMargin(self, netIncome:float, revenue:float):
        self.netincome = netIncome
        self.revenue = revenue
        return netIncome / revenue

    def calc_AssetTurnover(self, netSales:float, avgTotalAssets:float):
        self.netSales = netSales
        self.avgTotalAssets = avgTotalAssets
        return netSales * avgTotalAssets

    def calc_FinLeverage(self, totalLiabilities:float, shareholderEquity:float):
        self.totalLiabilities = totalLiabilities
        self.shareholderEquity = shareholderEquity
        return totalLiabilities / shareholderEquity