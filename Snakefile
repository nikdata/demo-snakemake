rule download_data:
    output:
        raw_data = "data/iris.csv"
    script:
        "dl.py"

rule make_hist:
    input:
        'data/iris.csv'
    output:
        plot = 'plots/histogram.png'
    script:
        "plt.py"