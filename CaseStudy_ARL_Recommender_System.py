#############################################
# Association Rule Based Recommender System
#############################################

#############################################
# İş Problemi
#############################################
# Aşağıda 3 farklı kullanıcının sepet bilgileri verilmiştir.
# Bu sepet bilgilerine en uygun ürün önerisini birliktelik kuralı kullanarak yapınız. Ürün önerileri 1 tane ya da 1'den fazla olabilir.
# Karar kurallarını 2010-2011 Germany müşterileri üzerinden türetiniz.

# Kullanıcı 1’in sepetinde bulunan ürünün id'si: 21987
# Kullanıcı 2’in sepetinde bulunan ürünün id'si : 23235
# Kullanıcı 3’in sepetinde bulunan ürünün id'si : 22747

#############################################
# Veri Seti Hikayesi
#############################################

# Online Retail II isimli veri seti İngiltere merkezli bir perakende şirketinin 01/12/2009 - 09/12/2011 tarihleri arasındaki online satış işlemlerini içeriyor.
# Şirketin ürün kataloğunda hediyelik eşyalar yer almaktadır ve çoğu müşterisinin toptancı olduğu bilgisi mevcuttur.

# 8 Değişken, 541.909 Gözlem, 45.6MB

# InvoiceNo: Fatura Numarası ( Eğer bu kod C ile başlıyorsa işlemin iptal edildiğini ifade eder )
# StockCode: Ürün kodu ( Her bir ürün için eşsiz )
# Description: Ürün ismi
# Quantity: Ürün adedi ( Faturalardaki ürünlerden kaçar tane satıldığı)
# InvoiceDate: Fatura tarihi
# UnitPrice: Fatura fiyatı ( Sterlin )
# CustomerID: Eşsiz müşteri numarası
# Country: Ülke ismi

#############################################
# Proje Görevleri
#############################################

#############################################
# Görev 1: Veriyi Hazırlama
#############################################

# Adım 1: Online Retail II veri setinden 2010-2011 sheet’ini okutunuz.

# !pip install mlxtend
import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
# çıktının tek bir satırda olmasını sağlar.
pd.set_option('display.expand_frame_repr', False)
from mlxtend.frequent_patterns import apriori, association_rules

df_ = pd.read_excel("datasets/online_retail_II.xlsx", sheet_name="Year 2010-2011")
df = df_.copy

def check_dataframe(df, row_num=5):
    print("*************** Dataset Shape ***************")
    print("No. of Rows:", df.shape[0], "\nNo. of Columns:", df.shape[1])
    print("*************** Dataset Information ***************")
    print(df.info())
    print("*************** Types of Columns ***************")
    print(df.dtypes)
    print(f"*************** First {row_num} Rows ***************")
    print(df.head(row_num))
    print(f"*************** Last {row_num} Rows ***************")
    print(df.tail(row_num))
    print("*************** Summary Statistics of The Dataset ***************")
    print(df.describe().T)
    print("*************** Dataset Missing Values Analysis ***************")
    print(df.isnull().sum())
    print("*************** Dataset Duplicates ***************")
    print(df[df.duplicated() == True])


check_dataframe(df)

# Adım 2: StockCode’u POST olan gözlem birimlerini drop ediniz. (POST her faturaya eklenen bedel, ürünü ifade etmemektedir.)
# Adım 3: Boş değer içeren gözlem birimlerini drop ediniz.
# Adım 4: Invoice içerisinde C bulunan değerleri veri setinden çıkarınız. (C faturanın iptalini ifade etmektedir.)
# Adım 5: Price değeri sıfırdan küçük olan gözlem birimlerini filtreleyiniz.
# Adım 6: Price ve Quantity değişkenlerinin aykırı değerlerini inceleyiniz, gerekirse baskılayınız.


#############################################
# Görev 2:  Alman Müşteriler Üzerinden Birliktelik Kuralları Üretme
#############################################


# Adım 1: check_id fonksiyonunu kullanarak verilen ürünlerin isimlerini bulunuz.
# Adım 2: arl_recommender fonksiyonunu kullanarak 3 kullanıcı için ürün önerisinde bulununuz.
# Adım 3: Önerilecek ürünlerin isimlerine bakınız.