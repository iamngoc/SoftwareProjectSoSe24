import pandas

df = pandas.read_excel('Uni-hannover.xlsx', header=None, names=["Parent Link (ID URL)", "Child Link (ID URL)"], usecols=["Parent Link (ID URL)"])

df_toList = df["Parent Link (ID URL)"].to_list()
print(df_toList)
def countLinks(link, count):
    while next(link) is None:
        count += 1
        link = next(link)
    return count

#rows = df[df.columns[0]].count()
#print(rows)
count = 0
link = df.at[1, "Parent Link (ID URL)"]

print(link)
f1 = countLinks(link, count)
print(f1)

def up_da_ter3(df):
    count = 0
    columns = df.columns.tolist()
    for _, i in df.iterrows():
        for c in columns:
            if i[c].apply(lambda x: 1 if df.isnull(x) == True else 0):
                count = count + 1
                print(i[c])

