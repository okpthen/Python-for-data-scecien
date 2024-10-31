from load_csv import load
# import pandas as pd
import matplotlib.pyplot as plt


def all_pop(db, country1, country2):
    db = db.set_index('country').loc[:, '1800':'2050']

    def convert_population(value):
        if isinstance(value, str):
            if 'k' in value:
                return float(value.replace('k', '')) * 1_000
            elif 'M' in value:
                return float(value.replace('M', '')) * 1_000_000
            elif 'B' in value:
                return float(value.replace('B', '')) * 1_000_000_000
        return float(value)
    # db = db.applymap(convert_population)
    db = db.apply(lambda col: col.map(convert_population))

    db1 = db.loc[country1]
    db2 = db.loc[country2]
    # print(db1, db2)
    plt.plot(db1, color="green", label=f"{country1}")
    plt.plot(db2, color="blue", label=f"{country2}")
    plt.legend(loc="lower right")
    plt.title("Population Projection")
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(ticks=range(0, len(db1), 40), labels=db1.index[::40])
    max_population = max(db1.max(), db2.max())
    y_ticks = range(0, int(max_population) + 20_0000_00, 20_000_000)
    y_labels = [f"{int(y / 1_000_000)}M" for y in y_ticks]
    plt.yticks(ticks=y_ticks, labels=y_labels)
    # plt.yticks(ticks=[20_000_000, 40_000_000, 60_000_000],
    #            labels=['20M', '40M', '60M'])
    # plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    file_name = ("picture/population_projection"
                 + country1 + "_" + country2 + ".png")
    plt.savefig(file_name)


def main():
    try:
        db = load("../population_total.csv")
    except Exception as e:
        print(e)
        exit(0)
    all_pop(db, "Japan", "France")


if __name__ == "__main__":
    main()
