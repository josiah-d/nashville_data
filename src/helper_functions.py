import folium
import matplotlib.pyplot as plt
import missingno


def preview_data(df_):
    '''
    Provides an overview of the data

    params
    ======
    df_ (pandas.core.frame.DataFrame): pandas dataframe

    attrs
    =====
    none

    returns
    =======
    none
    '''
    print(df_.shape)
    print(df_.head())
    print(df_.info())
    print(df_.describe())


def make_bar_plot(df_, column, X_tick_labels, title, df_title, y_label, x_label, color, limit=None):
    '''
    Basic construct of a bar plot that can be used across most features

    params
    ======
    df_ (pandas.core.frame.DataFrame): pandas dataframe
    column (str): name of the feature column to view the data
    X_tick_labels (list): contains strings to label the x ticks
    title (str): title for the plot
    df_title (str): aids in consistent naming
    y_label (str): y label for the plot
    x label (str): x label for the plot
    color (tuple): contains RGB float values
    limit (DEFAULT=None, int): allows a threshold to be set to limit the x ticks

    attrs
    =====
    none

    returns
    =======
    none
    '''
    fig, ax = plt.subplots(1, figsize=(16, 9))

    if limit:
        data = df_.groupby(column).size().sort_values(ascending=False)[:limit]
    else:
        data = df_.groupby(column).size().sort_values(ascending=False)

    X = data.index.astype(str)
    Y = data

    ax.bar(X, Y, color=color)
    ax.axhline(data.mean(), color=(.9, .5, .1), linestyle='-.', linewidth=5)

    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    plt.xticks(range(len(X)), X_tick_labels, rotation=90)

    plt.savefig(
        f'../figs/{df_title}_{"_".join(title.lower().split(" "))}.png', bbox_inches='tight')


def make_dt_bar_plot(df_, title, df_title, y_label, x_label, color, limit=None):
    '''
    Basic construct of a bar plot tailored to a datetime feature

    params
    == == ==
    df_(pandas.core.frame.DataFrame): pandas dataframe
    title(str): title for the plot
    df_title(str): aids in consistent naming
    y_label(str): y label for the plot
    x label(str): x label for the plot
    color(tuple): contains RGB float values
    limit(DEFAULT=None, int): allows a threshold to be set to limit the x ticks

    attrs
    == == =
    none

    returns
    == == == =
    none
    '''
    fig, ax = plt.subplots(1, figsize=(16, 9))

    if x_label == 'year':
        data = df_.groupby(df_['Call Received'].dt.year).size()
        X_tick_labels = ['2015', '2016', '2017',
                         '2018', '2019', '2020', '2021', '2022']
    elif x_label == 'month':
        data = df_.groupby(df_['Call Received'].dt.month).size()
        X_tick_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                         'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Now', 'Dec']
    elif x_label == 'hour':
        data = df_.groupby(df_['Call Received'].dt.hour).size()
        X_tick_labels = ['0000', '0100', '0200', '0300', '0400', '0500', '0600', '0700', '0800', '0900', '1000', '1100',
                         '1200', '1300', '1400', '1500', '1600', '1700', '1800', '1900', '2000', '2100', '02200', '02300', ]

    X = data.index.astype(str)
    Y = data

    ax.bar(X, Y, color=color)
    ax.axhline(data.mean(), color=(.9, .5, .1), linestyle='-.', linewidth=5)

    ax.set_title(title+x_label.title())
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    plt.xticks(range(len(X)), X_tick_labels, rotation=90)

    plt.savefig(
        f'../figs/{df_title}_{"_".join(title.lower().split(" "))}{x_label}.png', bbox_inches='tight')


def nullity_matrix(df_, df_title, color):
    '''
    Visual display of the missing data across all features

    params
    ======
    df_ (pandas.core.frame.DataFrame): pandas dataframe
    df_title(str): aids in consistent naming
    color(tuple): contains RGB float values

    attrs
    =====
    none

    returns
    =======
    none
    '''
    ax = missingno.matrix(df_, figsize=(16, 9), color=color)
    ax.set_title('Nullity Matrix')
    ax.figure.savefig(
        f'../figs/{df_title}_nullity_matrix.png', bbox_inches='tight')


def make_location_df(df_):
    '''
    Subsets the data to only include rows with complete lat/long

    params
    ======
    df_ (pandas.core.frame.DataFrame): pandas dataframe

    attrs
    =====
    none

    returns
    =======
    location_df (pandas.core.frame.DataFrame): pandas dataframe
    center_lat (float): mean latitude of all available data 
    center_long (float): mean longitude of all available data
    lat (numpy.ndarry): contains floats of all latitudes
    long (numpy.ndarry): contains floats of all longitudes
    '''
    location_df = df_[~df_['Latitude'].isna()]
    location_df.drop(['Event Number', 'Complaint Number'],
                     axis=1, inplace=True)

    location_df = location_df[(location_df != 0).all(1)]

    center_lat = location_df['Latitude'].mean()
    center_long = location_df['Longitude'].mean()

    lat = location_df['Latitude'].to_numpy()
    long = location_df['Longitude'].to_numpy()

    return location_df, center_lat, center_long, lat, long


def map_plot(df_, df_title):
    '''
    Plots an .html map of a particular feature

    params
    ======
    df_ (pandas.core.frame.DataFrame): pandas dataframe
    df_title(str): aids in consistent naming

    attrs
    =====
    none

    returns
    =======
    map_ (folium.folium.Map): object contian the map data with overlay
    '''
    location_df, center_lat, center_long, lat, long = make_location_df(df_)

    map_ = folium.Map(location=[center_lat, center_long], zoom_start=11)

    for lat_, long_ in zip(lat, long):
        folium.CircleMarker(
            location=[lat_, long_],
            radius=3,
            color=(0, 0, 0),
            fill_color=(.5, .5, .5),
            fill_opacity=0.05).add_to(map_)

    map_.save(f'../figs/{df_title}_map.html')
    return map_
