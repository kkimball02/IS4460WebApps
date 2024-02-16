from django.views import View
from django.shortcuts import render, redirect
from my_app import myfunctions
from my_app import my_objects

def title_name(the_name):
    return the_name.title()

class HomePageView(View):
    def get(self, request):
        my_name = "KYLER"
        names = ["Kyler", "John", "Shaniqua"]
        new_name = title_name(my_name)

        fixed_names = myfunctions.fix_names_list(names)

        car1 = my_objects.Car(color = "Blue", sound = "Honk! Honk!", year = "2005", 
                              make = "Honda", model = "Accord")
        car2 = my_objects.Car(color = "Red", sound = "Beep! Beep!", year = "2020",
                              model= "Lamborgini", make = "Aventador")
        motorcycle = my_objects.Motorcycle(make = "Harley Davidson", 
                                           model = "Road King",
                                            year = "2012", color = "White", 
                                            sound = "Vrrrm")



        context = {'hi':'Hello World!', 'name': new_name, 
                   'names': names, 'fixed_names': fixed_names, 'car1':car1,
                     'car2':car2, 'motorcycle':motorcycle}
        return render(request, 'my_app/index.html', context)
    
