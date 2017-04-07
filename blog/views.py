from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
<html>
<head>
<style>
.cities {
    background-color:black;
    color:white;
    margin:20px;
    padding:20px;
}	
</style>
</head>

<body>

<div class="cities">
<h2>Marmot的博客首页</h2>

<p>这是一个毛燥的首页</p>
<p>迈出WEB的第一步</p>
</div> 

</body>
</html>
    """)