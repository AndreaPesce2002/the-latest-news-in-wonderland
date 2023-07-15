from cat.mad_hatter.decorators import tool
import feedparser


def print_news(category):
    category_url = 'https://www.rainews.it/rss/' + category.replace(' ', '')
    d = feedparser.parse(category_url)
    news_list = []
    for i in range(3):
        news = d['entries'][i]
        news_list.append({
            'category': category,
            'Title': news['title'],
            'Summary': news['summary'],
            'Link': news['links'][0]['href'],
            'Published': news['published']
        })
    return news_list


@tool()
def latest_news(cat):
    """This tool is useful to gather the latest news."""
    categories = ['politica',
            'economia e finanza',
            'scienza e tecnologia',
            'viaggi e turismo',
            'sport', 'cronaca',
            'stili di vita e tempo libero',
            'salute', 'arti e spettacolo',
            'societa',
            'esteri',
            'economia',
            'inchieste',
            'spettacolo', 
        ]
    news=[]
    for category in categories:
        news.append(print_news(category))
        
    return news