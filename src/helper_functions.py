import folium
import matplotlib.pyplot as plt
import missingno

def preview_data(df):
    print(df.shape)
    print(df.head())
    print(df.info())
    print(df.describe())
    
def make_bar_plot(df_, column, X_tick_labels, title, df_title, y_label, x_label, limit=None):
    fig, ax = plt.subplots(1, figsize=(16,9))

    if limit:
        data = df_.groupby(column).size().sort_values(ascending=False)[:limit]
    else:
        data = df_.groupby(column).size().sort_values(ascending=False)
    
    X = data.index.astype(str)
    Y = data

    ax.bar(X, Y, color=(.1, .3, .5))
    ax.axhline(data.mean(), color=(.9, .5, .1), linestyle='-.', linewidth=5)
    
    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    plt.xticks(range(len(X)), X_tick_labels, rotation=90)
    
    plt.savefig(f'../figs/{df_title}_{"_".join(title.lower().split(" "))}.png', bbox_inches='tight');
    
def nullity_matrix(df_, df_title):
    ax = missingno.matrix(df_, figsize=(16,9), color=(.1, .3, .5))
    ax.set_title('Nullity Matrix')
    ax.figure.savefig(f'../figs/{df_title}_nullity_matrix.png', bbox_inches='tight')
    
def make_location_df(df_):
    location_df = df_[~df_['Latitude'].isna()]
    location_df.drop(['Event Number', 'Complaint Number'], axis=1, inplace=True)

    center_lat = location_df['Latitude'].mean()
    center_long = location_df['Longitude'].mean()

    lat = location_df['Latitude'].to_numpy()
    long = location_df['Longitude'].to_numpy()
    
    return location_df, center_lat, center_long, lat, long

def map_plot(df_, df_title):
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