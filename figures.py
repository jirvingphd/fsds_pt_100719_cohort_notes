def eda_plot(df, col = 'bedrooms', target='price',
            figsize=(10,5),hist_kws = None, kde_kws = None):
    """Plots a seaborn disrplot and a scatter plot of col vs target.
    
    Args:
        df (DataFrame): data to plot
        col (str): Name of the column to plot
        target (str): Name of the target variable for scatterplot
        figsize (tup): Figsize
        hist_kws (dict): Keywords for seaborn distplot histogram
        kde_kws (dict): Keywords for seaborn distplot kde
        
    Returns:
        fig (Figure Object)
        ax (list of Axes objects)
    """
    # Lets write our plot together
    import matplotlib.pyplot as plt
    import seaborn as sns 
    fig, axes = plt.subplots(ncols=2,figsize=figsize)

    ax = axes[0]
    
    
    if hist_kws is None:
        hist_kws = {'edgecolor':'black',
                   'alpha':0.3}
        
    if kde_kws is None:
        kde_kws = {'color':'black'}
    
    sns.distplot(df[col],ax=ax,kde_kws=kde_kws, hist_kws=hist_kws)

    label_fonts = {'weight':'bold',
                   'family':'serif',
                  'size':14}
    title_fonts = {'weight':'bold',
                   'family':'serif',
                  'size':20}

    ax.set_title(f'Distribution of {col}',fontdict=title_fonts)


    ax.set_ylabel('Density',fontdict=label_fonts)
    ax.set_xlabel(ax.get_xlabel(),fontdict=label_fonts)

    ax = axes[1]
    df.plot(kind='scatter',x=col,y=target,ax=ax)
    ax.set_title(f"{col.title()} vs {target}",fontdict=title_fonts)
    ax.set_ylabel(ax.get_ylabel(),fontdict=label_fonts)
    ax.set_xlabel(ax.get_xlabel(),fontdict=label_fonts)


    plt.tight_layout()
    plt.show()
    
    return fig, axes
    
# f,a = eda_plot(df,col='sqft_living',kde_kws={'color':'red','ls':':'})