from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "<img src='https://images.techinsider.ru/upload/img_cache/bab/bab3324f6b0470e5156a1ebd5e48ce14_ce_1920x1280x0x0_cropped_666x444.jpg'>"
        "<style>img{width:1000px}")