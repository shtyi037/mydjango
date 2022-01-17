from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# 定義視圖函數
def hello(request):
    # TODO 編寫試圖邏輯
    return HttpResponse("<h1>Hello, world.世界你好.</h1>")

# 定義類基礎視圖
class MyView(View):
    def get(self, request):
        # TODO 編寫試圖邏輯
        return HttpResponse('<h1>類基礎視圖</h1>')