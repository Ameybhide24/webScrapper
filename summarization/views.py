import imp
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .scrapper import Scrapper


def summarize(request):
    print("done")

    # replace hardcoded url with request.data.url
    url = "https://www.amazon.in/Columbia-Mens-wind-resistant-Glove/dp/B0772WVHPS/?_encoding=UTF8&pd_rd_w=d9RS9&pf_rd_p=3d2ae0df-d986-4d1d-8c95-aa25d2ade606&pf_rd_r=7MP3ZDYBBV88PYJ7KEMJ&pd_rd_r=550bec4d-5268-41d5-87cb-8af40554a01e&pd_rd_wg=oy8v8&ref_=pd_gw_cr_cartx&th=1"

    scrap = Scrapper(url)
    review_results = scrap.scrape_reviews()
    print(len(review_results))
    return JsonResponse({"review": review_results})
