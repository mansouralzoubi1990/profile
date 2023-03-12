from django.shortcuts import render,get_object_or_404
from .models import CV,Skill,About_Paragraph,Services,Achivmenet,Blog,BlogImgs
from django.db.models import Q


def index(request):
    cv = CV.objects.first()
    skills = Skill.objects.all().order_by('-id')
    aboutParagraph = About_Paragraph.objects.filter(cv=cv)
    services = Services.objects.all().order_by('-id')
    achivmenet = Achivmenet.objects.first()
    achivmenet_1 = achivmenet.worksCompleted
    achivmenet_2 = achivmenet.yearOfExperiance
    achivmenet_3 = achivmenet.totalclients
    achivmenet_4 = achivmenet.awardWon
    blog = Blog.objects.all().order_by('-created')[:6]
    context = {
        'cv':cv,'skills':skills,'aboutParagraph':aboutParagraph
        ,'services':services,'achivmenet_1':achivmenet_1,'achivmenet_2':achivmenet_2,
        'achivmenet_3':achivmenet_3,'achivmenet_4':achivmenet_4,'blog':blog
    }
    return render(request,'index.html',context)


def blog(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    imgs = BlogImgs.objects.filter(blog=blog)
    context = {"blog":blog,'imgs':imgs}
    return render(request,'portfolio-details.html',context)


def blogList(request):
    category = [] 
    blog = Blog.objects.all().order_by('-created')
    for i in blog:
        cate = i.category
        category.append(cate)
    category = [*set(category)]
    if request.method == "POST":
        s = request.POST.get('search')
        c = request.POST.get('cat')
        if c:
            blog = blog.filter(category=c)
        if s:
            blog = blog.filter(Q(title__icontains=s)|Q(text__icontains=s))
        
    context = {"blog":blog,"category":category}
    return render(request,'portfolio_list.html',context)