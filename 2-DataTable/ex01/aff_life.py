from load_csv import load
# import pandas as pd
import matplotlib.pyplot as plt


def all_life(db, country):
    db = db.set_index('country')
    data = db.loc[country]
    print(data)
    plt.plot(data)
    plt.title(f'{country} Life Expenctancy Projection')
    plt.xlabel('Year')
    plt.xticks(ticks=range(0, len(data), 40), labels=data.index[::40])
    plt.ylabel('Life Expectancy')
    file_name = "picture/life_expectancy_" + country + ".png"
    plt.savefig(file_name)
    # グラフを保存
    # country_data = db[(db['country'] == country)]
    # # japan = db.query('country == "Japan"')
    # # print(country_data)
    # country_data.set_index('country')
    # years = country_data.columns
    # life_expectancy = country_data.values[0]
    # print(years)
    # print(life_expectancy)
    # print(len(years), len(life_expectancy))
    # years = years.to_numpy()
    # print(type(years), type(life_expectancy))

    # 線グラフを描画
    # plt.figure(figsize=(12, 6))
    # plt.plot(years, life_expectancy)
    # plt.title(f'{country} Life Expenctancy Projection')
    # plt.xlabel('Year')
    # plt.ylabel('Life Expectancy (Years)')
    # plt.xticks(rotation=45)
    # plt.savefig('life_expectancy_japan.png')


def main():
    try:
        db = load("../life_expectancy_years.csv")
    except Exception as e:
        print(e)
        exit(0)
    all_life(db, "Japan")


if __name__ == "__main__":
    main()
