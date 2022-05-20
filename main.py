import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
# wieksza_od_1000 = df.loc[df.Liczba > 1000]
# print(wieksza_od_1000)
#
# imie = df.loc[df.Imie == 'RADOSŁAW']
# print(imie)
#
# print(df.agg({'Liczba':['sum']}))
#
# print(df.loc[df.Rok>=2000].loc[df.Rok<=2005].agg({'Liczba':['sum']}))
#
# grupaplec = df.groupby('Plec')
# print(grupaplec.agg({'Liczba':['sum']}))
#
# plecrok = df.groupby(['Plec','Rok'], as_index=False)['Liczba']
#
# # for m in plecrok.groups.keys():
# #     print(plecrok.get_group(m).sort_values(by='Liczba').iloc[-1])
#
# print(plecrok.max())
#
# # print(df.sort_values(by='Liczba').iloc[-1])

df1 = pd.read_csv('datasets/zamowienia.csv', sep=';')
#
# print(df1.sort_values(by='Utarg',ascending=False).head(5))
# print(set(df1.Sprzedawca))
# print(df1.groupby('Sprzedawca').size())
# print(df1.groupby('Kraj').agg({'Utarg':['sum']}))
# mask2005 = (df1['Data zamowienia'] >= "2005-01-01") & (df1['Data zamowienia'] <= "2005-12-31")
# print(df1[mask2005].groupby('Kraj').get_group('Polska').agg({'Utarg':['sum']}))

# dzieciroku = df.groupby('Rok').agg({'Liczba':['sum']})
# wykres = dzieciroku.plot()
# wykres.set_xlabel('Rok')
# wykres.set_ylabel('Dzieci')
# wykres.legend()
# plt.xticks([x for x in range (2000,2020) if x%2==0])
# plt.show()

# dzieciplec = df.groupby('Plec',as_index=False).sum()
# dzieciplec.drop('Rok',axis=1,inplace=True)
# plt.bar(dzieciplec['Plec'],dzieciplec['Liczba'],color=['Red','Blue'])
# plt.show()


# df5lat = df[df['Rok']>=2012].groupby('Plec',as_index=False).sum()
# df5lat['Liczba'].plot(kind='pie', autopct='%.2f%%',labels=["Mezczyzni", "Kobiety"])
# plt.legend(['M','K'])
# plt.show()

wykres_zad4 = df1.groupby('Sprzedawca').size()
wykres_zad4.plot(kind='bar', color=['Red', 'Blue', 'Yellow', 'Black', 'Green', 'Gray', 'Pink', 'Cyan', 'Purple'])
plt.show()
