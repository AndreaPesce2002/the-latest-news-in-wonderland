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
def latest_news(argomenti,cat):
    """useful for knowing the latest news, the input is the news category"""
    categories = [
            'politica',
            'economia e finanza',
            'scienza e tecnologia',
            'viaggi e turismo',
            'sport',
            'cronaca',
            'stili di vita e tempo libero',
            'salute',
            'arti e spettacolo',
            'societa',
            'esteri',
            'economia',
            'inchieste',
            'spettacolo', 
        ]
    news=[]
    
    argomenti = argomenti.split(',')
    
    if all(argomento in categories for argomento in argomenti):
        for argomento in argomenti:
            news.append(print_news(argomento))
    else:
        for category in categories:
            news.append(print_news(category))
        
    return news