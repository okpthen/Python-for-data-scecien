from load_csv import load
import matplotlib.pyplot as plt


def projection_life(life_df, income_df):
    life_df = life_df.loc[:, '1900']
    income_df = income_df.loc[:, '1900']
    plt.scatter(income_df, life_df)
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.title("1900")
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.savefig("picture/1900.png")


def main():
    try:
        path = "../life_expectancy_years.csv"
        life_df = load(path)
        path = "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        income_df = load(path)
    except Exception as e:
        print(e)
        exit(0)
    projection_life(life_df, income_df)


if __name__ == "__main__":
    main()
