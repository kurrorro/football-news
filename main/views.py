from django.http import HttpResponse # fungsi?
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import NewsForm
from main.models import News

def show_main(request):
    news_list = News.objects.all()
    context = {
        'npm' : '2406437331',
        'name': 'Keisha Vania Laurent',
        'class': 'PBP B',
        'news_list': news_list
    }

    return render(request, "main.html", context)

def create_news(request): # menghasilkan form yang dapat menambahkan data News secara otomatis ketika data di-submit dari form
    form = NewsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_news.html", context)

def show_news(request, id):
    news = get_object_or_404(News, pk=id) # untuk mengambil objek News berdasarkan primary key (id). Jika objek tidak ditemukan, akan mengembalikan halaman 404.
    news.increment_views() # menambah jumlah views

    context = {
        'news': news
    }

    return render(request, "news_detail.html", context)

def show_xml(request):
    news_list = News.objects.all()
    xml_data = serializers.serialize("xml", news_list) # translate objek model menjadi format lain seperti dalam fungsi ini adalah XML.
    return HttpResponse(xml_data, content_type="application/xml") 

def show_json(request):
    news_list = News.objects.all()
    json_data = serializers.serialize("json", news_list)
    return HttpResponse(json_data, content_type="application/json") # return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter ?

def show_xml_by_id(request, news_id):
    try: 
        news_item = News.objects.filter(pk=news_id) # ambil sesuai id
        xml_data = serializers.serialize("xml", news_item) # serialisasi jd xml
        return HttpResponse(xml_data, content_type="application/xml") # return HttpResponse yg berisi parameter data hasil query yg sdh diserialisasi
    except News.DoesNotExist:
       return HttpResponse(status=404)



def show_json_by_id(request, news_id):
    try: 
        news_item = News.objects.get(pk=news_id) # get terbatas 1 objek
        json_data = serializers.serialize("json", [news_item])
        return HttpResponse(json_data, content_type="application/json")
    except News.DoesNotExist:
       return HttpResponse(status=404)