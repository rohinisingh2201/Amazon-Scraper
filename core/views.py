from django.shortcuts import render
from django.http import HttpResponse


def amazon(pro):
    import requests
    # pro = input("Search for the product: ")
    url = f'https://www.amazon.in/s?k={pro}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers)
    return response

def homeView(request):
    return render(request, 'core2/home.html')

def results(request):
    # print('hello')
    import base64
    names = []
    prices = []
    images = []
    if 'pro' in request.GET:
        pro = request.GET.get('pro')
        response = amazon(pro)
        from bs4 import BeautifulSoup
        import lxml

        soup = BeautifulSoup(response.text, 'lxml')

        # products = soup.find_all('div', {'class': 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'})

        products = soup.find_all('div', {
            'class': 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'}) if soup.find_all(
            'div', {
                'class': 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'}) else soup.find_all(
            'div', {
                'class': 'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})

        for product in products:
            names.append(product.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).get_text())

            prices.append(product.find('span', {
                'class': 'a-price-whole'}).get_text() if product.find(
                'span', {
                    'class': 'a-price-whole'}) else product.find('span', {
                'class': 'a-price-whole'}).get_text())
            images.append(product.find('img', {'class': 's-image'}).get('src') if product.find('img', {
                'class': 's-image'}) else '')

    data = zip(names, prices, images)
    return render(request, 'core2/new.html', {'items': data})
