from django.shortcuts import render, redirect

from recipes.forms.recipes import RecipeForm, DeleteRecipeForm
from recipes.models import Recipe


def create_recipe(request):
    if request.method == 'GET':
        context = {
            'form': RecipeForm(),
        }
        return render(request, 'create.html', context)
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
        }
        return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': RecipeForm(instance=recipe),
        }
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'recipe': recipe,
            'form': form,
        }
        return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': DeleteRecipeForm(instance=recipe),
        }
        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('index')


def show_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe.ingredientes = recipe.ingredients.split(",")
    context = {
        'recipe': recipe,
    }
    return render(request, 'details.html', context)
