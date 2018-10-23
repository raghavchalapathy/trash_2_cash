import read_csv as csv
import trashConstants as Tc

productList = csv.readcsv(Tc.productFileName)
BrandsList = csv.readcsv(Tc.Brands)
CatList = csv.readcsv(Tc.Cat)
Sub_CatList = csv.readcsv(Tc.Sub_Cat)

for i, product in productList.iterrows():
   str = None
   for j,brands in BrandsList.iterrows():
      if(product.MANUF_NAME == brands.BRAND_NAME):
         str = brands.slno
   for k,cat in CatList.iterrows():
      if(product.CAT_NAME == cat.CAT_NAME):
         if(str != None):
            str = str + '_' + cat.slno
         else:
            str = cat.slno
   for l,subcat in Sub_CatList.iterrows():
      if (product.SUB_CAT_NAME == subcat.SUB_CAT_NAME):
         if (str != None):
            str = str + '_' + subcat.slno
         else:
            str = subcat.slno
   if(str != None):
      print(str)
      product['new_column'] = str
      product.to_csv('csv/test.csv')




